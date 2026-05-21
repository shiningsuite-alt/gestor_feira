from datetime import datetime,timedelta
import json
import os
from datetime import date
from logger import get_logger
import general_functions

log = get_logger("schedule")

schedules_file="schedules.json"

schedule_default={
    "id":0,
    "monday":datetime(2000,1,1),
    "tuesday":datetime(2000,1,2),
    "wednesday": datetime(2000, 1, 3),
    "thursday": datetime(2000, 1, 4),
    "friday": datetime(2000, 1, 5),
    "saturday": datetime(2000, 1, 6),
    "sunday": datetime(2000, 1, 7),
}

def save_schedule():
    with open(schedules_file, "w", encoding="utf-8") as ficheiro:
        log.debug("Ficha de horarios aberto '%s'.", schedules_file)
        json.dump(schedules, ficheiro, indent=4, ensure_ascii=False)
    log.debug("Horarios guardados em '%s'.", schedules_file)

def load_schedule():
    global schedules
    if os.path.exists(schedules_file):
        log.debug("Ficha de horarios encontrado '%s'.", schedules_file)
        with open(schedules_file, "r", encoding="utf-8") as ficheiro:
            log.debug("Ficha de horarios aberto '%s'.", schedules_file)
            schedules = json.load(ficheiro)
        log.debug("Ficha de horarios Carregado '%s'.", schedules_file)
    else:
        log.debug("Ficha de horarios não encontrado, sistema vai usar dicionario vazia '%s'.", schedules_file)
        schedules = {}

schedules={}

def create_schedule(day,month,year):
    log.info("Criar horarios '%s'.", schedules_file)
    load_schedule()
    big_break=True
    continue_path=True
    date = datetime(year,month,day)
    log.debug("Check se existe um horario nesse semana iniciado '%s'.", date)
    for i in schedules:
        for j in schedules[i]:
            if type(schedules[i][j]) is datetime:
                if schedules[i][j]==date:
                    continue_path=False
                    big_break=True
                    log.debug("Já existe um horario nesse semana:'%s'.", date)
                    break
                else:
                    continue_path=True
        if big_break:
            break
    if continue_path:
        id_counter=1
        for i in schedules:
            if schedules[i]["id"]==id_counter:
                id_counter+=1
        schedule_name="schedule"+str(id_counter)
        schedules[schedule_name]={}
        log.debug("nome de horario definido '%s'.", schedule_name)
        schedules[schedule_name]["id"]=id_counter
        log.debug("Id de horario definido '%s'.", id_counter)
        week_day = date.weekday()
        if week_day == 0:
            schedules[schedule_name]["monday"]=date
            schedules[schedule_name]["tuesday"]=date+timedelta(days=1)
            schedules[schedule_name]["wednesday"]=date+timedelta(days=2)
            schedules[schedule_name]["thursday"]=date+timedelta(days=3)
            schedules[schedule_name]["friday"]=date+timedelta(days=4)
            schedules[schedule_name]["saturday"]=date+timedelta(days=5)
            schedules[schedule_name]["sunday"]=date+timedelta(days=6)
        elif week_day == 1:
            schedules[schedule_name]["monday"]=date+timedelta(days=-1)
            schedules[schedule_name]["tuesday"]=date
            schedules[schedule_name]["wednesday"]=date+timedelta(days=1)
            schedules[schedule_name]["thursday"]=date+timedelta(days=2)
            schedules[schedule_name]["friday"]=date+timedelta(days=3)
            schedules[schedule_name]["saturday"]=date+timedelta(days=4)
            schedules[schedule_name]["sunday"]=date+timedelta(days=5)
        elif week_day == 2:
            schedules[schedule_name]["monday"]=date+timedelta(days=-2)
            schedules[schedule_name]["tuesday"]=date+timedelta(days=-1)
            schedules[schedule_name]["wednesday"]=date
            schedules[schedule_name]["thursday"]=date+timedelta(days=1)
            schedules[schedule_name]["friday"]=date+timedelta(days=2)
            schedules[schedule_name]["saturday"]=date+timedelta(days=3)
            schedules[schedule_name]["sunday"]=date+timedelta(days=4)
        elif week_day == 3:
            schedules[schedule_name]["monday"]=date+timedelta(days=-3)
            schedules[schedule_name]["tuesday"]=date+timedelta(days=-2)
            schedules[schedule_name]["wednesday"]=date+timedelta(days=-1)
            schedules[schedule_name]["thursday"]=date
            schedules[schedule_name]["friday"]=date+timedelta(days=1)
            schedules[schedule_name]["saturday"]=date+timedelta(days=2)
            schedules[schedule_name]["sunday"]=date+timedelta(days=3)
        elif week_day == 4:
            schedules[schedule_name]["monday"]=date+timedelta(days=-4)
            schedules[schedule_name]["tuesday"]=date+timedelta(days=-3)
            schedules[schedule_name]["wednesday"]=date+timedelta(days=-2)
            schedules[schedule_name]["thursday"]=date+timedelta(days=-1)
            schedules[schedule_name]["friday"]=date
            schedules[schedule_name]["saturday"]=date+timedelta(days=1)
            schedules[schedule_name]["sunday"]=date+timedelta(days=2)
        elif week_day == 5:
            schedules[schedule_name]["monday"]=date+timedelta(days=-5)
            schedules[schedule_name]["tuesday"]=date+timedelta(days=-4)
            schedules[schedule_name]["wednesday"]=date+timedelta(days=-3)
            schedules[schedule_name]["thursday"]=date+timedelta(days=-2)
            schedules[schedule_name]["friday"]=date+timedelta(days=-1)
            schedules[schedule_name]["saturday"]=date
            schedules[schedule_name]["sunday"]=date+timedelta(days=1)
        else:
            schedules[schedule_name]["monday"]=date+timedelta(days=-6)
            schedules[schedule_name]["tuesday"]=date+timedelta(days=-5)
            schedules[schedule_name]["wednesday"]=date+timedelta(days=-4)
            schedules[schedule_name]["thursday"]=date+timedelta(days=-3)
            schedules[schedule_name]["friday"]=date+timedelta(days=-2)
            schedules[schedule_name]["saturday"]=date+timedelta(days=-1)
            schedules[schedule_name]["sunday"]=date
        log.debug("Segunda de horario definido '%s'.", schedules[schedule_name]["monday"])
        log.debug("Terca de horario definido '%s'.", schedules[schedule_name]["tuesday"])
        log.debug("Quarta de horario definido '%s'.", schedules[schedule_name]["wednesday"])
        log.debug("Quinta de horario definido '%s'.", schedules[schedule_name]["thursday"])
        log.debug("Sexta de horario definido '%s'.", schedules[schedule_name]["friday"])
        log.debug("Sabado de horario definido '%s'.", schedules[schedule_name]["saturday"])
        log.debug("Domingo de horario definido '%s'.", schedules[schedule_name]["sunday"])
        save_schedule()
        log.info("Horario criado com sucesso '%s'.", date)
        return 200, schedules[schedule_name]["id"]
    else:
        log.error("Horario já existe nesse semana '%s'.", date)
        return 409, "Already exists"

