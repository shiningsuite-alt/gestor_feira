import general_functions
from items_file import items
from items_file import lists

default_sales = {
    "temp_order":{
        "quantities":{},
        "items":{}
    },
    "orders":{},
    "order_names":[],
}
sales = {
    "temp_order":{
        "quantities":{},
        "items":{}
    },
    "orders":{},
    "order_names":[],
}

def create_item_order(item_id,item_quantity):
    item_name=""
    for i in items:
        if "id" in items[i]:
            if items[i]["id"] == item_id:
                item_name=i
                break
    if item_name!="":
        item_price = items[item_name]["price"] * item_quantity
        if item_name not in sales["temp_order"]["items"]:
            sales["temp_order"]["items"][item_name] = {}
            sales["temp_order"]["items"][item_name]["name"] = item_name
            sales["temp_order"]["items"][item_name]["price"] = item_price
            sales["temp_order"]["quantities"][item_name] = item_quantity
            print(item_name + " has been added")
            items["quantities"][item_name] -= item_quantity
        else:
            sales["temp_order"]["items"][item_name]["price"] += item_price
            sales["temp_order"]["quantities"][item_name] += item_quantity
            items["quantities"][item_name] -= item_quantity
            print(str(item_quantity) + item_name + "(s) has(have) been added")
        return 200, "success"
    else:
        return 404, "not found"

def delete_item_order(item_name):
    if item_name in sales["temp_order"]["items"]:
        items["quantities"][item_name] += sales["temp_order"]["quantities"][item_name]
        del sales["temp_order"]["items"][item_name]
        del sales["temp_order"]["quantities"][item_name]
        return 200, "success"
    else:
        return 404, "not found"

def update_item_order(item_name,item_quantity):
    if sales["temp_order"]["quantities"][item_name]!=item_quantity:
        items["quantities"][item_name] += sales["temp_order"]["quantities"][item_name]
        sales["temp_order"]["quantities"][item_name] = 0
        sales["temp_order"]["quantities"][item_name] = general_functions.validation_check_2(items["quantities"][item_name])
        items["quantities"][item_name] -= sales["temp_order"]["quantities"][item_name]
        sales["temp_order"]["items"][item_name]["price"] = items[item_name]["price"] * sales["temp_order"]["quantities"][item_name]
        return 200, "success"
    else:
        return 304, "no change"

def read_item_order():
    if len(sales["temp_order"]["items"]) > 0:
        counter = 1
        for i in sales["temp_order"]["items"].keys():
            print(str(counter) + " - " + str(sales["temp_order"]["items"][i]) + ", quantities:'"+ str(sales["temp_order"]["quantities"][i])+"'")
            counter += 1
        return 200, "success"
    else:
        return 204, "No content"