import json
import os
from logger import get_logger
import general_functions
from product import items,lists,read_product_by_id, update_product

log = get_logger("orders")

ORDERS_FILE="saves/orders.json"
default_sales = {
    "temp_order":{
        "quantities":{},
        "items":{}
    },
    "orders":{}
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
        log.debug("ordens carregados: '%s'.", len(sales))
    else:
        sales = {}
        log.debug("Ficheiro nao encontrado. Base iniciada vazia: '%s'.", ORDERS_FILE)

def create_item_order(item_id,item_quantity,seller_name):
    log.info("Adicionar item para order: id='%s'.", item_id)
    load_orders()
    if seller_name not in sales:
        sales[seller_name] = default_sales
        log.debug("Dictionario de vendedor criado: id='%s'.", seller_name)
    item_name=""
    return_code, return_item_values, return_item_quantity, item_name = read_product_by_id(item_id, seller_name)
    if item_name!="":
        item_price = return_item_values["price"] * item_quantity
        if item_name not in sales[seller_name]["temp_order"]["items"]:
            sales[seller_name]["temp_order"]["items"][item_name] = {}
            log.debug("Dictionario de item criado na order: name='%s'.", item_name)
            sales[seller_name]["temp_order"]["items"][item_name]["name"] = item_name
            sales[seller_name]["temp_order"]["items"][item_name]["price"] = item_price
            log.debug("preço do conjunto de artigos: preço='%s'.", item_price)
            sales[seller_name]["temp_order"]["quantities"][item_name] = item_quantity
            log.debug("quantidade do conjunto de artigos: quantidade='%s'.", item_quantity)
            return_item_quantity -= item_quantity
        else:
            sales[seller_name]["temp_order"]["items"][item_name]["price"] += item_price
            log.debug("preço de artigo aumentou: preço='%s'.", item_price)
            sales[seller_name]["temp_order"]["quantities"][item_name] += item_quantity
            log.debug("quantidade de artigo aumentou: quantidade='%s'.", item_quantity)
            return_item_quantity -= item_quantity
        save_orders()
        log.info("Item adicionado por order: id='%s'.", item_id)
        return 200, sales[seller_name]["temp_order"]["items"],sales[seller_name]["temp_order"]["quantities"][item_name]
    else:
        log.error("Item não encontrado: id='%s'.", item_id)
        return 404, "not found", ""

def delete_item_order(item_name,seller_name):
    log.info("Removir item de order: id='%s'.", item_name)
    load_orders()
    if item_name in sales[seller_name]["temp_order"]["items"]:
        del sales[seller_name]["temp_order"]["items"][item_name]
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
    if item_name in sales[seller_name]["temp_order"]["items"]:
        price_default = sales[seller_name]["temp_order"]["items"][item_name]["price"] / sales[seller_name]["temp_order"]["quantities"][item_name]
        sales[seller_name]["temp_order"]["quantities"][item_name] = item_quantity
        log.debug("Quantidade de item atualizado: id='%s'.", item_quantity)
        sales[seller_name]["temp_order"]["items"][item_name]["price"] = price_default * item_quantity
        log.debug("price de item atualizado: id='%s'.", sales[seller_name]["temp_order"]["items"][item_name]["price"])
        log.info("Item foi atualizado: id='%s'.", item_name)
        save_orders()
        return 200, "success"
    else:
        log.warning("Item não foi encontrado: id='%s'.", item_name)
        return 404, "Failure"

def read_item_order(seller_name):
    log.info("Mostrar items de order: id='%s'.", seller_name)
    load_orders()
    if len(sales[seller_name]["temp_order"]["items"]) > 0:
        counter = 1
        log.debug("A impressão dos artigos já começou.: id='%s'.", seller_name)
        for i in sales[seller_name]["temp_order"]["items"].keys():
            counter += 1
        log.info("Os artigos mostrando com sucesso.: id='%s'.", seller_name)
        return 200, sales[seller_name]["temp_order"]
    else:
        log.info("Não há lá itens: id='%s'.", seller_name)
        return 204, "No content"

def next_order(seller_name):
    load_orders()
    order_number=len(sales[seller_name]["orders"])+1
    order_name="order_"+str(order_number)
    sales[seller_name]["orders"][order_name]={}
    sales[seller_name]["orders"][order_name]=sales[seller_name]["temp_order"]
    sales[seller_name]["temp_order"]=default_sales["temp_order"]
    save_orders()