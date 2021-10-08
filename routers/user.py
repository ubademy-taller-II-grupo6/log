from fastapi import APIRouter
from config.db  import client
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()


@user.get('/users')
def get_all_users():
    return usersEntity(client.local.Login.find())


@user.post('/users')
def create_user(user: User):
    new_User = dict(User)
    print(new_User)
    return "usuario recibido"


@user.get('/users/{id}')
def find_user():
    return "helloworl"


@user.put('/users')
def update_user():
    return "hellor"


@user.delete('/users/{id}')
def delete_user():
    return "borrar"
