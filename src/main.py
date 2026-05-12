import general_functions
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
    sellers,
    listed_names
)
from schedule import (
    create_schedule,
    delete_schedule,
    read_schedule,
    update_schedule,
    schedules
)
from sessions import (
    create_session,
    read_session,
    update_session,
    delete_session,
    sessions_dict,
    default_session_dict
)

save_file = Path("sellers.json")

seller_saves={}

def main():
    while True:
        print("======Menu======")
        print("1 - Select seller")
        print("2 - Edit sellers")
        print("3 - Sessions")
        print("4 - Schedule")
        print("5 - Leave")
        make_choice=general_functions.validation_check_2(5)
        if make_choice == 1:
            seller_id=int(input("Enter seller's name: "))
            for i in sellers:
                if seller_id==sellers[i]["ID"]:
                    name=i
            if name in listed_names:
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
                                return_code, return_name=create_product(item_name, item_price, item_quantity, item_class, name)
                                if return_code == 200:
                                    print(return_name+" added successfully")
                                else:
                                    print("Item not added")
                            elif make_choice == 2:
                                if name in items:
                                    item_id=general_functions.validation_check()
                                    return_code, return_item_values, return_item_quantity=read_product_by_id(item_id, name)
                                    if return_code==200:
                                        print(return_item_values+ " quantity:"+ str(return_item_quantity))
                                    else:
                                        print("Item not found")
                                else:
                                    print("Add items first")
                            elif make_choice == 3:
                                if name in items:
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
                                        return_code, return_item_values, return_item_quantity=update_product(item_id,new_name,new_class,new_price,new_quantity, name)
                                    else:
                                        return_code= 204, "no content"
                                    if return_code == 200:
                                        print(return_item_values+ " quantity:"+ str(return_item_quantity))
                                    elif return_code == 204:
                                        print("No class to choose from")
                                    else:
                                        print("Item not modified")
                                else:
                                    print("Add items first")
                            elif make_choice == 4:
                                if name in items:
                                    item_id = general_functions.validation_check()
                                    return_code, return_name=delete_product(item_id, name)
                                    if return_code==200:
                                        print(return_name+" removed successfully")
                                    else:
                                        print("Item not found")
                                else:
                                    print("Add items first")
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
                                return_code=create_item_order(item_id,item_quantity,name)
                                if return_code==200:
                                    print("Item added successfully to cart")
                                else:
                                    print("Item not found")
                            elif make_choice == 2:
                                if name in sales:
                                    return_code=read_item_order(name)
                                    if return_code==200:
                                        print("Item view successfully")
                                    else:
                                        print("No items to view")
                                else:
                                    print("Add items to order first")
                            elif make_choice == 3:
                                if name in sales:
                                    if len(sales[name]["temp_order"]["items"]) > 0:
                                        counter = 1
                                        for i in sales[name]["temp_order"]["items"].keys():
                                            print(str(counter) + " - " + str(sales[name]["temp_order"]["items"][i]))
                                            counter = counter + 1
                                        make_choice = general_functions.validation_check_2(counter - 1)
                                        item_name = list(sales[name]["temp_order"]["items"])[make_choice - 1]
                                        print("Input item quantity")
                                        item_quantity = general_functions.validation_check()
                                        return_code=update_item_order(item_name,item_quantity,name)
                                    else:
                                        return_code = 204, "no content"
                                    if return_code==200:
                                        print("Item edited successfully")
                                    elif return_code == 204:
                                        print("No items to edit")
                                    else:
                                        print("Item not changed")
                                else:
                                    print("Add items to order first")
                            elif make_choice == 4:
                                if name in sales:
                                    item_name=input("Input item name:")
                                    return_code=delete_item_order(item_name,name)
                                    if return_code==200:
                                        print("Item removed successfully")
                                    else:
                                        print("Item not found")
                                else:
                                    print("Add items to order first")
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
                print("========Editing sellers =======")
                print("1 - Create seller")
                print("2 - Read seller")
                print("3 - Update seller")
                print("4 - Delete seller")
                print("5 - Leave")
                make_choice = general_functions.validation_check_2(5)
                if make_choice == 1:
                    name = input("Write name of person: ")
                    name = name.lower()
                    extra_description = input("Extra description: ")
                    product_type = input("Type of product: ")
                    return_code, return_seller_values=create_seller(name, product_type, extra_description)
                    if return_code==200:
                        print(return_seller_values)
                    general_functions.pause()
                elif make_choice == 2:
                    print("Write seller id")
                    seller_id = general_functions.validation_check()
                    return_code,return_seller_values=read_sellers(seller_id)
                    if return_code==200:
                        for i in return_seller_values.items():
                            print(i)
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
                    return_code, return_seller_values= update_seller(input_id,name, product_type, extra_description)
                    if return_code==200:
                        print(return_seller_values)
                    else:
                        print("Id not found")
                    general_functions.pause()
                elif make_choice == 4:
                    print("Write seller id")
                    seller_id=general_functions.validation_check()
                    return_code, return_id=delete_sellers(seller_id)
                    if return_code==404:
                        print("sellers not found")
                    else:
                        print(str(return_id)+" deleted successfully")
                    general_functions.pause()
                else:
                    print("Leaving...")
                    general_functions.pause()
                    break
        elif make_choice==3:
            print("Write schedule id to create session")
            schedule_id=general_functions.validation_check()
            continue_path=False
            for i in schedules:
                if "id" in schedules[i]:
                    if schedule_id==schedules[i]["id"]:
                        schedule_name=i
                        continue_path=True
                        break
            if continue_path:
                while True:
                    if schedule_name not in sessions_dict:
                        sessions_dict[schedule_name]=default_session_dict
                    print("========Sessions========")
                    print("1 - Create session")
                    print("2 - Read session")
                    print("3 - Update session")
                    print("4 - Delete session")
                    print("5 - Leave")
                    make_choice = general_functions.validation_check_2(5)
                    if make_choice==1:
                        print("Input sellers id")
                        seller_id=general_functions.validation_check()
                        print("=======Day select=======")
                        print("1 - Monday")
                        print("2 - Tuesday")
                        print("3 - Wednesday")
                        print("4 - Thursday")
                        print("5 - Friday")
                        print("6 - Saturday")
                        print("7 - Sunday")
                        day_select=general_functions.validation_check_3(1,7)
                        print("=======Time select=======")
                        print("1 - 8:00-9:00")
                        print("2 - 9:00-10:00")
                        print("3 - 10:00-11:00")
                        print("4 - 11:00-12:00")
                        print("5 - 12:00-13:00")
                        print("6 - 13:00-14:00")
                        print("7 - 14:00-15:00")
                        print("8 - 15:00-16:00")
                        print("9 - 16:00-17:00")
                        print("10 - 17:00-18:00")
                        time_select=general_functions.validation_check_3(1,10)
                        return_code,session_return_dict=create_session(seller_id,schedule_name,day_select,time_select)
                        if return_code==200:
                            print(session_return_dict)
                        else:
                            print("cannot add more than 20 sessions in this time")
                    elif make_choice==2:
                        print("Input session id")
                        session_id=general_functions.validation_check()
                        return_code, return_session_dict=read_session(session_id)
                        if return_code==200:
                            print(return_session_dict)
                        else:
                            print("Session not found")
                    elif make_choice==3:
                        print("Input session id")
                        session_id=general_functions.validation_check()
                        print("=======Day select=======")
                        print("1 - Monday")
                        print("2 - Tuesday")
                        print("3 - Wednesday")
                        print("4 - Thursday")
                        print("5 - Friday")
                        print("6 - Saturday")
                        print("7 - Sunday")
                        day_select = general_functions.validation_check_3(1, 7)
                        print("=======Time select=======")
                        print("1 - 8:00-9:00")
                        print("2 - 9:00-10:00")
                        print("3 - 10:00-11:00")
                        print("4 - 11:00-12:00")
                        print("5 - 12:00-13:00")
                        print("6 - 13:00-14:00")
                        print("7 - 14:00-15:00")
                        print("8 - 15:00-16:00")
                        print("9 - 16:00-17:00")
                        print("10 - 17:00-18:00")
                        time_select = general_functions.validation_check_3(1, 10)
                        return_code, return_session_dict=update_session(session_id,schedule_name,day_select,time_select)
                        if return_code==200:
                            print(return_session_dict)
                        elif return_code==404:
                            print("Session not found")
                        else:
                            print("Cannot add more than 20 sessions in this time")
                    elif make_choice==4:
                        print("Input session id")
                        session_id=general_functions.validation_check()
                        return_code, return_session_id=delete_session(session_id)
                        if return_code==200:
                            print(str(return_session_id)+" deleted successfully")
                        else:
                            print("Session not found")
                    else:
                        print("Leaving...")
                        break
            else:
                print("Schedule not found")
        elif make_choice==4:
            while True:
                print("========Editing Schedule =======")
                print("1 - Create Schedule")
                print("2 - Read Schedule")
                print("3 - Update Schedule")
                print("4 - Delete Schedule")
                print("5 - Leave")
                make_choice = general_functions.validation_check_2(5)
                if make_choice == 1:
                    print("Input year")
                    year=general_functions.validation_check()
                    print("Input month")
                    month=general_functions.validation_check_2(12)
                    print("Input day")
                    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                        day=general_functions.validation_check_2(31)
                    elif month==2:
                        if year%4==0:
                            day=general_functions.validation_check_2(29)
                        else:
                            day = general_functions.validation_check_2(28)
                    else:
                        day = general_functions.validation_check_2(30)
                    return_code, schedule_id=create_schedule(day,month,year)
                    if return_code==200:
                        print("Schedule added with id "+ str(schedule_id))
                    else:
                        print("Schedule not added as schedule for that week already exists")
                    general_functions.pause()
                elif make_choice == 2:
                    print("Input ID:")
                    schedule_id=general_functions.validation_check()
                    return_code,schedule_dict=read_schedule(schedule_id)
                    if return_code==200:
                        for i in schedule_dict.items():
                            print(i)
                    else:
                        print("Schedule not found")
                elif make_choice == 3:
                    print("Input ID:")
                    schedule_id=general_functions.validation_check()
                    print("Input year")
                    year=general_functions.validation_check()
                    print("Input month")
                    month=general_functions.validation_check_2(12)
                    print("Input day")
                    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
                        day=general_functions.validation_check_2(31)
                    elif month==2:
                        if year%4==0:
                            day=general_functions.validation_check_2(29)
                        else:
                            day = general_functions.validation_check_2(28)
                    else:
                        day = general_functions.validation_check_2(30)
                    return_code, schedule_id=update_schedule(day,month,year,schedule_id)
                    if return_code==200:
                        print("Schedule date changed in "+ str(schedule_id))
                    elif return_code==404:
                        print("Schedule not found")
                    else:
                        print("Schedule not added as schedule for that week already exists")
                    general_functions.pause()
                elif make_choice == 4:
                    print("Input ID:")
                    schedule_id=general_functions.validation_check()
                    return_code,schedule_id=delete_schedule(schedule_id)
                    if return_code==200:
                        print(str(schedule_id)+" deleted successfully")
                    else:
                        print("schedule not found")
                else:
                    print("leaving...")
                    general_functions.pause()
                    break
        else:
            exit()

if __name__ == "__main__":
    main()
