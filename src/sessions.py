import general_functions
import os
import json
from schedule import schedules
from sellers import sellers
from datetime import datetime,timedelta
sessions_file="sessions.json"

list_of_days=[
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]
list_of_time=[
    "8:00-9:00",
    "9:00-10:00",
    "10:00-11:00",
    "11:00-12:00",
    "12:00-13:00",
    "13:00-14:00",
    "14:00-15:00",
    "15:00-16:00",
    "16:00-17:00",
    "17:00-18:00"
]
default_session_dict={
    "monday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    },
    "tuesday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    },
    "wednesday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    },
    "thursday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    },
    "friday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    },
    "saturday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    },
    "sunday":{
        "8:00-9:00":{},
        "9:00-10:00":{},
        "10:00-11:00":{},
        "11:00-12:00":{},
        "12:00-13:00":{},
        "13:00-14:00":{},
        "14:00-15:00":{},
        "15:00-16:00":{},
        "16:00-17:00":{},
        "17:00-18:00":{}
    }
}


def save_sellers():
    with open(sessions_file, "w", encoding="utf-8") as ficheiro:
        json.dump(sellers, ficheiro, indent=4, ensure_ascii=False)

def load_sellers():
    global sessions_dict
    if os.path.exists(sessions_file):
        with open(sessions_file, "r", encoding="utf-8") as ficheiro:
            sessions_dict = json.load(ficheiro)
    else:
        sessions_dict = {}

sessions_dict={}

def create_session(sellers_id,schedule_name,day_select,time_select):
    load_sellers()
    if schedule_name not in sessions_dict:
        sessions_dict[schedule_name]=default_session_dict
        sessions_dict[schedule_name]["monday_date"]=schedules[schedule_name]["monday"]
        sessions_dict[schedule_name]["tuesday_date"]=schedules[schedule_name]["tuesday"]
        sessions_dict[schedule_name]["wednesday_date"]=schedules[schedule_name]["wednesday"]
        sessions_dict[schedule_name]["thursday_date"]=schedules[schedule_name]["thursday"]
        sessions_dict[schedule_name]["friday_date"]=schedules[schedule_name]["friday"]
        sessions_dict[schedule_name]["saturday_date"]=schedules[schedule_name]["saturday"]
        sessions_dict[schedule_name]["sunday_date"]=schedules[schedule_name]["sunday"]
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    if len(sessions_dict[schedule_name][day][time])<20:
        continue_path=False
        for i in sellers:
            if sellers[i]["ID"] == sellers_id:
                seller_name=i
                continue_path=True
            else:
                continue_path=False
        if continue_path:
            session_name=seller_name+"/"+schedule_name
            session_id=1
            for schedules_count in sessions_dict:
                for days_count in sessions_dict[schedules_count]:
                    if days_count=={}:
                        for times_count in sessions_dict[schedules_count][days_count]:
                            for sessions_count in sessions_dict[schedules_count][days_count][times_count]:
                                if "id" in sessions_dict[schedules_count][days_count][times_count][sessions_count]:
                                    session_id+=1
            sessions_dict[schedule_name][day][time][session_name]={}
            sessions_dict[schedule_name][day][time][session_name]["id"]=session_id
            sessions_dict[schedule_name][day][time][session_name]["schedule_name"]=schedule_name
            sessions_dict[schedule_name][day][time][session_name]["seller_name"]=seller_name
            sessions_dict[schedule_name][day][time][session_name]["time"]=time
            sessions_dict[schedule_name][day][time][session_name]["day"]=day
            save_sellers()
            return 200, sessions_dict[schedule_name][day][time][session_name]
        else:
            return 404, "seller not found"
    else:
        return 403, "failure"

def read_session(session_id):
    load_sellers()
    found_session = False
    for schedule_name in sessions_dict:
        for days_count in sessions_dict[schedule_name]:
            if isinstance(sessions_dict[schedule_name][days_count],dict):
                for times_count in sessions_dict[schedule_name][days_count]:
                    for sessions_name in sessions_dict[schedule_name][days_count][times_count]:
                        if session_id==sessions_dict[schedule_name][days_count][times_count][sessions_name]["id"]:
                            found_session=True
                            name=sessions_name
                            break
                    if found_session:
                        break
                if found_session:
                    break
        if found_session:
            break
    if found_session:
        return 200, sessions_dict[schedule_name][days_count][times_count][name]
    else:
        return 404, "failure"

def update_session(session_id,schedule_name,day_select,time_select):
    load_sellers()
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    found_session = False
    for schedules_count in sessions_dict:
        for days_count in sessions_dict[schedules_count]:
            if sessions_dict[schedules_count][days_count]=={}:
                for times_count in sessions_dict[schedules_count][days_count]:
                    for sessions_name in sessions_dict[schedules_count][days_count][times_count]:
                        if "id" in sessions_dict[schedules_count][days_count][times_count][sessions_name]:
                            if session_id==sessions_dict[schedules_count][days_count][times_count][sessions_name]["id"]:
                                session_name=sessions_name
                                old_day=days_count
                                old_time=times_count
                                found_session=True
    if found_session:
        if len(sessions_dict[day][time])<20:
            sessions_dict[schedule_name][day][time][session_name]=sessions_dict[schedule_name][old_day][old_time][session_name]
            del sessions_dict[schedule_name][old_day][old_time][session_name]
            sessions_dict[schedule_name][day][time][session_name]["time"]=time
            sessions_dict[schedule_name][day][time][session_name]["day"]=day
            save_sellers()
            return 200,sessions_dict[schedule_name][day][time][session_name]
        else:
            return 403, "failure"
    else:
        return 404, "failure"

def delete_session(session_id):
    load_sellers()
    found_session = False
    for schedules_count in sessions_dict:
        for days_count in sessions_dict[schedules_count]:
            if sessions_dict[schedules_count][days_count]=={}:
                for times_count in sessions_dict[schedules_count][days_count]:
                    for sessions_name in sessions_dict[schedules_count][days_count][times_count]:
                        if session_id==sessions_dict[schedules_count][days_count][times_count][sessions_name]["id"]:
                            del sessions_dict[schedules_count][days_count][times_count][sessions_name]
                            found_session=True
    if found_session:
        save_sellers()
        return 200, session_id
    else:
        return 404, "failure"