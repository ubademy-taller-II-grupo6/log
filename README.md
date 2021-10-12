# log
Este respositiorio integra servicios en la nube  utilizando atlas + mongo db; exponenos un conjutno de end poits para utilizar<br/> 
Librerias usadas:<br/> 
-FastApi<br/>
-uvicorn<br/>
-Docker<br/>

##### **Infrestrucutra usada**
-Heroku <br/>
-Mongo atlas<br/>

##### **Como Dockerizar:**
-Instalar docker en el sistema operativo ( es nuestro caso sera linux Ubuntu pero puede ser cualquier otro).<br/>
-Instalar heroku en el sistema operativo.<br/>
-Instalar todos los paquetes explicatados en el archivo "requerimets.txt".<br/>
-Crear un docker file.(Se incluye en este repositorio).<br/>
-Ejecutar en la consola de comandos de linux o similar: <br/>
Dentro de la carpeta del proyecto (en nuestro caso sera "PycharmProjects/log")<br/>
$ docker build . -t app:1.0  <br/>
$ docker images -a   <br/>
$ docker run -p 8000:5000 app:1.0  <br/>

En caso de tener  que borrar algun paquete debemos  tener el ImageId del mismo,que se ve en el paso anterior, y ejecutar:<br/>
$docker rmi  550e38ba5899, siendo "550e38ba5899" el ImageId del paquete <br/>

##### **Como realizar el deploy en heroku:**
heroku container:login <br/>
heroku container:push web -a aqueous-everglades-25138<br/>
heroku create<br/>

heroku container:release web -a aqueous-everglades-25138<br/>
##### **Descripcion de los ENDPOINTS:**
Se exponens los siguientes endpoints en las siguientes URL , utilizando heroku:<br/>

-Crear una nueva entrada de login para un usuario. <br/>
El json de entrada debe tener esta estructura 
Se instancia
-Listar  todos los campos de todos los usuarios  que se han logueado. <br/>
-Obtener todo  los logins de UN usuario.<br/>
-Obtener todos los registos por un rango de fechas.<br/>
-Obtener todos los registros por rango de hora.<br/>
-Obtener todos los registros por NIVEL de incidente.<br/>
-Obtener todos los registros por rango de hora y rango de fecha <br/>

