from fastapi import APIRouter
from config.db import client
from schemas.user import userEntity, usersEntity
from models.user import User


user = APIRouter()


@user.get('/users')
def find_all_users():
    return usersEntity(client.ubademyLog.Login.find())


@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    #Guarda el usuario recibido en la base de datos ,esta le asigna un id
    id  = client.ubademyLog.Login.insert_one(new_user).inserted_id
    #Busca en base el id anterior el usuario y lo devuelve
    user = client.ubademyLog.Login.find_one(id)
    return userEntity(user)


#Devuelve todos los documentos de un userId

@user.get('/users/{userid}', response_model=User)
def find_user(userid: str):
    return usersEntity(client.ubademyLog.Login.find({"userId": userid}))


@user.get('/users/{nivel}')
def find_user(nivel: str):
    return usersEntity(client.ubademyLog.Login.find({"nivel": nivel}))

@user.get('/users')
def find_users(userid: str, nivel: str):
    return usersEntity(client.ubademyLog.Login.find({"nivel": nivel}, {"userId": userid}))


@user.put('/users')
def update_user():
    return "hellor"


@user.delete('/users/{id}')
def delete_user():
    return "borrar"
