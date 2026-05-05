import general_functions
from schedule import schedules
from sellers import sellers
from datetime import datetime,timedelta

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
        "8:00":{},
        "9:00":{},
        "10:00":{},
        "11:00":{},
        "12:00":{},
        "13:00":{},
        "14:00":{},
        "15:00":{},
        "16:00":{},
        "17:00":{},
        "18:00":{}
    },
    "tuesday":{
        "8:00":{},
        "9:00":{},
        "10:00":{},
        "11:00":{},
        "12:00":{},
        "13:00":{},
        "14:00":{},
        "15:00":{},
        "16:00":{},
        "17:00":{},
        "18:00":{}
    },
    "wednesday":{
        "8:00":{},
        "9:00":{},
        "10:00":{},
        "11:00":{},
        "12:00":{},
        "13:00":{},
        "14:00":{},
        "15:00":{},
        "16:00":{},
        "17:00":{},
        "18:00":{}
    },
    "thursday":{
        "8:00":{},
        "9:00":{},
        "10:00":{},
        "11:00":{},
        "12:00":{},
        "13:00":{},
        "14:00":{},
        "15:00":{},
        "16:00":{},
        "17:00":{},
        "18:00":{}
    },
    "friday":{
        "8:00":{},
        "9:00":{},
        "10:00":{},
        "11:00":{},
        "12:00":{},
        "13:00":{},
        "14:00":{},
        "15:00":{},
        "16:00":{},
        "17:00":{},
        "18:00":{}
    },
    "saturday": {
        "8:00": {},
        "9:00": {},
        "10:00": {},
        "11:00": {},
        "12:00": {},
        "13:00": {},
        "14:00": {},
        "15:00": {},
        "16:00": {},
        "17:00": {},
        "18:00": {}
    },
    "sunday": {
        "8:00": {},
        "9:00": {},
        "10:00": {},
        "11:00": {},
        "12:00": {},
        "13:00": {},
        "14:00": {},
        "15:00": {},
        "16:00": {},
        "17:00": {},
        "18:00": {}
    },
    "monday_date":datetime(0000,1,1),
    "tuesday_date":datetime(0000,1,2),
    "wednesday_date":datetime(0000,1,3),
    "thursday_date":datetime(0000,1,4),
    "friday_date":datetime(0000,1,5),
}

sessions_dict={}

def create_session(sellers_id,schedule_name,day_select,time_select):
    if schedule_name not in sessions_dict:
        sessions_dict[schedule_name]=default_session_dict
        sessions_dict[schedule_name]["monday"]=schedules[schedule_name]["monday"]
        sessions_dict[schedule_name]["tuesday"]=schedules[schedule_name]["tuesday"]
        sessions_dict[schedule_name]["wednesday"]=schedules[schedule_name]["wednesday"]
        sessions_dict[schedule_name]["thursday"]=schedules[schedule_name]["thursday"]
        sessions_dict[schedule_name]["friday"]=schedules[schedule_name]["friday"]
        sessions_dict[schedule_name]["saturday"]=schedules[schedule_name]["saturday"]
        sessions_dict[schedule_name]["sunday"]=schedules[schedule_name]["sunday"]
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    if len(sessions_dict[day][time])<20:
        for i in sellers:
            if "id" in sellers[i]:
                if sellers[i]["id"] == sellers_id:
                    seller_name=i
        session_name=seller_name+"/"+schedule_name
        session_id=0
        for schedules_count in sessions_dict:
            for days_count in sessions_dict[schedules_count]:
                for times_count in sessions_dict[schedules_count][days_count]:
                    for sessions_count in sessions_dict[schedules_count][days_count][times_count]:
                        if "id" in sessions_dict[schedules_count][days_count][times_count][sessions_count]:
                            session_id+=1
        sessions_dict[schedule_name][day][time][session_name]={}
        sessions_dict[schedule_name][day][time][session_name]["schedule_name"]=schedule_name
        sessions_dict[schedule_name][day][time][session_name]["seller_name"]=seller_name
        sessions_dict[schedule_name][day][time][session_name]["time"]=time
        sessions_dict[schedule_name][day][time][session_name]["day"]=day
        sessions_dict[schedule_name][day][time][session_name]["id"]=session_id
        return 200, "success", sellers_id, sessions_dict, day, time
    else:
        return 403, "failure", sellers_id, sessions_dict, day, time

def read_session(session_id):
    found_session = False
    for schedules_count in sessions_dict:
        for days_count in sessions_dict[schedules_count]:
            for times_count in sessions_dict[schedules_count][days_count]:
                for sessions_name in sessions_dict[schedules_count][days_count][times_count]:
                    if "id" in sessions_dict[schedules_count][days_count][times_count][sessions_name]:
                        if session_id==sessions_dict[schedules_count][days_count][times_count][sessions_name]["id"]:
                            found_session=True
    if found_session:
        return 200, sessions_dict[schedules_count][days_count][times_count][sessions_name]
    else:
        return 404, "failure"

def update_session(session_id,schedule_name,day_select,time_select):
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    found_session = False
    for schedules_count in sessions_dict:
        for days_count in sessions_dict[schedules_count]:
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
            return 200, "success", sessions_dict[schedule_name][day][time][session_name], day, time
        else:
            return 403, "failure", sessions_dict, day, time
    else:
        return 404, "failure", sessions_dict, day, time

def delete_session(session_id):
    found_session=False
    for schedules_count in sessions_dict:
        for days_count in sessions_dict[schedules_count]:
            for times_count in sessions_dict[schedules_count][days_count]:
                for sessions_name in sessions_dict[schedules_count][days_count][times_count]:
                    if "id" in sessions_dict[schedules_count][days_count][times_count][sessions_name]:
                        if session_id==sessions_dict[schedules_count][days_count][times_count][sessions_name]["id"]:
                            del sessions_dict[schedules_count][days_count][times_count][sessions_name]
                            found_session=True
    if found_session:
        return 200, sessions_dict[schedules_count][days_count][times_count][sessions_name][""]
    else:
        return 404, "failure"