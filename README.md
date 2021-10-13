# log
Este respositiorio integra servicios en la nube  utilizando atlas + mongo db; exponenos un conjunto de end poits para utilizar<br/> 
Librerias usadas:<br/> 
-FastApi<br/>
-uvicorn<br/>
-Docker<br/>

##### **Infrestrucutra usada**
-Heroku <br/>
-Mongo atlas<br/>

##### **Como Dockerizar:**<br/><br/>
-Instalar docker en el sistema operativo ( es nuestro caso sera linux Ubuntu pero puede ser cualquier otro).<br/>
-Instalar heroku en el sistema operativo.<br/>
-Instalar todos los paquetes explicatados en el archivo "requerimets.txt".<br/>
-Crear un docker file.(Se incluye en este repositorio).<br/>
-Ejecutar en la consola de comandos de linux o similar: <br/>
<br/>
Dentro de la carpeta del proyecto (en nuestro caso sera "PycharmProjects/log")<br/>
$ docker build . -t app:1.0  <br/>
$ docker images -a   <br/>
$ docker run -p 8000:5000 app:1.0  <br/>

En caso de tener  que borrar algun paquete debemos  tener el ImageId del mismo,que se ve en el paso anterior, y ejecutar:<br/>
$docker rmi  550e38ba5899, siendo "550e38ba5899" el ImageId del paquete <br/>
<br/>
##### **Como realizar el deploy en heroku:**
heroku container:login <br/>
heroku container:push web -a aqueous-everglades-25138<br/>
heroku create<br/>

heroku container:release web -a aqueous-everglades-25138<br/>
##### **Descripcion de los ENDPOINTS:** <br/>
Se exponens los siguientes endpoints en las siguientes URL , utilizando heroku:<br/>

**-Crear una nueva entrada de login para un usuario.** <br/>
Se da de alta una nueva entra en el log, que contiene, el Id de usuario (usamos el mail), nivel del incidente (INFO,WARNG,DEBUG,ERROR), fecha y hora en que el incidente se dio en el server, y una descripcion del mismo.<br/>

Hacemos un POST a esta direcion<br/>
https://aqueous-everglades-25138.herokuapp.com/users <br/>
El json de entrada debe tener esta estructura <br/>
{<br/>
  "userId": "pininoMas@hotmail.com",<br/>
  "nivel": "Info",<br/>
  "fecha": "10/10/2021",<br/>
  "hora": "10:41:34 AM",<br/>
  "descripcion": "Usuario logueado con exito"<br/>
}<br/>

**-Listar todos los campos de todos los usuarios  que se han logueado.** <br/>
Hacemos un GET a esta direcion<br/>
o directamente pegamos esta direccion al navegador o POSTMAN o gestor de http<br/>
https://aqueous-everglades-25138.herokuapp.com/users<br/>
Nos devolvera un Json con todos los campos de todos los usuario. O sea todas las entradas e incidetentes de todos los usuarios del sistema.<br/>

**-Obtener todo  los logins de UN usuario.**<br/>
Enviamos el userId  de esta forma y nos devolvera todas las entradas al log que tenga ese usuario <br/>
https://aqueous-everglades-25138.herokuapp.com/users/mriarte@gmail <br/>

Resta implemntar: <br/>

-Obtener todos los registos por un rango de fechas.<br/>
-Obtener todos los registros por rango de hora.<br/>
-Obtener todos los registros por NIVEL de incidente.<br/>
-Obtener todos los registros por rango de hora y rango de fecha <br/>

