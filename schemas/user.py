#Describe que tendra cada usuario
import json


def userEntity (item) -> dict:
    return {
        "id": str(item["_id"]),
        "userId": item["userId"],
        "nivel": str(item["nivel"]),
        "fecha": item["fecha"],
        "hora": item["hora"],
        "descripcion": item["descripcion"]
    }


def usersEntity (entity) -> list:
    return [userEntity(item) for item in entity]

