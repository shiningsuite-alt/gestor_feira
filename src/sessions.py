import json
import os
import copy
from datetime import datetime,timedelta,date
from logger import get_logger
import general_functions
from schedule import schedules
from sellers import sellers, read_sellers

log = get_logger("sessions")

SESSIONS_FILE="saves/sessions.json"

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

def json_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    else:
        return obj

def json_deserializer(obj):
    if obj.get("__type__") == "datetime":
        return datetime.fromisoformat(obj["value"])
    else:
        return obj

def save_sessions():
    with open(SESSIONS_FILE, "w", encoding="utf-8") as ficheiro:
        log.debug("Ficha de horarios aberto '%s'.", SESSIONS_FILE)
        json.dump(sessions_dict, ficheiro, indent=4,default=json_serializer)
    log.debug("Horarios guardados em '%s'.", SESSIONS_FILE)

def load_sessions():
    global sessions_dict
    if os.path.exists(SESSIONS_FILE):
        log.debug("Ficha de horarios encontrado '%s'.", SESSIONS_FILE)
        with open(SESSIONS_FILE, "r", encoding="utf-8") as ficheiro:
            log.debug("Ficha de horarios aberto '%s'.", SESSIONS_FILE)
            sessions_dict = json.load(ficheiro,object_hook=json_deserializer)
        log.debug("Ficha de horarios Carregado '%s'.", SESSIONS_FILE)
    else:
        log.debug("Ficha de horarios não encontrado, sistema vai usar dicionario vazia '%s'.", SESSIONS_FILE)
        schedules = {}

sessions_dict={}

def create_session(sellers_id,schedule_name,day_select,time_select,schedule_dict):
    log.info("Criação de sessão'%s'.", sellers_id)
    load_sessions()
    if schedule_name not in sessions_dict:
        sessions_dict[schedule_name] = copy.deepcopy(default_session_dict)
        for d in list_of_days:
            sessions_dict[schedule_name][d + "_date"] = schedule_dict[d]
        log.debug("Horario de semana atualizado'%s'.", schedule_name)
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    if isinstance(sessions_dict[schedule_name][day][time], int):
        sessions_dict[schedule_name][day][time] = {}
    if len(sessions_dict[schedule_name][day][time])<20:
        return_code, sellers_dict, seller_name=read_sellers(sellers_id)
        if seller_name!="":
            session_name=seller_name+"/"+schedule_name
            session_id = sum(
                1
                for n in sessions_dict
                for d in sessions_dict[n]
                for t in sessions_dict[n][d]
                if isinstance(sessions_dict[n][d][t], dict)
                for s in sessions_dict[n][d][t]
                if isinstance(sessions_dict[n][d][t][s], dict)
            ) + 1
            sessions_dict[schedule_name][day][time][session_name]={}
            sessions_dict[schedule_name][day][time][session_name]["id"]=session_id
            log.debug("ID da sessão definido:'%s'.", session_id)
            sessions_dict[schedule_name][day][time][session_name]["schedule_name"]=schedule_name
            log.debug("ID da sessão definido:'%s'.", session_id)
            sessions_dict[schedule_name][day][time][session_name]["seller_name"]=seller_name
            log.debug("Nome da sessão definido:'%s'.", seller_name)
            sessions_dict[schedule_name][day][time][session_name]["time"]=time
            log.debug("Tempo da sessão definido:'%s'.", time)
            sessions_dict[schedule_name][day][time][session_name]["day"]=day
            log.debug("Dia da sessão definido:'%s'.", day)
            save_sessions()
            log.info("Sessão criado com sucesso'%s'.", session_id)
            return 200, sessions_dict[schedule_name][day][time][session_name]
        else:
            log.error("Vendedor não encontrado:'%s'.", sellers_id)
            return 404, "seller not found"
    else:
        save_sessions()
        log.error("Não ten espaço nesse tempo para sessão'%s'.", sellers_id)
        return 403, "failure"

