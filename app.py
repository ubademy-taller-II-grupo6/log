from fastapi import FastAPI
from routers.user import user

app = FastAPI(
            title= "Ubademy-Log de usuarios",
            description= "API de log de eventos, implementa operaciones CRUD",
            version=1.0
              )

app.include_router(user)


