import json
import os
from datetime import date
from logger import get_logger
import general_functions

log = get_logger("products")

PRODUCT_FILE="products.json"
items =  {
}
default_items =  {
    "quantities":{}
}
lists= {
    "items_class":[]
}

def guardar_produtos():
    with open(PRODUCT_FILE, "w", encoding="utf-8") as ficheiro:
        log.debug("Arquivo dos produtos aberto '%s'.", PRODUCT_FILE)
        json.dump(items, ficheiro, indent=4, ensure_ascii=False)
    log.debug("Produtos guardados em '%s'.", PRODUCT_FILE)

def carregar_produtos():
    global items
    if os.path.exists(PRODUCT_FILE):
        log.debug("Ficheiro dos produtos encontrado '%s'.", PRODUCT_FILE)
        with open(PRODUCT_FILE, "r", encoding="utf-8") as ficheiro:
            log.debug("Arquivo dos produtos aberto '%s'.", PRODUCT_FILE)
            items = json.load(ficheiro)
        log.debug("Produtos carregados: %d registo(s).", len(items))
    else:
        items = {}
        log.debug("Ficheiro '%s' nao encontrado. Base iniciada vazia: %d registo(s).", PRODUCT_FILE)

def create_product(name,price,quantity,item_class, seller_name):
    log.info("Criar Produto: nome='%s'.", name)
    carregar_produtos()
    if seller_name not in items:
        items[seller_name] = default_items
        log.debug("Dictionario de vendedor criado: id='%s'.", seller_name)
    if name not in items[seller_name]:
        items[seller_name][name] = {}
        log.debug("Dicionario de item criado : id='%s'.", name)
        id_item = 1
        for i in items[seller_name].keys():
            if "id" in items[seller_name][i]:
                if id_item == items[seller_name][i]["id"]:
                    id_item += 1
        items[seller_name][name]["id"] = id_item
        log.debug("ID do conjunto de artigos : id='%s'.", id_item)
        items[seller_name][name]["name"]=name
        log.debug("nome do conjunto de artigos : id='%s'.", name)
        items[seller_name][name]["price"] = price
        log.debug("preço de item criado : id='%s'.", price)
        items[seller_name]["quantities"][name] = quantity
        log.debug("quantidade de item criado : id='%s'.", quantity)
        items[seller_name][name]["class"] = item_class
        log.debug("class de item criado : id='%s'.", item_class)
        general_functions.pause()
        guardar_produtos()
        log.info("produto criado com sucesso : id='%s'.", name)
        return 200, name
    else:
        guardar_produtos()
        log.error("item não criado, já existe um item que isso nome : id='%s'.", name)
        return 409, "Already exists"

def update_product(item_id,new_name,new_class,new_price,new_quantity, seller_name):
    log.info("Atualizar Produto: id='%s'.", item_id)
    carregar_produtos()
    failure = True
    change = False
    things_changed=[]
    for i in items[seller_name].keys():
        log.debug("Pesquisa de produto iniciada '%s'.", PRODUCT_FILE)
        if "id" in items[seller_name][i]:
            if item_id == items[seller_name][i]["id"]:
                item_name = i
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    if failure:
        log.error("Produto não foi encontrado: id='%s'.", item_id)
        return 404, "Não encontrado"
    else:
        log.debug("Produto foi encontrado '%s'.", PRODUCT_FILE)
        if item_name!=new_name:
            items[seller_name][new_name] = items[seller_name][item_name]
            del items[seller_name][item_name]
            items[seller_name]["quantities"][new_name] = items[seller_name]["quantities"][item_name]
            del items[seller_name]["quantities"][item_name]
            items[seller_name][new_name]["name"] = new_name
            item_name = new_name
            change=True
            log.debug("nome de produto atualizado '%s'.", item_name)
        if items[seller_name][item_name]["class"] != new_class:
            items[seller_name][item_name]["class"] = new_class
            change=True
            log.debug("class de produto atualizado '%s'.", new_class)
        if items[seller_name][item_name]["price"] != new_price:
            items[seller_name][item_name]["price"] = new_price
            change=True
            log.debug("preço de produto atualizado '%s'.", new_price)
        if items[seller_name][item_name]["class"] != new_quantity:
            items[seller_name]["quantities"][item_name] = new_quantity
            change=True
            log.debug("quantidade de produto atualizado '%s'.", new_quantity)
        guardar_produtos()
        if change:
            log.info("Produto Atualizado: id='%s'.", item_id)
            return 200, items[seller_name][item_name], items[seller_name]["quantities"][item_name]
        else:
            log.info("Produto encontrado mas não atualizado: id='%s'.", item_id)
            return 304, "no change"

def delete_product(item_id, seller_name):
    log.info("Remover Produto: id='%s'.", item_id)
    carregar_produtos()
    failure = True
    log.debug("pesquisa de produto iniciado '%s'.", item_id)
    for i in items[seller_name].keys():
        if "id" in items[seller_name][i]:
            if item_id == items[seller_name][i]["id"]:
                print("Removed " + i)
                del items[seller_name][i]
                del items[seller_name]["quantities"][i]
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    guardar_produtos()
    if failure:
        log.error("Produto não foi encontrado: id='%s'.", item_id)
        return 404, i
    else:
        log.info("Remover Produto: id='%s'.", item_id)
        return 200, "success"

def read_product_by_id(item_id, seller_name):
    log.info("Pesquisar Produto: id='%s'.", item_id)
    carregar_produtos()
    failure = True
    log.debug("pesquisa de produto iniciado '%s'.", item_id)
    for i in items[seller_name].keys():
        if "id" in items[seller_name][i]:
            if item_id == items[seller_name][i]["id"]:
                failure = False
                general_functions.pause()
                break
            else:
                failure = True
    if failure:
        log.error("Produto não foi encontrado: id='%s'.", item_id)
        return 404, "not found"
    else:
        log.info("Produto Encontrado: id='%s'.", item_id)
        return 200, items[seller_name][i], items[seller_name]["quantities"][i]