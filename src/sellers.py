import general_functions
import json
import os
sellers_file = "sellers.json"

listed_names=[]
headers= [
    "Id",
    "Name",
    "Product type",
    "Time",
    "Day",
    "Description"
]

sellers={
}

def save_sellers():
    with open(sellers_file, "w", encoding="utf-8") as ficheiro:
        json.dump(sellers, ficheiro, indent=4, ensure_ascii=False)

def load_sellers():
    global sellers
    if os.path.exists(sellers_file):
        with open(sellers_file, "r", encoding="utf-8") as ficheiro:
            sellers = json.load(ficheiro)
    else:
        sellers = {}

def create_seller(name, product_type,extra_description):
    load_sellers()
    sellers[name]={}
    counter = 1
    if name not in listed_names:
        listed_names.append(name)
    counter=1
    for i in sellers:
        if "ID" in sellers[i]:
            if counter==sellers[i]["ID"]:
                counter+=1
    sellers[name]["ID"] = counter
    sellers[name]["name"] = name
    sellers[name]["product_type"] = product_type
    if extra_description == "" or extra_description == " ":
        sellers[name]["extra_description"]="none"
    else:
        sellers[name]["extra_description"]=extra_description
    save_sellers()
    return 200, sellers[name]

def read_sellers(seller_id):
    load_sellers()
    temp_list = []
    for name in sellers:
        if "ID" in sellers[name]:
            if sellers[name]["ID"] == seller_id:
                temp_list.append(sellers[name].values())
    if temp_list:
        return 200, sellers[name]
    else:
        return 404, "not found"

def update_seller(seller_id,new_name, product_type,extra_description):
    load_sellers()
    for i in sellers:
        if sellers[i]["ID"]==seller_id:
            name=i
            found=True
            break
        else:
            found=False
    if found:
        if new_name not in listed_names:
            listed_names.append(new_name)
        if sellers[name]["name"] != new_name:
            sellers[new_name]=sellers[name]
            del sellers[name]
            name=new_name
            sellers[name]["name"] = new_name
        if sellers[name]["product_type"] != product_type:
            sellers[name]["product_type"] = product_type
        if extra_description == "" or extra_description == " ":
            sellers[name]["extra_description"]="none"
        else:
            sellers[name]["extra_description"]=extra_description
        save_sellers()
        return 200, sellers[name]
    else:
        return 404, "not found"

def delete_sellers(id_select):
    load_sellers()
    for name in sellers:
        if "ID" in sellers[name]:
            if sellers[name]["ID"] == id_select:
                del sellers[name]
                found_id = True
                break
        else:
            found_id = False
    if not found_id:
        return 404, "not found"
    else:
        save_sellers()
        return 200, id_select
