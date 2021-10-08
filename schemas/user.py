#Describe que tendra cada usuario
def userEntity (item) -> dict:
    return {
        "id": item["id"],
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

def usersEntity (entity) -> list:
    [userEntity(entity) for item in entity]
