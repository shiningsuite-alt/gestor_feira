import json

def load_state(save_file_name,default_state):
    if save_file_name.exists():
        with open(save_file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    return default_state.copy()

def save_state(estado,save_file_name):
    with open(save_file_name, "w", encoding="utf-8") as f:
        json.dump(estado, f, indent=4)

def pause():
    wait=input("Press enter to continue...")

def validation_check():
    while True:
        try:
            choice = int(input("Choice: "))
            break
        except ValueError:
            print("Write a number")
    return choice

def validation_check_float():
    while True:
        try:
            choice = float(input("Choice: "))
            break
        except ValueError:
            print("Write a decimal")
    return choice

def validation_check_2(x):
    while True:
        try:
            choice = int(input("Choice: "))
            while choice>x:
                try:
                    choice = int(input("Make a choice that is in range: "))
                except ValueError:
                    print("Write a number")
            break
        except ValueError:
            print("Write a number")
    return choice

def validation_check_3(x,y):
    while True:
        try:
            choice = int(input("Choice: "))
            while y<choice or choice<x:
                try:
                    choice = int(input("Make a choice that is in range: "))
                except ValueError:
                    print("Write a number")
            break
        except ValueError:
            print("Write a number")
    return choice

def list_to_tuple(x_dict):
    for i in x_dict.keys():
        x_dict[i]=tuple(x_dict[i])

def list_to_set(x_dict):
    x_dict=set(x_dict)