def read_schedule(schedule_id):
    log.info("Pesquisar horario '%s'.", schedule_id)
    load_schedule()
    continue_path=False
    log.debug("Pesquisa de horario iniciado '%s'.", schedule_id)
    for i in schedules:
        if "id" in schedules[i]:
            if schedules[i]["id"] == schedule_id:
                schedule_name=i
                continue_path=True
                log.debug("Horario encontrado '%s'.", schedule_id)
    if continue_path:
        log.info("Horario Encontrado com sucesso '%s'.", schedule_id)
        return 200, schedules[schedule_name]
    else:
        log.error("Horario não encontrado '%s'.", schedule_id)
        return 404, "Schedule not found"

def update_schedule(day,month,year,schedule_id):
    log.info("Atualizar horario '%s'.", schedule_id)
    load_schedule()
    continue_path=False
    log.debug("Pesquisa de horario iniciado '%s'.", schedule_id)
    for i in schedules:
        if "id" in schedules[i]:
            if schedules[i]["id"] == schedule_id:
                schedule_name=i
                continue_path=True
                log.debug("horario encontrado '%s'.", schedule_id)
    if continue_path:
        big_break = False
        continue_path_2 = True
        date = datetime(year, month, day)
        for i in schedules:
            for j in schedules[i]:
                if type(schedules[i][j]) is datetime:
                    if schedules[i][j] == date:
                        continue_path_2 = False
                        big_break = True
                        break
                    else:
                        continue_path_2 = True
            if big_break:
                break
        if continue_path_2:
            week_day = date.weekday()
            if week_day == 0:
                schedules[schedule_name]["monday"] = date
                schedules[schedule_name]["tuesday"] = date + timedelta(days=1)
                schedules[schedule_name]["wednesday"] = date + timedelta(days=2)
                schedules[schedule_name]["thursday"] = date + timedelta(days=3)
                schedules[schedule_name]["friday"] = date + timedelta(days=4)
                schedules[schedule_name]["saturday"] = date + timedelta(days=5)
                schedules[schedule_name]["sunday"] = date + timedelta(days=6)
            elif week_day == 1:
                schedules[schedule_name]["monday"] = date + timedelta(days=-1)
                schedules[schedule_name]["tuesday"] = date
                schedules[schedule_name]["wednesday"] = date + timedelta(days=1)
                schedules[schedule_name]["thursday"] = date + timedelta(days=2)
                schedules[schedule_name]["friday"] = date + timedelta(days=3)
                schedules[schedule_name]["saturday"] = date + timedelta(days=4)
                schedules[schedule_name]["sunday"] = date + timedelta(days=5)
            elif week_day == 2:
                schedules[schedule_name]["monday"] = date + timedelta(days=-2)
                schedules[schedule_name]["tuesday"] = date + timedelta(days=-1)
                schedules[schedule_name]["wednesday"] = date
                schedules[schedule_name]["thursday"] = date + timedelta(days=1)
                schedules[schedule_name]["friday"] = date + timedelta(days=2)
                schedules[schedule_name]["saturday"] = date + timedelta(days=3)
                schedules[schedule_name]["sunday"] = date + timedelta(days=4)
            elif week_day == 3:
                schedules[schedule_name]["monday"] = date + timedelta(days=-3)
                schedules[schedule_name]["tuesday"] = date + timedelta(days=-2)
                schedules[schedule_name]["wednesday"] = date + timedelta(days=-1)
                schedules[schedule_name]["thursday"] = date
                schedules[schedule_name]["friday"] = date + timedelta(days=1)
                schedules[schedule_name]["saturday"] = date + timedelta(days=2)
                schedules[schedule_name]["sunday"] = date + timedelta(days=3)
            elif week_day == 4:
                schedules[schedule_name]["monday"] = date + timedelta(days=-4)
                schedules[schedule_name]["tuesday"] = date + timedelta(days=-3)
                schedules[schedule_name]["wednesday"] = date + timedelta(days=-2)
                schedules[schedule_name]["thursday"] = date + timedelta(days=-1)
                schedules[schedule_name]["friday"] = date
                schedules[schedule_name]["saturday"] = date + timedelta(days=1)
                schedules[schedule_name]["sunday"] = date + timedelta(days=2)
            elif week_day == 5:
                schedules[schedule_name]["monday"] = date + timedelta(days=-5)
                schedules[schedule_name]["tuesday"] = date + timedelta(days=-4)
                schedules[schedule_name]["wednesday"] = date + timedelta(days=-3)
                schedules[schedule_name]["thursday"] = date + timedelta(days=-2)
                schedules[schedule_name]["friday"] = date + timedelta(days=-1)
                schedules[schedule_name]["saturday"] = date
                schedules[schedule_name]["sunday"] = date + timedelta(days=1)
            else:
                schedules[schedule_name]["monday"] = date + timedelta(days=-6)
                schedules[schedule_name]["tuesday"] = date + timedelta(days=-5)
                schedules[schedule_name]["wednesday"] = date + timedelta(days=-4)
                schedules[schedule_name]["thursday"] = date + timedelta(days=-3)
                schedules[schedule_name]["friday"] = date + timedelta(days=-2)
                schedules[schedule_name]["saturday"] = date + timedelta(days=-1)
                schedules[schedule_name]["sunday"] = date
            log.debug("Segunda de horario atualizado '%s'.", schedules[schedule_name]["monday"])
            log.debug("Terca de horario atualizado '%s'.", schedules[schedule_name]["tuesday"])
            log.debug("Quarta de horario atualizado '%s'.", schedules[schedule_name]["wednesday"])
            log.debug("Quinta de horario atualizado '%s'.", schedules[schedule_name]["thursday"])
            log.debug("Sexta de horario atualizado '%s'.", schedules[schedule_name]["friday"])
            log.debug("Sabado de horario atualizado '%s'.", schedules[schedule_name]["saturday"])
            log.debug("Domingo de horario atualizado '%s'.", schedules[schedule_name]["sunday"])
            save_schedule()
            log.info("Horario atualizado com successo '%s'.", schedule_id)
            return 200, schedules[schedule_name]["id"]
        else:
            log.error("Horario já existe nesse semana '%s'.", date)
            return 409, schedules[schedule_name]["id"]
    else:
        log.error("Horario não encontrado '%s'.", schedule_id)
        return 404, schedules[schedule_name]["id"]

def delete_schedule(schedule_id):
    log.info("Removir horario '%s'.", schedule_id)
    load_schedule()
    continue_path=False
    log.debug("Pesquisa de horario iniciado '%s'.", schedule_id)
    for i in schedules:
        if "id" in schedules[i]:
            if schedules[i]["id"] == schedule_id:
                schedule_name=i
                continue_path=True
                log.debug("Horario encontrado '%s'.", schedule_id)
    if continue_path:
        del schedules[schedule_name]
        save_schedule()
        log.info("Horario apagado com sucesso '%s'.", schedule_id)
        return 200, schedule_id
    else:
        log.error("Horario não encontrado '%s'.", schedule_id)
        return 404, "Schedule not found"