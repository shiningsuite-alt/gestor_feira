import general_functions

items =  {
    "quantities":{}
}
default_items =  {
    "quantities":{}
}
lists= {
    "items_class":[]
}

def add_product(name,price,quantity,item_class):
    if name not in items:
        items[name] = {}
        id_item = 1
        for i in items.keys():
            if "id" in items[i]:
                if id_item == items[i]["id"]:
                    id_item += 1
        items[name]["id"] = id_item
        items[name]["name"]=name
        items[name]["price"] = price
        items["quantities"][name] = quantity
        items[name]["class"] = item_class
        print("Added  " + name)
        general_functions.pause()
        return 200
    else:
        return 409

def change_product(item_id,new_name,new_class,new_price,new_quantity):
    failure = True
    change = False
    things_changed=[]
    for i in items.keys():
        if "id" in items[i]:
            if item_id == items[i]["id"]:
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
        items[new_name] = items[item_name]
        del items[item_name]
        items["quantities"][new_name] = items["quantities"][item_name]
        del items["quantities"][item_name]
        items[new_name]["name"] = new_name
        item_name = new_name
        print("Item name has been changed")
        change=True
    if items[item_name]["class"] != new_class:
        items[item_name]["class"] = new_class
        print("Class has been changed")
        change=True
    if items[item_name]["price"] != new_price:
        items[item_name]["price"] = new_price
        print("Price has been changed")
        change=True
    if items[item_name]["class"] != new_quantity:
        items["quantities"][item_name] = new_quantity
        change=True
    if change:
        return 200
    else:
        return 304

def remove_product(item_id):
    failure = True
    for i in items.keys():
        if "id" in items[i]:
            if item_id == items[i]["id"]:
                print("Removed " + i)
                del items[i]
                del items["quantities"][i]
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    if failure:
        return 404
    else:
        return 200

def search_product_by_id(item_id):
    failure = True
    for i in items.keys():
        if "id" in items[i]:
            if item_id == items[i]["id"]:
                for j in items[i].items():
                    print(j)
                print(items["quantities"][i])
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    if failure:
        return 404
    else:
        return 200