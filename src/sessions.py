import json
import os
from datetime import datetime,timedelta,date
from logger import get_logger
import general_functions
from schedule import schedules
from sellers import sellers

log = get_logger("sessions")

SESSIONS_FILE="sessions.json"

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
    with open(SESSIONS_FILE, "w", encoding="utf-8") as ficheiro:
        log.debug("Ficheiro de ficha sessão aberto '%s'.", SESSIONS_FILE)
        json.dump(sellers, ficheiro, indent=4, ensure_ascii=False)
    log.debug("Sessões guardados em '%s'.", SESSIONS_FILE)

def load_sellers():
    global sessions_dict
    if os.path.exists(SESSIONS_FILE):
        log.debug("Ficheiro de ficha encontrado '%s'.", SESSIONS_FILE)
        with open(SESSIONS_FILE, "r", encoding="utf-8") as ficheiro:
            log.debug("Ficheiro de ficha sessão aberto '%s'.", SESSIONS_FILE)
            sessions_dict = json.load(ficheiro)
        log.debug("Sessões carregado em '%s'.", SESSIONS_FILE)
    else:
        sessions_dict = {}
        log.debug("Ficheiro de ficha não encontrado, sistema vai usar dicionario vazio '%s'.", SESSIONS_FILE)

sessions_dict={}

def create_session(sellers_id,schedule_name,day_select,time_select):
    log.info("Criação de sessão'%s'.", sellers_id)
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
        log.debug("Horario de semana atualizado'%s'.", schedule_name)
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    if len(sessions_dict[schedule_name][day][time])<20:
        continue_path=False
        log.debug("Pesquisa de vendedor'%s'.", sellers_id)
        for i in sellers:
            if sellers[i]["ID"] == sellers_id:
                seller_name=i
                continue_path=True
                log.debug("Vendedor encontrado'%s'.", sellers_id)
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
            log.debug("ID da sessão definido:'%s'.", session_id)
            sessions_dict[schedule_name][day][time][session_name]["schedule_name"]=schedule_name
            log.debug("ID da sessão definido:'%s'.", session_id)
            sessions_dict[schedule_name][day][time][session_name]["seller_name"]=seller_name
            log.debug("Nome da sessão definido:'%s'.", seller_name)
            sessions_dict[schedule_name][day][time][session_name]["time"]=time
            log.debug("Tempo da sessão definido:'%s'.", time)
            sessions_dict[schedule_name][day][time][session_name]["day"]=day
            log.debug("Dia da sessão definido:'%s'.", day)
            save_sellers()
            log.info("Sessão criado com sucesso'%s'.", session_id)
            return 200, sessions_dict[schedule_name][day][time][session_name]
        else:
            save_sellers()
            log.error("Vendedor não encontrado:'%s'.", sellers_id)
            return 404, "seller not found"
    else:
        save_sellers()
        log.error("Não ten espaço nesse tempo para sessão'%s'.", sellers_id)
        return 403, "failure"

def read_session(session_id):
    log.info("Pesquisa de sessão'%s'.", session_id)
    found_session = False
    log.debug("Pesquisa de sessão iniciado'%s'.", session_id)
    for schedule_name in sessions_dict:
        for days_count in sessions_dict[schedule_name]:
            if isinstance(sessions_dict[schedule_name][days_count],dict):
                for times_count in sessions_dict[schedule_name][days_count]:
                    for sessions_name in sessions_dict[schedule_name][days_count][times_count]:
                        if session_id==sessions_dict[schedule_name][days_count][times_count][sessions_name]["id"]:
                            found_session=True
                            name=sessions_name
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

def update_session(session_id,schedule_name,day_select,time_select):
    log.info("Atualização de sessão'%s'.", session_id)
    load_sellers()
    day = list_of_days[day_select - 1]
    time = list_of_time[time_select - 1]
    found_session = False
    log.debug("Pesquisa de sessão iniciado'%s'.", session_id)
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
                                log.debug("Sessão encontrado com sucesso'%s'.", session_id)
    if found_session:
        if len(sessions_dict[day][time])<20:
            sessions_dict[schedule_name][day][time][session_name]=sessions_dict[schedule_name][old_day][old_time][session_name]
            del sessions_dict[schedule_name][old_day][old_time][session_name]
            log.info("Sessão nome atualizado'%s'.", session_name)
            sessions_dict[schedule_name][day][time][session_name]["time"]=time
            log.info("Sessão tempo atualizado'%s'.", time)
            sessions_dict[schedule_name][day][time][session_name]["day"]=day
            log.info("Sessão dia atualizado'%s'.", day)
            save_sellers()
            log.info("Sessão atualizado com sucesso'%s'.", session_id)
            return 200,sessions_dict[schedule_name][day][time][session_name]
        else:
            save_sellers()
            log.error("Sessão não atualizado, não pode ser mais sessões nesse tempo'%s'.", session_id)
            return 403, "failure"
    else:
        log.error("Sessão não encontrado'.", session_id)
        save_sellers()
        return 404, "failure"

def delete_session(session_id):
    log.info("Removir sessão'%s'.", session_id)
    load_sellers()
    found_session = False
    log.debug("Pesquisa de sessão iniciado'%s'.", session_id)
    for schedules_count in sessions_dict:
        for days_count in sessions_dict[schedules_count]:
            if sessions_dict[schedules_count][days_count]=={}:
                for times_count in sessions_dict[schedules_count][days_count]:
                    for sessions_name in sessions_dict[schedules_count][days_count][times_count]:
                        if session_id==sessions_dict[schedules_count][days_count][times_count][sessions_name]["id"]:
                            del sessions_dict[schedules_count][days_count][times_count][sessions_name]
                            found_session=True
                            log.debug("Sessão apagado com sucesso'%s'.", session_id)
    save_sellers()
    if found_session:
        log.info("Sessão apagado com sucesso'%s'.", session_id)
        return 200, session_id
    else:
        log.error("Sessão não foi encontrado'%s'.", session_id)
        return 404, "failure"