import general_functions
import os
import tkinter as tk
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
    next_order,
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

#global variables#

selected_day=0
selected_time=0
name=""
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TIMES = ["8:00-9:00", "9:00-10:00", "10:00-11:00", "11:00-12:00","12:00-13:00", "13:00-14:00", "14:00-15:00", "15:00-16:00","16:00-17:00", "17:00-18:00"]

#background#

root=tk.Tk()
root.title("Gestor de feira")
root.state("zoomed")
root.resizable(False, 10)
root.configure(bg="#2E3440")

root.update_idletasks()

canvas = tk.Canvas(root, bg="white")

#button functions#

def sellers_window():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_current.place(relx=0.0508, rely=0.09)
    items_button_normal.place(relx=0.159, rely=0.11)
    orders_button_normal.place(relx=0.227, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    id_search_bar.place(relx=0.4,rely=0.29,anchor="center", width=root.winfo_width() * 0.5, height=root.winfo_height() * 0.075)
    search_seller_button.place(relx=0.68,rely=0.255)
    create_seller_button.place(relx=0.15,rely=0.41)
    update_seller_button.place(relx=0.15,rely=0.58)
    delete_seller_button.place(relx=0.15,rely=0.75)

def items_name_window():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_current.place(relx=0.12, rely=0.09)
    orders_button_normal.place(relx=0.22875, rely=0.11)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    id_search_bar.place(relx=0.4,rely=0.55,anchor="center", width=root.winfo_width() * 0.6, height=root.winfo_height() * 0.075)
    item_confirm.place(relx=0.8,rely=0.55, anchor="center")

def items_window_login():
    items_name_window()
    global name
    try:
        seller_id=int(id_search_bar.get())
        return_code, return_seller_values, seller_name = read_sellers(seller_id)
        name=seller_name
        if return_code == 200:
            item_window_real()
        else:
            tk.Label(root, text="Seller not found", font=("Arial", 15), bg="white", fg="red").place(relx=0.15, rely=0.65)
    except ValueError:
        error.place(relx=0.15,rely=0.65)

def item_window_real():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_current.place(relx=0.12, rely=0.09)
    orders_button_normal.place(relx=0.22875, rely=0.11)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    tk.Label(root, text=name, font=("Impact", 20), bg="white", fg="black").place(relx=0.5, rely=0.25,anchor="center")
    id_search_bar.place(relx=0.4, rely=0.34, anchor="center", width=root.winfo_width() * 0.5, height=root.winfo_height() * 0.075)
    search_item_button.place(relx=0.68,rely=0.3)
    create_item_button.place(relx=0.15,rely=0.44)
    update_item_button.place(relx=0.15, rely=0.58)
    delete_item_button.place(relx=0.15, rely=0.72)

def order_name_window():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_current.place(relx=0.189, rely=0.09)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    id_search_bar.place(relx=0.4,rely=0.55,anchor="center", width=root.winfo_width() * 0.6, height=root.winfo_height() * 0.075)
    order_confirm.place(relx=0.8,rely=0.55, anchor="center")

def order_window_login():
    order_name_window()
    global name
    try:
        seller_id=int(id_search_bar.get())
        return_code, return_seller_values, seller_name = read_sellers(seller_id)
        name=seller_name
        if return_code == 200:
            order_window_real()
        else:
            tk.Label(root, text="Seller not found", font=("Arial", 15), bg="white", fg="red").place(relx=0.15, rely=0.65)
    except ValueError:
        error.place(relx=0.15,rely=0.65)

def order_window_real():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_current.place(relx=0.189, rely=0.09)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    tk.Label(root, text=name, font=("Impact", 20), bg="white", fg="black").place(relx=0.5, rely=0.25, anchor="center")
    search_order_button.place(relx=0.15, rely=0.3)
    create_order_button.place(relx=0.15, rely=0.42)
    update_order_button.place(relx=0.15, rely=0.54)
    delete_order_button.place(relx=0.15, rely=0.66)
    new_order_button.place(relx=0.15, rely=0.78)

def schedule_window():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508,rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_normal.place(relx=0.189, rely=0.11)
    schedule_button_current.place(relx=0.258, rely=0.09)
    search_schedule_button.place(relx=0.11,rely=0.3)
    create_schedule_button.place(relx=0.11, rely=0.44)
    update_schedule_button.place(relx=0.11, rely=0.58)
    delete_schedule_button.place(relx=0.11, rely=0.72)
    for c, day in enumerate(DAYS, start=1):
        lbl = tk.Label(sessions_frame,text=day,font=("Arial", 10, "bold"))
        lbl.grid(row=0, column=c, padx=8, pady=8)
    for r, time in enumerate(TIMES, start=1):
        lbl = tk.Label(sessions_frame,text=time,font=("Arial", 10, "bold"),bg="gray")
        lbl.grid(row=r, column=0, padx=8, pady=8)
        for c, day in enumerate(DAYS, start=1):
            btn = tk.Button(sessions_frame,text="",width=10,height=2,bd=0,command=lambda day_id=c, time_id=r: sessions_window(day_id, time_id))
            btn.grid(row=r, column=c, padx=3, pady=3)
    sessions_frame.place(relx=0.4, rely=0.2,width=root.winfo_width() * 0.52,height=root.winfo_height() * 0.69)

def sessions_window(day_select, time_select):
    global selected_day, selected_time
    selected_day = day_select
    selected_time = time_select
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508,rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_normal.place(relx=0.189, rely=0.11)
    schedule_button_current.place(relx=0.258, rely=0.09)
    search_session_button.place(relx=0.11,rely=0.3)
    create_session_button.place(relx=0.11, rely=0.44)
    update_session_button.place(relx=0.11, rely=0.58)
    delete_session_button.place(relx=0.11, rely=0.72)

#Sellers#

def sellers_search():
    sellers_window()
    try:
        seller_id = int(id_search_bar.get())
        return_code, return_seller_values, seller_name = read_sellers(seller_id)
        if return_code == 200:
            create_seller_button.place_forget()
            delete_seller_button.place_forget()
            update_seller_button.place_forget()
            tk.Label(root, text="Id:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.4)
            tk.Label(root, text="Name:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.5)
            tk.Label(root, text="Product type:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.6)
            tk.Label(root, text="Extra description:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.7)
            tk.Label(root, text=str(return_seller_values["ID"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.4)
            tk.Label(root, text=return_seller_values["name"], font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.5)
            tk.Label(root, text=return_seller_values["product_type"], font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.6)
            tk.Label(root, text=return_seller_values["extra_description"], font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.7)
            return_button_seller.place(anchor="center",relx=0.5,rely=0.85)
        elif return_code==404:
            tk.Label(root, text="Seller not found", font=("Arial", 15), bg="white", fg="red").place(relx=0.15, rely=0.33)
    except ValueError:
        error.place(relx=0.15,rely=0.33)

def sellers_create_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_current.place(relx=0.0508, rely=0.09)
    items_button_normal.place(relx=0.159, rely=0.11)
    orders_button_normal.place(relx=0.227, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    create_seller_button.place(relx=0.15,rely=0.41)
    tk.Label(root, text="Name:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.26)
    tk.Label(root, text="Product type:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.42)
    tk.Label(root, text="Extra description:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.58)
    seller_name_input.place(relx=0.6, rely=0.26, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_product_type_input.place(relx=0.6, rely=0.42, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_description_input.place(relx=0.6, rely=0.58, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_create_confirm.place(relx=0.6,rely=0.74)
    return_button_seller.place(relx=0.2, rely=0.74)

def confirm_seller_create():
    sellers_create_menu()
    if seller_name_input.get() != "" and seller_product_type_input.get() != "":
        name = seller_name_input.get()
        product_type = seller_product_type_input.get()
        extra_description = seller_description_input.get()
        return_code, return_seller_values = create_seller(name, product_type, extra_description)
        tk.Label(root, text="Seller Created!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.85)
    else:
        error.place(relx=0.6,rely=0.85)

def sellers_update_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_current.place(relx=0.0508, rely=0.09)
    items_button_normal.place(relx=0.159, rely=0.11)
    orders_button_normal.place(relx=0.227, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    update_seller_button.place(relx=0.15,rely=0.58)
    tk.Label(root, text="ID:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.26)
    tk.Label(root, text="Name:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.38)
    tk.Label(root, text="Product type:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.50)
    tk.Label(root, text="Extra description:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.62)
    id_search_bar.place(relx=0.6, rely=0.26, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_name_input.place(relx=0.6, rely=0.38, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_product_type_input.place(relx=0.6, rely=0.50, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_description_input.place(relx=0.6, rely=0.62, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_update_confirm.place(relx=0.6,rely=0.74)
    return_button_seller.place(relx=0.2, rely=0.74)

def confirm_seller_update():
    sellers_update_menu()
    try:
        input_id = int(id_search_bar.get())
        name = seller_name_input.get()
        product_type = seller_product_type_input.get()
        extra_description = seller_description_input.get()
        return_code, return_seller_values = update_seller(input_id, name, product_type, extra_description)
        tk.Label(root, text="Seller Updated!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.85)
        if return_code == 200:
            tk.Label(root, text="Seller Updated!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.85)
        else:
            tk.Label(root, text="Seller Not Found!", font=("Impact", 25), bg="white", fg="red").place(relx=0.675, rely=0.85)
    except ValueError:
        error.place(relx=0.6,rely=0.85)

def sellers_delete_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_current.place(relx=0.0508, rely=0.09)
    items_button_normal.place(relx=0.159, rely=0.11)
    orders_button_normal.place(relx=0.227, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    delete_seller_button.place(relx=0.15,rely=0.75)
    tk.Label(root, text="ID:", font=("Impact", 25), bg="white", fg="black").place(relx=0.2, rely=0.3)
    id_search_bar.place(relx=0.25,rely=0.3, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    seller_delete_confirm.place(relx=0.6,rely=0.3, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.08)
    return_button_seller.place(relx=0.6,rely=0.74)

def confirm_seller_delete():
    sellers_delete_menu()
    try:
        seller_id = int(id_search_bar.get())
        return_code, return_id = delete_sellers(seller_id)
        if return_code == 404:
            tk.Label(root, text="Seller Not found!", font=("Impact", 25), bg="white", fg="red").place(relx=0.25,rely=0.4)
        elif return_code == 200:
            tk.Label(root, text="Seller Deleted!", font=("Impact", 25), bg="white", fg="black").place(relx=0.25,rely=0.4)
    except ValueError:
        error.place(relx=0.25,rely=0.4)

##Items##

def items_search():
    item_window_real()
    try:
        item_id = int(id_search_bar.get())
        return_code, return_item_values, return_item_quantity, item_name = read_product_by_id(item_id, name)
        if return_code == 200:
            create_item_button.place_forget()
            delete_item_button.place_forget()
            update_item_button.place_forget()
            id_search_bar.place_forget()
            search_item_button.place_forget()
            tk.Label(root, text="Id:", font=("Impact", 20), bg="white", fg="black").place(relx=0.3, rely=0.3)
            tk.Label(root, text="Name:", font=("Impact", 20), bg="white", fg="black").place(relx=0.3, rely=0.4)
            tk.Label(root, text="Price:", font=("Impact", 20), bg="white", fg="black").place(relx=0.3, rely=0.5)
            tk.Label(root, text="Quantity:", font=("Impact", 20), bg="white", fg="black").place(relx=0.3, rely=0.6)
            tk.Label(root, text="Class:", font=("Impact", 20), bg="white", fg="black").place(relx=0.3, rely=0.7)
            tk.Label(root, text=str(return_item_values["id"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.6, rely=0.3)
            tk.Label(root, text=return_item_values["name"], font=("Arial", 20), bg="white", fg="black").place(relx=0.6, rely=0.4)
            tk.Label(root, text=str(return_item_values["price"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.6, rely=0.5)
            tk.Label(root, text=str(return_item_quantity), font=("Arial", 20), bg="white", fg="black").place(relx=0.6, rely=0.6)
            tk.Label(root, text=return_item_values["class"], font=("Arial", 20), bg="white", fg="black").place(relx=0.6, rely=0.7)
            return_button_item.place(anchor="center",relx=0.5,rely=0.85)
        elif return_code==404:
            tk.Label(root, text="Items not found", font=("Arial", 15), bg="white", fg="red").place(relx=0.15, rely=0.4)
    except ValueError:
        error.place(relx=0.15,rely=0.4)

def items_create_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_current.place(relx=0.12, rely=0.09)
    orders_button_normal.place(relx=0.2285, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    tk.Label(root, text=name, font=("Impact", 25), bg="white", fg="black").place(relx=0.2, rely=0.25,anchor="center")
    create_item_button.place(relx=0.15,rely=0.41)
    tk.Label(root, text="Name:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.22)
    tk.Label(root, text="Price:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.34)
    tk.Label(root, text="Quality:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.46)
    tk.Label(root, text="Class:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.58)
    item_name_input.place(relx=0.6, rely=0.22, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_price_input.place(relx=0.6, rely=0.34, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_quantity_input.place(relx=0.6, rely=0.46, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_class_input.place(relx=0.6, rely=0.58, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_create_confirm.place(relx=0.6,rely=0.70)
    return_button_item.place(relx=0.2, rely=0.70)

def confirm_items_create():
    items_create_menu()
    if item_name_input!="" and item_price_input!="" and item_quantity_input!="" and item_class_input!="":
        try:
            item_name = item_name_input.get()
            item_price = float(item_price_input.get())
            item_quantity = int(item_quantity_input.get())
            item_class = item_class_input.get()
            return_code, return_name = create_product(item_name, item_price, item_quantity, item_class, name)
            if return_code==200:
                tk.Label(root, text="Item Created!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.80)
            else:
                tk.Label(root, text="Item Exists!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.80)
        except ValueError:
            error.place(relx=0.6,rely=0.80)
    else:
        error.place(relx=0.6, rely=0.80)

def items_update_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_current.place(relx=0.12, rely=0.09)
    orders_button_normal.place(relx=0.2285, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    tk.Label(root, text=name, font=("Impact", 25), bg="white", fg="black").place(relx=0.2, rely=0.25,anchor="center")
    update_item_button.place(relx=0.15,rely=0.41)
    tk.Label(root, text="ID:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.22)
    tk.Label(root, text="Name:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.32)
    tk.Label(root, text="Price:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.42)
    tk.Label(root, text="Quality:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.52)
    tk.Label(root, text="Class:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.62)
    id_search_bar.place(relx=0.6, rely=0.22, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_name_input.place(relx=0.6, rely=0.32, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_price_input.place(relx=0.6, rely=0.42, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_quantity_input.place(relx=0.6, rely=0.52, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_class_input.place(relx=0.6, rely=0.62, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_update_confirm.place(relx=0.6,rely=0.72)
    return_button_item.place(relx=0.2, rely=0.72)

def confirm_items_update():
    items_update_menu()
    if id_search_bar!="" and item_name_input!="" and item_price_input!="" and item_quantity_input!="" and item_class_input!="":
        try:
            item_id = int(id_search_bar.get())
            item_name = item_name_input.get()
            item_price = float(item_price_input.get())
            item_quantity = int(item_quantity_input.get())
            item_class = item_class_input.get()
            return_code, return_item_values, return_item_quantity = update_product(item_id, item_name, item_class, item_price, item_quantity, name)
            if return_code==200:
                tk.Label(root, text="Item Updated!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.80)
            else:
                tk.Label(root, text="Item dont exist!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.80)
        except ValueError:
            error.place(relx=0.6,rely=0.80)
    else:
        error.place(relx=0.6, rely=0.80)

def items_delete_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_current.place(relx=0.12, rely=0.09)
    orders_button_normal.place(relx=0.2285, rely=0.11)
    schedule_button_normal.place(relx=0.295, rely=0.11)
    tk.Label(root, text=name, font=("Impact", 20), bg="white", fg="black").place(relx=0.5, rely=0.25,anchor="center")
    delete_item_button.place(relx=0.15,rely=0.75)
    tk.Label(root, text="ID:", font=("Impact", 25), bg="white", fg="black").place(relx=0.2, rely=0.4)
    id_search_bar.place(relx=0.25,rely=0.4, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    item_delete_confirm.place(relx=0.6,rely=0.4, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.08)
    return_button_item.place(relx=0.6,rely=0.74)

def confirm_items_delete():
    items_delete_menu()
    try:
        item_id = int(id_search_bar.get())
        return_code, return_name = delete_product(item_id, name)
        if return_code == 404:
            tk.Label(root, text="Item Not found!", font=("Impact", 25), bg="white", fg="red").place(relx=0.25,rely=0.5)
        elif return_code == 200:
            tk.Label(root, text="Item Deleted!", font=("Impact", 25), bg="white", fg="black").place(relx=0.25,rely=0.5)
    except ValueError:
        error.place(relx=0.25,rely=0.5)

##Orders##

def order_search():
    order_window_real()
    return_code, return_values = read_item_order(name)
    if return_code == 200:
        order_info.insert("end","Quantity  |  Item Name  |  Price\n")
        for i in return_values["items"]:
            order_info.insert("end",f"{return_values["quantities"][i]} | {return_values["items"][i]["name"]} | {return_values["items"][i]["price"]}\n")
        order_frame.place(relx=0.4,rely=0.3,height=300)
        create_order_button.place_forget()
        delete_order_button.place_forget()
        update_order_button.place_forget()
        new_order_button.place_forget()
        return_button_order.place(anchor="center",relx=0.5,rely=0.85)
    else:
        tk.Label(root, text="No items in order", font=("Arial", 20), bg="white", fg="Red").place(relx=0.4, rely=0.325)

def order_create_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_current.place(relx=0.189, rely=0.09)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    tk.Label(root, text=name, font=("Impact", 25), bg="white", fg="black").place(relx=0.2, rely=0.25,anchor="center")
    create_order_button.place(relx=0.15,rely=0.41)
    tk.Label(root, text="Item ID:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.22)
    tk.Label(root, text="Quantity:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.34)
    id_search_bar.place(relx=0.6, rely=0.22, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    order_quantity_input.place(relx=0.6, rely=0.34, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    order_create_confirm.place(relx=0.6,rely=0.70)
    return_button_order.place(relx=0.2, rely=0.70)

def confirm_order_create():
    order_create_menu()
    try:
        item_id = int(id_search_bar.get())
        item_quantity = int(order_quantity_input.get())
        return_code, item_dict, item_quantity = create_item_order(item_id, item_quantity, name)
        if return_code==200:
            tk.Label(root, text="Item Added to order!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.80)
        else:
            tk.Label(root, text="Item Not found!", font=("Impact", 25), bg="white", fg="Red").place(relx=0.675, rely=0.80)
    except ValueError:
        error.place(relx=0.6,rely=0.80)

def order_update_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_current.place(relx=0.189, rely=0.09)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    update_order_button.place(relx=0.15, rely=0.54)
    tk.Label(root, text=name, font=("Impact", 25), bg="white", fg="black").place(relx=0.2, rely=0.25,anchor="center")
    tk.Label(root, text="Item name:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.22)
    tk.Label(root, text="Quantity:", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.34)
    order_name_input.place(relx=0.6, rely=0.22, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    order_quantity_input.place(relx=0.6, rely=0.34, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    order_update_confirm.place(relx=0.6,rely=0.70)
    return_button_order.place(relx=0.2, rely=0.70)

def confirm_order_update():
    order_update_menu()
    try:
        item_name = order_name_input.get()
        item_quantity = int(order_quantity_input.get())
        return_code, msg = update_item_order(item_name, item_quantity, name)
        if return_code==404:
            tk.Label(root, text="Item Not found!", font=("Impact", 25), bg="white", fg="Red").place(relx=0.675, rely=0.80)
        else:
            tk.Label(root, text="Item Updated in order!", font=("Impact", 25), bg="white", fg="black").place(relx=0.675, rely=0.80)
    except ValueError:
        error.place(relx=0.6,rely=0.80)

def order_delete_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_current.place(relx=0.189, rely=0.09)
    schedule_button_normal.place(relx=0.297, rely=0.11)
    tk.Label(root, text=name, font=("Impact", 20), bg="white", fg="black").place(relx=0.5, rely=0.25,anchor="center")
    delete_order_button.place(relx=0.15,rely=0.75)
    order_name_input.place(relx=0.25,rely=0.4, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.08)
    order_delete_confirm.place(relx=0.6,rely=0.4, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.08)
    return_button_order.place(relx=0.6,rely=0.74)

def confirm_order_delete():
    order_delete_menu()
    try:
        item_name=order_name_input.get()
        return_code, return_msg = delete_item_order(item_name, name)
        if return_code == 404:
            tk.Label(root, text="Item Not found!", font=("Impact", 25), bg="white", fg="red").place(relx=0.25,rely=0.5)
        elif return_code == 200:
            tk.Label(root, text="Item Removed!", font=("Impact", 25), bg="white", fg="black").place(relx=0.25,rely=0.5)
    except ValueError:
        error.place(relx=0.25,rely=0.5)

def new_order_menu():
    next_order(name)

##Schedule##

def schedule_search():
    schedule_window()
    create_schedule_button.place_forget()
    update_schedule_button.place_forget()
    delete_schedule_button.place_forget()
    sessions_frame.place_forget()
    id_search_bar.place(relx=0.35, rely=0.3, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.075)
    search_schedule_confirm.place(relx=0.7, rely=0.3)
    return_schedule_button.place(relx=0.5, rely=0.75, anchor="n")

def schedule_search_result():
    schedule_search()
    try:
        schedule_id=int(id_search_bar.get())
        return_code, schedule_dict, schedule_name = read_schedule(schedule_id)
        if return_code == 200:
            tk.Label(root, text="Id:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.45)
            tk.Label(root, text="First day:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.55)
            tk.Label(root, text="Last day:", font=("Impact", 20), bg="white", fg="black").place(relx=0.25, rely=0.65)
            tk.Label(root, text=str(schedule_dict["id"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.45)
            tk.Label(root, text=str(schedule_dict["monday"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.55)
            tk.Label(root, text=str(schedule_dict["sunday"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.5, rely=0.65)
        else:
            tk.Label(root, text="Schedule not found", font=("Impact", 20), bg="white", fg="red").place(relx=0.35, rely=0.4)
    except ValueError:
        error.place(relx=0.35,rely=0.4)

def schedule_create_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_normal.place(relx=0.189, rely=0.11)
    schedule_button_current.place(relx=0.258, rely=0.09)
    create_schedule_button.place(relx=0.11, rely=0.44)
    tk.Label(root, text="Day:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.30)
    tk.Label(root, text="Month:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.44)
    tk.Label(root, text="Year:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.58)
    schedule_day.place(relx=0.70, rely=0.3, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_month.place(relx=0.70, rely=0.44, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_year.place(relx=0.70, rely=0.58, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_create_confirm.place(relx=0.60, rely=0.72)
    return_schedule_button.place(relx=0.11, rely=0.72)

def confirm_schedule_create():
    schedule_create_menu()
    try:
        day = int(schedule_day.get())
        month = int(schedule_month.get())
        year = int(schedule_year.get())
        continue_path=False
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day <= 31:
                continue_path = True
        elif month == 2:
            if year % 4 == 0:
                if day <= 29:
                    continue_path = True
            else:
                if day <= 28:
                    continue_path = True
        else:
            if day <= 30:
                continue_path = True
        if continue_path:
            return_code, schedule_id = create_schedule(day, month, year)
            if return_code==200:
                msg="schedule created with id " + str(schedule_id)
                tk.Label(root, text=msg, font=("Impact", 25), bg="white", fg="black").place(relx=0.60, rely=0.8)
            else:
                tk.Label(root, text="Schedule already exists", font=("Impact", 25), bg="white", fg="Red").place(relx=0.60, rely=0.8)
        else:
            tk.Label(root, text="Date doesnt exist", font=("Impact", 25), bg="white", fg="Red").place(relx=0.60, rely=0.80)
    except ValueError:
        error.place(relx=0.6,rely=0.80)

def schedule_update_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_normal.place(relx=0.189, rely=0.11)
    schedule_button_current.place(relx=0.258, rely=0.09)
    update_schedule_button.place(relx=0.11, rely=0.58)
    tk.Label(root, text="ID:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.3)
    tk.Label(root, text="Day:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.405)
    tk.Label(root, text="Month:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.51)
    tk.Label(root, text="Year:", font=("Impact", 20), bg="white", fg="black").place(relx=0.60, rely=0.615)
    id_search_bar.place(relx=0.70, rely=0.3, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_day.place(relx=0.70, rely=0.405, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_month.place(relx=0.70, rely=0.51, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_year.place(relx=0.70, rely=0.615, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_update_confirm.place(relx=0.60, rely=0.72)
    return_schedule_button.place(relx=0.11, rely=0.72)

def confirm_schedule_update():
    schedule_update_menu()
    try:
        schedule_id = int(id_search_bar.get())
        day = int(schedule_day.get())
        month = int(schedule_month.get())
        year = int(schedule_year.get())
        continue_path=False
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day <= 31:
                continue_path = True
        elif month == 2:
            if year % 4 == 0:
                if day <= 29:
                    continue_path = True
            else:
                if day <= 28:
                    continue_path = True
        else:
            if day <= 30:
                continue_path = True
        if continue_path:
            return_code, schedule_id = update_schedule(day, month, year, schedule_id)
            if return_code==200:
                tk.Label(root, text="schedule updated", font=("Impact", 25), bg="white", fg="black").place(relx=0.60, rely=0.8)
            else:
                tk.Label(root, text="Schedule already exists in this week", font=("Impact", 25), bg="white", fg="Red").place(relx=0.60, rely=0.8)
        else:
            tk.Label(root, text="Date doesnt exist", font=("Impact", 25), bg="white", fg="Red").place(relx=0.60, rely=0.80)
    except ValueError:
        error.place(relx=0.6,rely=0.80)

def schedule_delete_menu():
    schedule_window()
    create_schedule_button.place_forget()
    update_schedule_button.place_forget()
    search_schedule_button.place_forget()
    sessions_frame.place_forget()
    id_search_bar.place(relx=0.35, rely=0.72, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.075)
    schedule_delete_confirm.place(relx=0.7, rely=0.72)
    return_schedule_button.place(relx=0.5, rely=0.3, anchor="n")

def confirm_schedule_delete():
    schedule_delete_menu()
    try:
        schedule_id = int(id_search_bar.get())
        return_code, schedule_id = delete_schedule(schedule_id)
        if return_code == 404:
            tk.Label(root, text="Schedule not found!", font=("Impact", 25), bg="white", fg="red").place(relx=0.4,rely=0.65)
        elif return_code == 200:
            tk.Label(root, text="Schedule deleted!", font=("Impact", 25), bg="white", fg="black").place(relx=0.4,rely=0.65)
    except ValueError:
        error.place(relx=0.4,rely=0.65)

##Sessions##

def session_search():
    sessions_window(selected_day,selected_time)
    create_session_button.place_forget()
    update_session_button.place_forget()
    delete_session_button.place_forget()
    id_search_bar.place(relx=0.35, rely=0.3, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.075)
    search_session_confirm.place(relx=0.7, rely=0.3)
    return_session_button.place(relx=0.5, rely=0.8, anchor="n")

def session_search_result():
    session_search()
    try:
        session_id=int(id_search_bar.get())
        return_code, return_session_dict = read_session(session_id)
        if return_code == 200:
            tk.Label(root, text="Id:", font=("Impact", 20), bg="white", fg="black").place(relx=0.35, rely=0.45)
            tk.Label(root, text="Schedule name:", font=("Impact", 20), bg="white", fg="black").place(relx=0.35, rely=0.52)
            tk.Label(root, text="Seller name:", font=("Impact", 20), bg="white", fg="black").place(relx=0.35, rely=0.59)
            tk.Label(root, text="Time:", font=("Impact", 20), bg="white", fg="black").place(relx=0.35, rely=0.66)
            tk.Label(root, text="Day:", font=("Impact", 20), bg="white", fg="black").place(relx=0.35, rely=0.73)
            tk.Label(root, text=str(return_session_dict["id"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.55, rely=0.45)
            tk.Label(root, text=str(return_session_dict["schedule_name"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.55, rely=0.52)
            tk.Label(root, text=str(return_session_dict["seller_name"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.55, rely=0.59)
            tk.Label(root, text=str(return_session_dict["time"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.55, rely=0.66)
            tk.Label(root, text=str(return_session_dict["day"]), font=("Arial", 20), bg="white", fg="black").place(relx=0.55, rely=0.73)
        else:
            tk.Label(root, text="Session not found", font=("Impact", 20), bg="white", fg="red").place(relx=0.35, rely=0.4)
    except ValueError:
        error.place(relx=0.35,rely=0.4)

def session_create_menu():
    for widget in root.winfo_children():
        if widget.winfo_manager() == "place":
            widget.place_forget()
    canvas.place(relx=0.5, rely=0.55, anchor="center", width=root.winfo_width() * 0.9, height=root.winfo_height() * 0.78)
    sellers_button_normal.place(relx=0.0508, rely=0.11)
    items_button_normal.place(relx=0.12, rely=0.11)
    orders_button_normal.place(relx=0.189, rely=0.11)
    schedule_button_current.place(relx=0.258, rely=0.09)
    create_session_button.place(relx=0.11, rely=0.44)
    tk.Label(root, text="Sellers ID:", font=("Impact", 20), bg="white", fg="black").place(relx=0.56, rely=0.31)
    tk.Label(root, text="Schedule ID:", font=("Impact", 20), bg="white", fg="black").place(relx=0.56, rely=0.45)
    seller_id_input.place(relx=0.70, rely=0.3, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    schedule_id_input.place(relx=0.70, rely=0.44, width=root.winfo_width() * 0.1, height=root.winfo_height() * 0.075)
    session_create_confirm.place(relx=0.60, rely=0.66)
    return_session_button.place(relx=0.11, rely=0.66)

def confirm_session_create():
    session_create_menu()
    try:
        seller_id=int(seller_id_input.get())
        schedule_id=int(schedule_id_input.get())
        return_code, schedule_dict, schedule_name = read_schedule(schedule_id)
        if return_code==200:
            return_code, session_return_dict = create_session(seller_id, schedule_name, selected_day, selected_time, schedule_dict)
            if return_code==200:
                msg = "session created with id: " + str(session_return_dict["id"])
                tk.Label(root, text=msg, font=("Impact", 25), bg="white", fg="black").place(relx=0.60, rely=0.75)
            else:
                tk.Label(root, text="Seller doesnt exists", font=("Impact", 25), bg="white", fg="Red").place(relx=0.60, rely=0.75)
        else:
            tk.Label(root, text="Schedule doesnt exists", font=("Impact", 25), bg="white", fg="Red").place(relx=0.60, rely=0.75)
    except ValueError:
        error.place(relx=0.6,rely=0.75)

def session_update_menu():
    sessions_window(selected_day,selected_time)
    create_session_button.place_forget()
    search_session_button.place_forget()
    delete_session_button.place_forget()
    id_search_bar.place(relx=0.35, rely=0.58, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.075)
    update_session_confirm.place(relx=0.7, rely=0.58)
    return_session_button.place(relx=0.5, rely=0.8, anchor="n")

def confirm_session_update():
    session_update_menu()
    try:
        session_id = int(id_search_bar.get())
        return_code, return_session_dict = read_session(session_id)
        if return_code == 200:
            return_code, return_session_dict = update_session(session_id, return_session_dict["schedule_name"], selected_day, selected_time)
            if return_code==200:
                tk.Label(root, text="schedule updated", font=("Impact", 25), bg="white", fg="black").place(relx=0.4, rely=0.7)
            else:
                tk.Label(root, text="Schedule already exists in this week", font=("Impact", 25), bg="white", fg="Red").place(relx=0.4, rely=0.7)
        else:
            tk.Label(root, text="Schedule doesnt exists", font=("Impact", 25), bg="white", fg="Red").place(relx=0.4, rely=0.7)
    except ValueError:
        error.place(relx=0.4,rely=0.7)

def session_delete_menu():
    sessions_window(selected_day,selected_time)
    create_session_button.place_forget()
    update_session_button.place_forget()
    search_session_button.place_forget()
    id_search_bar.place(relx=0.35, rely=0.72, width=root.winfo_width() * 0.3, height=root.winfo_height() * 0.075)
    delete_session_confirm.place(relx=0.7, rely=0.72)
    return_session_button.place(relx=0.5, rely=0.3, anchor="n")

def confirm_session_delete():
    session_delete_menu()
    try:
        session_id = int(id_search_bar.get())
        return_code, return_session_id = delete_session(session_id)
        if return_code == 404:
            tk.Label(root, text="Session not found!", font=("Impact", 25), bg="white", fg="red").place(relx=0.4,rely=0.65)
        elif return_code == 200:
            tk.Label(root, text="Session deleted!", font=("Impact", 25), bg="white", fg="black").place(relx=0.4,rely=0.65)
    except ValueError:
        error.place(relx=0.4,rely=0.65)

#map_buttons#

sellers_button_current = tk.Button(root, text="Sellers",width=9,height=1, bg="white", fg="gray",borderwidth=0,highlightthickness=0,command=sellers_window,font=("Arial", 20))
sellers_button_normal = tk.Button(root, text="Sellers",width=13,height=2, bg="gray", fg="white",borderwidth=0,highlightthickness=0,command=sellers_window)

items_button_current = tk.Button(root, text="Items",width=9,height=1, bg="white", fg="gray",borderwidth=0,highlightthickness=0,command=items_name_window,font=("Arial", 20))
items_button_normal = tk.Button(root, text="Items",width=13,height=2, bg="gray", fg="white",borderwidth=0,highlightthickness=0,command=items_name_window)

orders_button_current = tk.Button(root, text="Orders",width=9,height=1, bg="white", fg="gray",borderwidth=0,highlightthickness=0,command=order_name_window,font=("Arial", 20))
orders_button_normal = tk.Button(root, text="Orders",width=13,height=2, bg="gray", fg="white",borderwidth=0,highlightthickness=0,command=order_name_window)

schedule_button_current = tk.Button(root, text="Schedule",width=9,height=1, bg="white", fg="gray",borderwidth=0,highlightthickness=0,command=schedule_window,font=("Arial", 20))
schedule_button_normal = tk.Button(root, text="Schedule",width=13,height=2, bg="gray", fg="white",borderwidth=0,highlightthickness=0,command=schedule_window)

#Extra#

id_search_bar = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

error= tk.Label(root, text="Error: Fill out all forms correctly",font=("Arial", 15),bg="white",fg="red")

#sellers#

return_button_seller = tk.Button(root, text="Return",width=9,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=sellers_window,font=("Arial", 20))

seller_name_input = tk.Entry(root, font=("Arial",20),bg="#D3D3D3")

seller_product_type_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

seller_description_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

#Create sellers#

create_seller_button = tk.Button(root, text="Create seller",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=sellers_create_menu,font=("Arial", 20))

seller_create_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_seller_create,font=("Arial", 20))

#search sellers#

search_seller_button = tk.Button(root, text="Search seller",width=13,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=sellers_search,font=("Arial", 20))

#Update sellers#

update_seller_button = tk.Button(root, text="Update seller",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=sellers_update_menu,font=("Arial", 20))

seller_update_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_seller_update,font=("Arial", 20))

#Delete sellers#

delete_seller_button = tk.Button(root, text="Delete seller",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=sellers_delete_menu,font=("Arial", 20))

seller_delete_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_seller_delete,font=("Arial", 20))

#items#

item_confirm = tk.Button(root, text="Search Items",width=13,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=items_window_login,font=("Arial", 20))

item_name_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

item_price_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

item_quantity_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

item_class_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

return_button_item = tk.Button(root, text="Return",width=9,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=item_window_real,font=("Arial", 20))

#Create items#

create_item_button = tk.Button(root, text="Create Items",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=items_create_menu,font=("Arial", 20))

item_create_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_items_create,font=("Arial", 20))

#search items#

search_item_button = tk.Button(root, text="Search Items",width=13,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=items_search,font=("Arial", 20))

#Update items#

update_item_button = tk.Button(root, text="Update Items",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=items_update_menu,font=("Arial", 20))

item_update_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_items_update,font=("Arial", 20))

#Delete items#

delete_item_button = tk.Button(root, text="Delete Items",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=items_delete_menu,font=("Arial", 20))

item_delete_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_items_delete,font=("Arial", 20))

#Orders#

order_confirm = tk.Button(root, text="Search Items",width=13,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=order_window_login,font=("Arial", 20))

order_name_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

order_price_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

order_quantity_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

order_class_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

return_button_order = tk.Button(root, text="Return",width=9,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=order_window_real,font=("Arial", 20))

#Create order#

create_order_button = tk.Button(root, text="Add Items",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=order_create_menu,font=("Arial", 20))

order_create_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_order_create,font=("Arial", 20))

#search order#

search_order_button = tk.Button(root, text="Search Order",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=order_search,font=("Arial", 20))

order_frame = tk.Frame(root,bd=5,relief="solid")

order_scrollbar = tk.Scrollbar(order_frame)
order_scrollbar.pack(side="right", fill="y")

order_info = tk.Text(order_frame, yscrollcommand=order_scrollbar.set)
order_info.pack(side="left", fill="both", expand=True)

order_scrollbar.config(command=order_info.yview)

#Update order#

update_order_button = tk.Button(root, text="Update Order",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=order_update_menu,font=("Arial", 20))

order_update_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_order_update,font=("Arial", 20))

#Delete order#

delete_order_button = tk.Button(root, text="Remove item",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=order_delete_menu,font=("Arial", 20))

order_delete_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_order_delete,font=("Arial", 20))

#new order#

new_order_button = tk.Button(root, text="New order",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=new_order_menu,font=("Arial", 20))

#schedule#

schedule_day = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

schedule_month = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

schedule_year = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

return_schedule_button = tk.Button(root, text="Return",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=schedule_window,font=("Arial", 20))

#Create schedule#

create_schedule_button = tk.Button(root, text="Create Schedule",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=schedule_create_menu,font=("Arial", 20))

schedule_create_confirm = tk.Button(root, text="Confirm",width=18,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_schedule_create,font=("Arial", 20))

#search schedule#

search_schedule_button = tk.Button(root, text="Search Schedule",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=schedule_search,font=("Arial", 20))

search_schedule_confirm = tk.Button(root, text="Search",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=schedule_search_result,font=("Arial", 20))

#Update schedule#

update_schedule_button = tk.Button(root, text="Update Schedule",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=schedule_update_menu,font=("Arial", 20))

schedule_update_confirm = tk.Button(root, text="Confirm",width=25,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_schedule_update,font=("Arial", 20))

#Delete schedule#

delete_schedule_button = tk.Button(root, text="Delete schedule",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=schedule_delete_menu,font=("Arial", 20))

schedule_delete_confirm = tk.Button(root, text="Confirm",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_schedule_delete,font=("Arial", 20))

#Sessions#

return_session_button = tk.Button(root, text="Return",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=lambda: sessions_window(selected_day,selected_time),font=("Arial", 20))

sessions_frame = tk.Frame(root,bg="gray")

schedule_id_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")

seller_id_input = tk.Entry(root, font=("Arial", 20),bg="#D3D3D3")


#Create schedule#

create_session_button = tk.Button(root, text="Create Session",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=session_create_menu,font=("Arial", 20))

session_create_confirm = tk.Button(root, text="Confirm",width=18,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_session_create,font=("Arial", 20))

#search schedule#

search_session_button = tk.Button(root, text="Search Session",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=session_search,font=("Arial", 20))

search_session_confirm = tk.Button(root, text="Search",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=session_search_result,font=("Arial", 20))

#Update schedule#

update_session_button = tk.Button(root, text="Update Session",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=session_update_menu,font=("Arial", 20))

update_session_confirm = tk.Button(root, text="Confirm",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_session_update,font=("Arial", 20))

#Delete schedule#

delete_session_button = tk.Button(root, text="Delete Session",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=session_delete_menu,font=("Arial", 20))

delete_session_confirm = tk.Button(root, text="Confirm",width=17,height=1, bg="gray", fg="black",borderwidth=0,highlightthickness=0,command=confirm_session_delete,font=("Arial", 20))

#program#

sellers_window()

root.mainloop()