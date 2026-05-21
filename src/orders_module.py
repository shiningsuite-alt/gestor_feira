import json
import os
from datetime import date
from logger import get_logger
import general_functions
from product import items
from product import lists

log = get_logger("orders")

ORDERS_FILE="orders.json"
default_sales = {
    "temp_order":{
        "quantities":{},
        "items[seller_name]":{}
    },
    "orders":{},
    "order_names":[]
}
sales = {
}

def save_orders():
    with open(ORDERS_FILE, "w", encoding="utf-8") as ficheiro:
        log.debug("Arquivo dos ordens aberto '%s'.", ORDERS_FILE)
        json.dump(sales, ficheiro, indent=4, ensure_ascii=False)
    log.debug("Ordens guardados em '%s'.", ORDERS_FILE)

def load_orders():
    global sales
    if os.path.exists(ORDERS_FILE):
        log.debug("Arquivo dos ordens encontrado '%s'.", ORDERS_FILE)
        with open(ORDERS_FILE, "r", encoding="utf-8") as ficheiro:
            log.debug("Arquivo dos ordens aberto '%s'.", ORDERS_FILE)
            sales = json.load(ficheiro)
        log.debug("ordens carregados: %d registo(s).", len(sales))
    else:
        sales = {}
        log.debug("Ficheiro '%s' nao encontrado. Base iniciada vazia: %d registo(s).", ORDERS_FILE)

def create_item_order(item_id,item_quantity,seller_name):
    log.info("Adicionar item para order: id='%s'.", item_id)
    load_orders()
    if seller_name not in sales:
        sales[seller_name] = default_sales
        log.debug("Dictionario de vendedor criado: id='%s'.", seller_name)
    item_name=""
    log.debug("Pesquias de item iniciado: id='%s'.", item_id)
    for i in items[seller_name]:
        if "id" in items[seller_name][i]:
            if items[seller_name][i]["id"] == item_id:
                item_name=i
                break
    if item_name!="":
        item_price = items[seller_name][item_name]["price"] * item_quantity
        if item_name not in sales[seller_name]["temp_order"]["items"]:
            sales[seller_name]["temp_order"]["items"][item_name] = {}
            log.debug("Dictionario de item criado na order: name='%s'.", item_name)
            sales[seller_name]["temp_order"]["items"][item_name]["name"] = item_name
            sales[seller_name]["temp_order"]["items"][item_name]["price"] = item_price
            log.debug("preço do conjunto de artigos: preço='%s'.", item_price)
            sales[seller_name]["temp_order"]["quantities"][item_name] = item_quantity
            log.debug("quantidade do conjunto de artigos: quantidade='%s'.", item_quantity)
            items[seller_name]["quantities"][item_name] -= item_quantity
        else:
            sales[seller_name]["temp_order"]["items"][item_name]["price"] += item_price
            log.debug("preço de artigo aumentou: preço='%s'.", item_price)
            sales[seller_name]["temp_order"]["quantities"][item_name] += item_quantity
            log.debug("quantidade de artigo aumentou: quantidade='%s'.", item_quantity)
            items[seller_name]["quantities"][item_name] -= item_quantity
        save_orders()
        log.info("Item adicionado por order: id='%s'.", item_id)
        return 200, "success"
    else:
        log.error("Item não encontrado: id='%s'.", item_id)
        return 404, "not found"

def delete_item_order(item_name,seller_name):
    log.info("Removir item de order: id='%s'.", item_name)
    load_orders()
    if item_name in sales[seller_name]["temp_order"]["items[seller_name]"]:
        items[seller_name]["quantities"][item_name] += sales[seller_name]["temp_order"]["quantities"][item_name]
        del sales[seller_name]["temp_order"]["items[seller_name]"][item_name]
        del sales[seller_name]["temp_order"]["quantities"][item_name]
        log.info("item removido: id='%s'.", item_name)
        save_orders()
        return 200, "success"
    else:
        log.error("item não foi encontrado: id='%s'.", item_name)
        return 404, "not found"

def update_item_order(item_name,item_quantity,seller_name):
    log.info("Atualizar item de order: id='%s'.", item_name)
    load_orders()
    if sales[seller_name]["temp_order"]["quantities"][item_name]!=item_quantity:
        items[seller_name]["quantities"][item_name] += sales[seller_name]["temp_order"]["quantities"][item_name]
        sales[seller_name]["temp_order"]["quantities"][item_name] = 0
        sales[seller_name]["temp_order"]["quantities"][item_name] = general_functions.validation_check_2(items[seller_name]["quantities"][item_name])
        items[seller_name]["quantities"][item_name] -= sales[seller_name]["temp_order"]["quantities"][item_name]
        log.debug("Quantidade de item atualizado: id='%s'.", item_quantity)
        sales[seller_name]["temp_order"]["items[seller_name]"][item_name]["price"] = items[seller_name][item_name]["price"] * sales[seller_name]["temp_order"]["quantities"][item_name]
        log.debug("price de item atualizado: id='%s'.", sales[seller_name]["temp_order"]["items[seller_name]"][item_name]["price"])
        log.info("Item foi atualizado: id='%s'.", item_name)
        save_orders()
        return 200, "success"
    else:
        log.warning("Item não foi atualizado: id='%s'.", item_name)
        save_orders()
        return 304, "no change"

def read_item_order(seller_name):
    log.info("Mostrar items de order: id='%s'.", seller_name)
    load_orders()
    if len(sales[seller_name]["temp_order"]["items[seller_name]"]) > 0:
        counter = 1
        log.debug("A impressão dos artigos já começou.: id='%s'.", seller_name)
        for i in sales[seller_name]["temp_order"]["items[seller_name]"].keys():
            print(str(counter) + " - " + str(sales[seller_name]["temp_order"]["items[seller_name]"][i]) + ", quantities:'"+ str(sales[seller_name]["temp_order"]["quantities"][i])+"'")
            counter += 1
        log.info("Os artigos mostrando com sucesso.: id='%s'.", seller_name)
        return 200, "success"
    else:
        log.info("Não há lá itens: id='%s'.", seller_name)
        return 204, "No content"