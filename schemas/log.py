#Describe que tendra cada usuario
import json


def entryEntity (item) -> dict:
    return {
        "id": str(item["_id"]),
        "userId": item["userId"],
        "fecha": item["fecha"],
        "hora": item["hora"],
        "nivel": item["nivel"],
        "descripcion": item["descripcion"]
    }


def entrysEntity (entity) -> list:
    return [entryEntity(item) for item in entity]

