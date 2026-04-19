import general_functions
from tabulate import tabulate

schedule={
    "headers": [
        "Time",
        "1 - Monday",
        "2 - Tuesday",
        "3 - Wednesday",
        "4 - Thursday",
        "5 - Friday"
    ],
    "headers_2": [
        "Id",
        "Name",
        "Product type",
        "Time",
        "Day",
        "Description"
    ],
    "list_of_days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ],
    "list_of_time": [
        "8:00",
        "9:05",
        "10:15",
        "11:25",
        "12:35",
        "13:45",
        "14:50",
        "16:00",
        "17:10"
    ],
    "Monday": {
        "8:00": {},
        "9:05": {},
        "10:15": {},
        "11:25": {},
        "12:35": {},
        "13:45": {},
        "14:50": {},
        "16:00": {},
        "17:10": {}
    },
    "Tuesday": {
        "8:00": {},
        "9:05": {},
        "10:15": {},
        "11:25": {},
        "12:35": {},
        "13:45": {},
        "14:50": {},
        "16:00": {},
        "17:10": {}
    },
    "Wednesday": {
        "8:00": {},
        "9:05": {},
        "10:15": {},
        "11:25": {},
        "12:35": {},
        "13:45": {},
        "14:50": {},
        "16:00": {},
        "17:10": {}
    },
    "Thursday": {
        "8:00": {},
        "9:05": {},
        "10:15": {},
        "11:25": {},
        "12:35": {},
        "13:45": {},
        "14:50": {},
        "16:00": {},
        "17:10": {}
    },
    "Friday": {
        "8:00": {},
        "9:05": {},
        "10:15": {},
        "11:25": {},
        "12:35": {},
        "13:45": {},
        "14:50": {},
        "16:00": {},
        "17:10": {}
    },
    "listed_names": [
    ],
    "print": [
    ]
}

def create_seller(name, product_type,extra_description,day,time):
    schedule[day][time][name]={}
    counter = 1
    if name not in schedule["listed_names"]:
        schedule["listed_names"].append(name)
    counter=1
    for i in schedule["list_of_days"]:
        for j in schedule["list_of_time"]:
            for k in schedule[i][j]:
                if "ID" in schedule[i][j][k]:
                    if counter==schedule[i][j][k]["ID"]:
                        counter+=1
    schedule[day][time][name]["ID"] = counter
    schedule[day][time][name]["name"] = name
    schedule[day][time][name]["product_type"] = product_type
    schedule[day][time][name]["time"]=time
    schedule[day][time][name]["day"]=day
    if extra_description == "" or extra_description == " ":
        schedule[day][time][name]["extra_description"]="none"
    else:
        schedule[day][time][name]["extra_description"]=extra_description
    return 200, "success"

def read_sellers(seller_id):
    temp_list = []
    for day in schedule["list_of_days"]:
        for time in schedule["list_of_time"]:
            for name in schedule["listed_names"]:
                if name in schedule[day][time]:
                    if schedule[day][time][name]["ID"] == seller_id:
                        temp_list.append(list(schedule[day][time][name].values()))
    if temp_list:
        print(tabulate(temp_list, headers=schedule["headers_2"], tablefmt="grid"))
        return 200, "success"
    else:
        return 404, "not found"

def update_seller(seller_id,new_name, product_type,extra_description,new_day,new_time):
    found=False
    for i in schedule["list_of_days"]:
        for j in schedule["list_of_time"]:
            for k in schedule[i][j]:
                if schedule[i][j][k]["ID"]==seller_id:
                    name=k
                    day=i
                    time=j
                    found=True
    if found:
        if new_name not in schedule["listed_names"]:
            schedule["listed_names"].append(new_name)
        if schedule[day][time][name]["name"] != new_name:
            schedule[day][time][new_name]=schedule[day][time][name]
            del schedule[day][time][name]
            name=new_name
            schedule[day][time][name]["name"] = new_name
        if schedule[day][time][name]["product_type"] != product_type:
            schedule[day][time][name]["product_type"] = product_type
        if schedule[day][time][name]["time"] != new_time:
            schedule[day][time][name]["time"]=new_time
        if schedule[day][time][name]["day"] != new_day:
            schedule[day][time][name]["day"]=new_day
        if extra_description == "" or extra_description == " ":
            schedule[day][time][name]["extra_description"]="none"
        else:
            schedule[day][time][name]["extra_description"]=extra_description
        return 200, "success"
    else:
        return 404, "not found"

def delete_sellers(id_select):
    for i in schedule["list_of_days"]:
        for j in schedule["list_of_time"]:
            for k in schedule[i][j]:
                if schedule[i][j][k]["ID"] == id_select:
                    del schedule[i][j][k]
                    found_id = True
                    break
                else:
                    found_id = False
    if not found_id:
        return 404, "not found"
    else:
        return 200, "success"
