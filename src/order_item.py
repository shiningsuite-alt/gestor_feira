import general_functions
from items_file import (
items,
lists
)
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

def add_item_order():
    while True:
        print("========Item select to Add========")
        print("1 - Select item by name")
        print("2 - Select item by class")
        print("3 - Select item by id")
        print("4 - stop")
        make_choice = general_functions.validation_check_2(4)
        if make_choice == 1 or make_choice == 2 or make_choice == 3:
            continue_path = False
            if make_choice == 1:
                item_name = input("Write item name:")
                if item_name in items:
                    continue_path = True
                else:
                    continue_path = False
            elif make_choice == 2:
                if "items_class" not in lists:
                    lists["items_class"] = []
                if len(lists["items_class"]) > 0:
                    print("========Select class========")
                    for i in range(len(lists["items_class"])):
                        print(str(i + 1) + " - " + lists["items_class"][i])
                    make_choice = general_functions.validation_check_2(len(lists["items_class"]))
                    item_class = lists["items_class"][make_choice - 1]
                    lists["items_class_temp"] = []
                    for i in items.keys():
                        if "item_class" in items[i]:
                            if item_class == items[i]["class"]:
                                lists["items_class_temp"].append(items[i]["name"])
                    for i in range(len(lists["items_class_temp"])):
                        print(str(i + 1) + " - " + lists["items_class_temp"][i])
                    make_choice = general_functions.validation_check_2(len(lists["items_class_temp"]))
                    item_name = lists["items_class_temp"][make_choice - 1]
                    continue_path = True
                else:
                    continue_path = False
            elif make_choice == 3:
                print("Write item id")
                item_id = general_functions.validation_check()
                for i in items.keys():
                    if "item_id" in items[i]:
                        if item_id == items[i]["id"]:
                            item_name = i
                            continue_path = True
                            break
                        else:
                            continue_path = False
            if continue_path:
                print("Write item quantity")
                item_quantity = general_functions.validation_check_2(items["quantities"][item_name])
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
                general_functions.pause()
            else:
                print("Item not found or no classes exist")
                general_functions.pause()
        else:
            print("Cancelling")
            general_functions.pause()
            break

def remove_item_order():
    if len(sales["temp_order"]["items"]) > 0:
        print("========Remove from order========")
        counter = 1
        for i in sales["temp_order"]["items"].keys():
            print(str(counter) + " - " + str(sales["temp_order"]["items"][i]))
            counter += 1
        make_choice = general_functions.validation_check_2(len(sales["temp_order"]))
        item_name = list(sales["temp_order"]["items"])[make_choice - 1]
        items["quantities"][item_name] += sales["temp_order"]["quantities"][item_name]
        del sales["temp_order"]["items"][item_name]
        del sales["temp_order"]["quantities"][item_name]
        print("Order has been removed")
        general_functions.pause()
    else:
        print("Add something to remove")
        general_functions.pause()

def edit_item_order():
    if len(sales["temp_order"]["items"]) > 0:
        counter = 1
        for i in sales["temp_order"]["items"].keys():
            print(str(counter) + " - " + str(sales["temp_order"]["items"][i]))
            counter = counter + 1
        make_choice = general_functions.validation_check_2(counter - 1)
        item_name = list(sales["temp_order"]["items"])[make_choice - 1]
        while True:
            print("======Edit item======")
            print("1 - Edit quantity")
            print("2 - Leave")
            make_choice = general_functions.validation_check_2(2)
            if make_choice == 1:
                items["quantities"][item_name] += sales["temp_order"]["quantities"][item_name]
                sales["temp_order"]["quantities"][item_name] = 0
                print("Write new quantity")
                sales["temp_order"]["quantities"][item_name] = general_functions.validation_check_2(items["quantities"][item_name])
                items["quantities"][item_name] -= sales["temp_order"]["quantities"][item_name]
                sales["temp_order"]["items"][item_name]["price"] = items[item_name]["price"] * sales["temp_order"]["quantities"][item_name]
                print("Quantity has been changed")
            else:
                print("leaving...")
                general_functions.pause()
                break
        general_functions.pause()
    else:
        print("Add something to view")
        general_functions.pause()

def view_item_order():
    if len(sales["temp_order"]["items"]) > 0:
        counter = 1
        for i in sales["temp_order"]["items"].keys():
            print(str(counter) + " - " + str(sales["temp_order"]["items"][i]))
            counter += 1
        general_functions.pause()
    else:
        print("Add something to view")
        general_functions.pause()