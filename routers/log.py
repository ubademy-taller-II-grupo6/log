from fastapi import APIRouter
from config.db import client
from schemas.log import entryEntity, entrysEntity
from models.log import Entry
#from config.db import MongoClient
from pymongo import MongoClient


log = APIRouter()


@log.get('/log/user/{userid}')
def find_entrys_by_user(userid: str):
    return entrysEntity(client.ubademyLog.Login.find({"userId": {"$regex": userid, "$options": 'i'}}))


@log.get('/log/{nivel}')
def find_entrys_by_nivel (nivel: str):
    #Consulta case-insensitive
    return entrysEntity(client.ubademyLog.Login.find({"nivel": {"$regex": nivel, "$options": 'i'}}))



@log.post('/log')
def create_entry(entry: Entry):
    new_user = dict(entry)
    #Guarda el usuario recibido en la base de datos ,esta le asigna un id en la DB
    id  = client.ubademyLog.Login.insert_one(new_user).inserted_id
    #Busca en base el id anterior el usuario y lo devuelve
    entry = client.ubademyLog.Login.find_one(id)
    return entryEntity(entry)

