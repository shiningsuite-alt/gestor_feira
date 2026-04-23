import general_functions
from tabulate import tabulate
from pathlib import Path
from product import (
    create_product,
    update_product,
    delete_product,
    read_product_by_id,
    items,
    default_items,
    lists
)
from orders_module import (
    create_item_order,
    update_item_order,
    delete_item_order,
    read_item_order,
    sales,
    default_sales
)
from sellers import (
    create_seller,
    read_sellers,
    update_seller,
    delete_sellers,
    schedule
)

save_file = Path("sellers.json")

seller_saves={}

def main():
    while True:
        print("======Menu======")
        print("1 - Select seller")
        print("2 - Edit schedule")
        print("3 - Leave")
        make_choice=general_functions.validation_check_2(3)
        if make_choice == 1:
            name=input("Enter seller's name: ")
            name=name.lower()
            if name in schedule["listed_names"]:
                if name not in seller_saves:
                    seller_saves[name]={}
                if "items" not in seller_saves[name]:
                    seller_saves[name]["items"]={}
                if "orders" not in seller_saves[name]:
                    seller_saves[name]["sales"]={}
                if seller_saves[name]["items"]!={}:
                    items=seller_saves[name]["items"]
                else:
                    items=default_items
                if seller_saves[name]["sales"]!={}:
                    sales=seller_saves[name]["sales"]
                else:
                    sales=default_sales
                while True:
                    print("======= Sales =======")
                    print("1 - Manage stock")
                    print("2 - Manage Cart")
                    print("3 - Leave")
                    make_choice=general_functions.validation_check_2(3)
                    if make_choice == 1:
                        while True:
                            print("============Stock manager============")
                            print("1 - Create product")
                            print("2 - Update product")
                            print("3 - Delete product")
                            print("4 - Read product by id")
                            print("5 - Leave")
                            make_choice = general_functions.validation_check_2(5)
                            if make_choice == 1:
                                print("========Add product========")
                                item_name = input("Write item Name:")
                                item_name = item_name.lower()
                                print("Write item price")
                                item_price = general_functions.validation_check_float()
                                print("Write item quantity")
                                item_quantity = general_functions.validation_check()
                                while True:
                                    print("Item class")
                                    print("1 - Write a new item class")
                                    print("2 - Select a preexisting item class")
                                    make_choice = general_functions.validation_check_2(2)
                                    if make_choice == 1:
                                        item_class = input("Write item Class:")
                                        item_class = item_class.lower()
                                        if item_class not in lists["items_class"]:
                                            lists["items_class"].append(item_class)
                                        break
                                    else:
                                        if len(lists["items_class"]) > 0:
                                            counter = 1
                                            for i in lists["items_class"]:
                                                print(str(counter) + " -  " + i)
                                                counter += 1
                                            make_choice = general_functions.validation_check_2(len(lists["items_class"]))
                                            item_class = lists["items_class"][make_choice - 1]
                                            break
                                        else:
                                            print("No preexisting item classes")
                                            general_functions.pause()
                                return_code, return_name=create_product(item_name, item_price, item_quantity, item_class)
                                if return_code[0] == 200:
                                    print(return_name+" added successfully")
                                else:
                                    print("Item not added")
                            elif make_choice == 2:
                                item_id=general_functions.validation_check()
                                return_code, return_item_values, return_item_quantity=read_product_by_id(item_id)
                                if return_code[0]==200:
                                    print(return_item_values+ " quantity:"+ str(return_item_quantity))
                                else:
                                    print("Item not found")
                            elif make_choice == 3:
                                print("input item id")
                                item_id = general_functions.validation_check()
                                new_name=input("Input new name:")
                                if len(lists["items_class"])>0:
                                    print("Select class")
                                    for i in range(len(lists["items_class"])):
                                        print(str(i + 1) + " -  " + lists["items_class"][i])
                                    class_select = general_functions.validation_check_2(len(lists["items_class"]))
                                    new_class = lists["items_class"][class_select - 1]
                                    print("Input new price")
                                    new_price=general_functions.validation_check_float()
                                    print("Input new quantity")
                                    new_quantity=general_functions.validation_check()
                                    return_code, return_item_values, return_item_quantity=update_product(item_id,new_name,new_class,new_price,new_quantity)
                                else:
                                    return_code= 204, "no content"
                                if return_code[0] == 200:
                                    print(return_item_values+ " quantity:"+ str(return_item_quantity))
                                elif return_code[0] == 204:
                                    print("No class to choose from")
                                else:
                                    print("Item not modified")
                            elif make_choice == 4:
                                item_id = general_functions.validation_check()
                                return_code, return_name=delete_product(item_id)
                                if return_code[0]==200:
                                    print(return_name+" removed successfully")
                                else:
                                    print("Item not found")
                            else:
                                print("leaving...")
                                general_functions.pause()
                                break
                    elif make_choice == 2:
                        while True:
                            print("======Order manager======")
                            print("1 - Create item to order")
                            print("2 - Read items")
                            print("3 - Update items")
                            print("4 - Delete items")
                            print("5 - Finalize order")
                            print("6 - Leave")
                            make_choice = general_functions.validation_check()
                            if make_choice==1:
                                print("Input item id")
                                item_id=general_functions.validation_check()
                                print("Input item quantity")
                                item_quantity=general_functions.validation_check()
                                return_code=create_item_order(item_id,item_quantity)
                                if return_code[0]==200:
                                    print("Item added successfully to cart")
                                else:
                                    print("Item not found")
                            elif make_choice == 2:
                                return_code=read_item_order()
                                if return_code[0]==200:
                                    print("Item view successfully")
                                else:
                                    print("No items to view")
                            elif make_choice == 3:
                                if len(sales["temp_order"]["items"]) > 0:
                                    counter = 1
                                    for i in sales["temp_order"]["items"].keys():
                                        print(str(counter) + " - " + str(sales["temp_order"]["items"][i]))
                                        counter = counter + 1
                                    make_choice = general_functions.validation_check_2(counter - 1)
                                    item_name = list(sales["temp_order"]["items"])[make_choice - 1]
                                    print("Input item quantity")
                                    item_quantity = general_functions.validation_check()
                                    return_code=update_item_order(item_name,item_quantity)
                                else:
                                    return_code = 204, "no content"
                                if return_code[0]==200:
                                    print("Item edited successfully")
                                elif return_code[0] == 204:
                                    print("No items to edit")
                                else:
                                    print("Item not changed")
                            elif make_choice == 4:
                                item_name=input("Input item name:")
                                return_code=delete_item_order(item_name)
                                if return_code[0]==200:
                                    print("Item removed successfully")
                                else:
                                    print("Item not found")
                            elif make_choice == 5:
                                sales["temp_order"]=default_sales["temp_order"]
                            else:
                                print("leaving...")
                                general_functions.pause()
                                break
                            general_functions.pause()
                    else:
                        print("leaving")
                        seller_saves[name]["items"]= items
                        seller_saves[name]["sales"]= sales
                        general_functions.pause()
                        break
            else:
                print("Seller does not exist")
        elif make_choice==2:
            while True:
                schedule["print"]=[]
                for time in schedule["list_of_time"]:
                    temp_list = [time]
                    for day in schedule["list_of_days"]:
                        if len(schedule[day][time]) == 10:
                            temp_list.append("\033[32mFull\033[0m")
                        elif 10 > len(schedule[day][time]) > 0:
                            temp_list.append("\033[93mPartially filled\033[0m")
                        else:
                            temp_list.append("\033[31mEmpty\033[0m")
                    schedule["print"].append(temp_list)
                print("=======Schedule=======")
                print(tabulate(schedule["print"], headers=schedule["headers"], tablefmt="grid"))
                print("========Editing schedule =======")
                print("1 - Add seller")
                print("2 - View seller")
                print("3 - Edit seller")
                print("4 - Remove seller")
                print("5 - Leave")
                make_choice = general_functions.validation_check_2(5)
                if make_choice == 1:
                    name = input("Write name of person: ")
                    name = name.lower()
                    extra_description = input("Extra description: ")
                    product_type = input("Type of product: ")
                    counter=1
                    for i in schedule["list_of_days"]:
                        print(str(counter) + " - " + i)
                        counter+=1
                    print("Select day")
                    day_select = general_functions.validation_check_2(5)
                    day = schedule["list_of_days"][day_select - 1]
                    counter=1
                    for i in schedule["list_of_time"]:
                        print(str(counter) + " - " + i)
                        counter+=1
                    print("Select time")
                    time_select = general_functions.validation_check_2(9)
                    time = schedule["list_of_time"][time_select - 1]
                    return_code, return_seller_values=create_seller(name, product_type, extra_description, day, time)
                    if return_code[0]==200:
                        print(return_seller_values)
                    general_functions.pause()
                elif make_choice == 2:
                    print("Write seller id")
                    seller_id = general_functions.validation_check()
                    return_code,return_seller_values=read_sellers(seller_id)
                    if return_code[0]==200:
                        print(return_seller_values)
                    else:
                        print("Seller not found")
                    general_functions.pause()
                elif make_choice == 3:
                    print("Write seller id")
                    input_id=general_functions.validation_check()
                    name = input("Write name of person: ")
                    name = name.lower()
                    extra_description = input("Extra description: ")
                    product_type = input("Type of product: ")
                    counter=1
                    for i in schedule["list_of_days"]:
                        print(str(counter) + " - " + i)
                        counter+=1
                    print("Select day")
                    day_select = general_functions.validation_check_2(5)
                    day = schedule["list_of_days"][day_select - 1]
                    counter=1
                    for i in schedule["list_of_time"]:
                        print(str(counter) + " - " + i)
                        counter+=1
                    print("Select time")
                    time_select = general_functions.validation_check_2(9)
                    time = schedule["list_of_time"][time_select - 1]
                    return_code, return_seller_values= update_seller(input_id,name, product_type, extra_description, day, time)
                    if return_code[0]==200:
                        print(return_seller_values)
                    else:
                        print("Id not found")
                    general_functions.pause()
                elif make_choice == 4:
                    print("Write seller id")
                    seller_id=general_functions.validation_check()
                    return_code, return_name=delete_sellers(seller_id)
                    if return_code[0]==404:
                        print("sellers not found")
                    else:
                        print(return_name+" deleted successfully")
                    general_functions.pause()
                else:
                    print("Leaving...")
                    general_functions.pause()
                    break
        else:
            exit()

main()