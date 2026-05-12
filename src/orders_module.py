import general_functions
import os
import json
from product import items
from product import lists
orders_file="orders.json"

default_sales = {
    "temp_order":{
        "quantities":{},
        "items[seller_name]":{}
    },
    "orders":{},
    "order_names":[]
}
sales = {
}

def save_orders():
    with open(orders_file, "w", encoding="utf-8") as ficheiro:
        json.dump(sales, ficheiro, indent=4, ensure_ascii=False)

def load_orders():
    global sales
    if os.path.exists(orders_file):
        with open(orders_file, "r", encoding="utf-8") as ficheiro:
            sales = json.load(ficheiro)
    else:
        sales = {}

def create_item_order(item_id,item_quantity,seller_name):
    load_orders()
    if seller_name not in sales:
        sales[seller_name] = default_sales
    item_name=""
    for i in items[seller_name]:
        if "id" in items[seller_name][i]:
            if items[seller_name][i]["id"] == item_id:
                item_name=i
                break
    if item_name!="":
        item_price = items[seller_name][item_name]["price"] * item_quantity
        if item_name not in sales[seller_name]["temp_order"]["items[seller_name]"]:
            sales[seller_name]["temp_order"]["items[seller_name]"][item_name] = {}
            sales[seller_name]["temp_order"]["items[seller_name]"][item_name]["name"] = item_name
            sales[seller_name]["temp_order"]["items[seller_name]"][item_name]["price"] = item_price
            sales[seller_name]["temp_order"]["quantities"][item_name] = item_quantity
            print(item_name + " has been added")
            items[seller_name]["quantities"][item_name] -= item_quantity
        else:
            sales[seller_name]["temp_order"]["items[seller_name]"][item_name]["price"] += item_price
            sales[seller_name]["temp_order"]["quantities"][item_name] += item_quantity
            items[seller_name]["quantities"][item_name] -= item_quantity
            print(str(item_quantity) + item_name + "(s) has(have) been added")
        save_orders()
        return 200, "success"
    else:
        return 404, "not found"

def delete_item_order(item_name,seller_name):
    load_orders()
    if item_name in sales[seller_name]["temp_order"]["items[seller_name]"]:
        items[seller_name]["quantities"][item_name] += sales[seller_name]["temp_order"]["quantities"][item_name]
        del sales[seller_name]["temp_order"]["items[seller_name]"][item_name]
        del sales[seller_name]["temp_order"]["quantities"][item_name]
        save_orders()
        return 200, "success"
    else:
        return 404, "not found"

def update_item_order(item_name,item_quantity,seller_name):
    load_orders()
    if sales[seller_name]["temp_order"]["quantities"][item_name]!=item_quantity:
        items[seller_name]["quantities"][item_name] += sales[seller_name]["temp_order"]["quantities"][item_name]
        sales[seller_name]["temp_order"]["quantities"][item_name] = 0
        sales[seller_name]["temp_order"]["quantities"][item_name] = general_functions.validation_check_2(items[seller_name]["quantities"][item_name])
        items[seller_name]["quantities"][item_name] -= sales[seller_name]["temp_order"]["quantities"][item_name]
        sales[seller_name]["temp_order"]["items[seller_name]"][item_name]["price"] = items[seller_name][item_name]["price"] * sales[seller_name]["temp_order"]["quantities"][item_name]
        save_orders()
        return 200, "success"
    else:
        return 304, "no change"

def read_item_order(seller_name):
    load_orders()
    if len(sales[seller_name]["temp_order"]["items[seller_name]"]) > 0:
        counter = 1
        for i in sales[seller_name]["temp_order"]["items[seller_name]"].keys():
            print(str(counter) + " - " + str(sales[seller_name]["temp_order"]["items[seller_name]"][i]) + ", quantities:'"+ str(sales[seller_name]["temp_order"]["quantities"][i])+"'")
            counter += 1
        return 200, "success"
    else:
        return 204, "No content"