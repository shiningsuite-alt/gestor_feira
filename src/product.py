import general_functions
import os
import json
products_file="products.json"

items =  {
}
default_items =  {
    "quantities":{}
}
lists= {
    "items[seller_name]_class":[]
}

def guardar_produtos():
    with open(products_file, "w", encoding="utf-8") as ficheiro:
        json.dump(items, ficheiro, indent=4, ensure_ascii=False)
def carregar_produtos():
    global items
    if os.path.exists(products_file):
        with open(products_file, "r", encoding="utf-8") as ficheiro:
            items = json.load(ficheiro)
    else:
        items = {}

def create_product(name,price,quantity,item_class, seller_name):
    carregar_produtos()
    if seller_name not in items:
        items[seller_name] = default_items
    if name not in items[seller_name]:
        items[seller_name][name] = {}
        id_item = 1
        for i in items[seller_name].keys():
            if "id" in items[seller_name][i]:
                if id_item == items[seller_name][i]["id"]:
                    id_item += 1
        items[seller_name][name]["id"] = id_item
        items[seller_name][name]["name"]=name
        items[seller_name][name]["price"] = price
        items[seller_name]["quantities"][name] = quantity
        items[seller_name][name]["class"] = item_class
        print("Added  " + name)
        general_functions.pause()
        guardar_produtos()
        return 200, name
    else:
        guardar_produtos()
        return 409, "Already exists"

def update_product(item_id,new_name,new_class,new_price,new_quantity, seller_name):
    carregar_produtos()
    failure = True
    change = False
    things_changed=[]
    for i in items[seller_name].keys():
        if "id" in items[seller_name][i]:
            if item_id == items[seller_name][i]["id"]:
                item_name = i
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    if failure:
        print("Item doesn't exist")
        general_functions.pause()
    if item_name!=new_name:
        items[seller_name][new_name] = items[seller_name][item_name]
        del items[seller_name][item_name]
        items[seller_name]["quantities"][new_name] = items[seller_name]["quantities"][item_name]
        del items[seller_name]["quantities"][item_name]
        items[seller_name][new_name]["name"] = new_name
        item_name = new_name
        print("Item name has been changed")
        change=True
    if items[seller_name][item_name]["class"] != new_class:
        items[seller_name][item_name]["class"] = new_class
        print("Class has been changed")
        change=True
    if items[seller_name][item_name]["price"] != new_price:
        items[seller_name][item_name]["price"] = new_price
        print("Price has been changed")
        change=True
    if items[seller_name][item_name]["class"] != new_quantity:
        items[seller_name]["quantities"][item_name] = new_quantity
        change=True
    guardar_produtos()
    if change:
        return 200, items[seller_name][item_name], items[seller_name]["quantities"][item_name]
    else:
        return 304, "no change"

def delete_product(item_id, seller_name):
    carregar_produtos()
    failure = True
    for i in items[seller_name].keys():
        if "id" in items[seller_name][i]:
            if item_id == items[seller_name][i]["id"]:
                print("Removed " + i)
                del items[seller_name][i]
                del items[seller_name]["quantities"][i]
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    guardar_produtos()
    if failure:
        return 404, i
    else:
        return 200, "success"

def read_product_by_id(item_id, seller_name):
    failure = True
    for i in items[seller_name].keys():
        if "id" in items[seller_name][i]:
            if item_id == items[seller_name][i]["id"]:
                for j in items[seller_name][i].items[seller_name]():
                    print(j)
                print(items[seller_name]["quantities"][i])
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    if failure:
        return 404, "not found"
    else:
        return 200, items[seller_name][i], items[seller_name]["quantities"][i]