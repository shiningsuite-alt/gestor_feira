import json
import os
from logger import get_logger
import general_functions

log = get_logger("sellers")

SELLERS_FILE = "saves/sellers.json"

listed_names=[]
headers= [
    "Id",
    "Name",
    "Product type",
    "Time",
    "Day",
    "Description"
]

sellers={
}

def save_sellers():
    with open(SELLERS_FILE, "w", encoding="utf-8") as ficheiro:
        log.debug("Ficha de sellers aberto '%s'.", SELLERS_FILE)
        json.dump(sellers, ficheiro, indent=4, ensure_ascii=False)
    log.debug("Vendedores guardados em '%s'.", SELLERS_FILE)

def load_sellers():
    global sellers
    if os.path.exists(SELLERS_FILE):
        log.debug("Ficha vendedores encontrada '%s'.", SELLERS_FILE)
        with open(SELLERS_FILE, "r", encoding="utf-8") as ficheiro:
            log.debug("Ficha de sellers aberto '%s'.", SELLERS_FILE)
            sellers = json.load(ficheiro)
        log.info("Ficha vendedores guardado '%s'.", SELLERS_FILE)
    else:
        log.debug("Ficha vendedores não foi encontrada '%s'.", SELLERS_FILE)
        sellers = {}

def create_seller(name, product_type,extra_description):
    log.info("Criar vendedor '%s'.", name)
    load_sellers()
    sellers[name]={}
    counter = 1
    if name not in listed_names:
        listed_names.append(name)
        log.debug("Vendedor adicionado a lista de vendedores '%s'.", name)
    counter=1
    for i in sellers:
        if "ID" in sellers[i]:
            if counter==sellers[i]["ID"]:
                counter+=1
    sellers[name]["ID"] = counter
    log.debug("Conjunto de ID do vendedor '%s'.", counter)
    sellers[name]["name"] = name
    log.debug("Conjunto de nome do vendedor '%s'.", name)
    sellers[name]["product_type"] = product_type
    log.debug("Conjunto de tipo de produto do vendedor '%s'.", product_type)
    if extra_description == "" or extra_description == " ":
        sellers[name]["extra_description"]="none"
        log.debug("Conjunto de descrição do vendedor '%s'.", sellers[name]["extra_description"])
    else:
        sellers[name]["extra_description"]=extra_description
        log.debug("Conjunto de descrição do vendedor '%s'.", sellers[name]["extra_description"])
    save_sellers()
    log.info("Vendedor criado com sucesso'%s'.", name)
    return 200, sellers[name]

def read_sellers(seller_id):
    log.info("Pesquisa de vendedor '%s'.", seller_id)
    load_sellers()
    found=False
    log.debug("Pesquisa de vendedor iniciado '%s'.", seller_id)
    for name in sellers:
        if sellers[name]["ID"] == seller_id:
            found=True
            log.debug("Vendedor encontrado e informação guardado'%s'.", seller_id)
            seller_name=name
            break
    if found:
        log.info("Vendedor encontrado com sucesso '%s'.", seller_id)
        return 200, sellers[seller_name], seller_name
    else:
        log.error("Vendedor não encontrado '%s'.", seller_id)
        return 404, "not found", ""

def update_seller(seller_id,new_name, product_type,extra_description):
    log.info("Atualização de vendedor '%s'.", seller_id)
    load_sellers()
    log.debug("Pesquisa de vendedor iniciado '%s'.", seller_id)
    found=False
    for i in sellers:
        if sellers[i]["ID"]==seller_id:
            name=i
            found=True
            log.debug("Vendedor encontrado e informação guardado'%s'.", seller_id)
            break
        else:
            found=False
    if found:
        if new_name not in listed_names:
            listed_names.append(new_name)
        if sellers[name]["name"] != new_name:
            sellers[new_name]=sellers[name]
            del sellers[name]
            name=new_name
            sellers[name]["name"] = new_name
            log.debug("nome do vendedor atualizado'%s'.", name)
        if sellers[name]["product_type"] != product_type:
            sellers[name]["product_type"] = product_type
            log.debug("tipo de produto do vendedor atualizado'%s'.", product_type)
        if extra_description == "" or extra_description == " ":
            sellers[name]["extra_description"]="none"
            log.debug("descrição do vendedor atualizado'%s'.", sellers[name]["extra_description"])
        else:
            sellers[name]["extra_description"]=extra_description
            log.debug("descrição do vendedor atualizado'%s'.", sellers[name]["extra_description"])
        save_sellers()
        log.info("Vendedor atualizado com sucesso '%s'.", seller_id)
        return 200, sellers[name]
    else:
        log.error("Vendedor não encontrado '%s'.", seller_id)
        save_sellers()
        return 404, "not found"

def delete_sellers(id_select):
    log.info("Removir vendedor '%s'.", id_select)
    load_sellers()
    log.debug("Pesquisa de vendedor iniciado '%s'.", id_select)
    found_id=False
    for name in sellers:
        if "ID" in sellers[name]:
            if sellers[name]["ID"] == id_select:
                del sellers[name]
                found_id = True
                log.debug("Vendedor encontrado e informação apagado'%s'.", id_select)
                break
        else:
            found_id = False
    if not found_id:
        log.error("Vendedor não encontrado '%s'.", id_select)
        return 404, "not found"
    else:
        save_sellers()
        log.info("Vendedor apagado com sucesso '%s'.", id_select)
        return 200, id_select
