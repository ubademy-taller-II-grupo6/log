import os
import uvicorn
from fastapi import FastAPI
from routers.log import log

app = FastAPI(
            title= "Ubademy-Log de usuarios",
            description= "API de log de eventos, implementa operaciones CRUD",
            version=1.0
              )

app.include_router(log)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=int(os.environ.get('PORT')), reload=True)