def read_session(session_id):
    log.info("Pesquisa de sessão'%s'.", session_id)
    found_session = False
    load_sessions()
    log.debug("Pesquisa de sessão iniciado'%s'.", session_id)
    for schedule_name in sessions_dict:
        for days_count in sessions_dict[schedule_name]:
            if not isinstance(sessions_dict[schedule_name][days_count], dict):
                continue
            for times_count in sessions_dict[schedule_name][days_count]:
                if not isinstance(sessions_dict[schedule_name][days_count][times_count], dict):
                    continue
                for sessions_name in sessions_dict[schedule_name][days_count][times_count]:
                    session_obj = sessions_dict[schedule_name][days_count][times_count][sessions_name]
                    if isinstance(session_obj, dict) and session_obj.get("id") == session_id:
                        found_session = True
                        name = sessions_name
                        log.debug("Sessão encontrado com sucesso'%s'.", session_id)
                        break
                if found_session:
                    break
            if found_session:
                break
        if found_session:
            break
    if found_session:
        log.info("Sessão encontrado com sucesso'%s'.", session_id)
        return 200, sessions_dict[schedule_name][days_count][times_count][name]
    else:
        log.error("Sessão não foi encontrado'%s'.", session_id)
        return 404, "failure"

def update_session(session_id,schedule_name_input,day_select,time_select):
    log.info("Atualização de sessão'%s'.", session_id)
    load_sessions()
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    found_session = False
    log.debug("Pesquisa de sessão iniciado'%s'.", session_id)
    for schedule_name in sessions_dict:
        for days_count in sessions_dict[schedule_name]:
            if not isinstance(sessions_dict[schedule_name][days_count], dict):
                continue
            for times_count in sessions_dict[schedule_name][days_count]:
                if not isinstance(sessions_dict[schedule_name][days_count][times_count], dict):
                    continue
                for sessions_name in sessions_dict[schedule_name][days_count][times_count]:
                    session_obj = sessions_dict[schedule_name][days_count][times_count][sessions_name]
                    if isinstance(session_obj, dict) and session_obj.get("id") == session_id:
                        session_name = sessions_name
                        old_day = days_count
                        old_time = times_count
                        found_session = True
                        log.debug("Sessão encontrado com sucesso'%s'.", session_id)
                        break
                if found_session:
                    break
            if found_session:
                break
        if found_session:
            break
    if found_session:
        target_schedule = schedule_name_input
        if len(sessions_dict[schedule_name][day][time])<20:
            sessions_dict[schedule_name][day][time][session_name]=sessions_dict[schedule_name][old_day][old_time][session_name]
            del sessions_dict[schedule_name][old_day][old_time][session_name]
            log.info("Sessão nome atualizado'%s'.", session_name)
            sessions_dict[schedule_name][day][time][session_name]["time"]=time
            log.info("Sessão tempo atualizado'%s'.", time)
            sessions_dict[schedule_name][day][time][session_name]["day"]=day
            log.info("Sessão dia atualizado'%s'.", day)
            save_sessions()
            log.info("Sessão atualizado com sucesso'%s'.", session_id)
            return 200,sessions_dict[schedule_name][day][time][session_name]
        else:
            log.error("Sessão não atualizado, não pode ser mais sessões nesse tempo'%s'.", session_id)
            return 403, "failure"
    else:
        log.error("Sessão não encontrado'%s'.", session_id)
        return 404, "failure"

def delete_session(session_id):
    log.info("Removir sessão'%s'.", session_id)
    load_sessions()
    found_session = False
    log.debug("Pesquisa de sessão iniciado'%s'.", session_id)
    for schedule_name in sessions_dict:
        for days_count in sessions_dict[schedule_name]:
            if not isinstance(sessions_dict[schedule_name][days_count], dict):
                continue
            for times_count in sessions_dict[schedule_name][days_count]:
                if not isinstance(sessions_dict[schedule_name][days_count][times_count], dict):
                    continue
                for sessions_name in sessions_dict[schedule_name][days_count][times_count]:
                    session_obj = sessions_dict[schedule_name][days_count][times_count][sessions_name]
                    if isinstance(session_obj, dict) and session_obj.get("id") == session_id:
                        found_session=True
                        del sessions_dict[schedule_name][days_count][times_count][sessions_name]
                        log.debug("Sessão encontrado e apagado com sucesso'%s'.", session_id)
                        break
                if found_session:
                    break
            if found_session:
                break
        if found_session:
            break
    if found_session:
        log.info("Sessão apagado com sucesso'%s'.", session_id)
        save_sessions()
        return 200, session_id
    else:
        log.error("Sessão não foi encontrado'%s'.", session_id)
        return 404, "failure"