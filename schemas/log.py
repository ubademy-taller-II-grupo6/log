#Describe que tendra cada usuario
import json


def entryEntity (item) -> dict:
    return {
        "id": str(item["_id"]),
        "userId": item["userId"],
        "nivel": item["nivel"],
        "fecha": item["fecha"],
        "hora": item["hora"],
        "descripcion": item["descripcion"]
    }


def entrysEntity (entity) -> list:
    return [entryEntity(item) for item in entity]

