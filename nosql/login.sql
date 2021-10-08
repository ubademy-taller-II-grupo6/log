use ubademyLog;
db.createCollection("Login", {
  validator: {
    $and: [
      {
        "userId": {$type: "string", $exists: true}
      },
      {
        "respuesta": { $type: "string", $exists: true}
      },
      {
        "codigo_respuesta": { $type: "string", $exists: true}
      },
      {
        "session_star_date": { $type: "string", $exists: true}
      },
      {
        "session_end_date": { $type: "string", $exists: true}
      }
            ]
    }
  }
);

db.Login.insertOne({
    userId: "mriarte@gmail",
    nivel: "Info",
    fecha: "10/10/2021",
    hora: "10:41:34 AM",
    descripcion: "Usuario Logueado"
});
