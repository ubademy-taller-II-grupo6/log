use ubademyLog;
db.createCollection("Login", {
  validator: {
    $and: [
      {
        "userId": {$type: "string", $exists: true}
      },
      {
        "fecha": { $type: "string", $exists: true}
      },
      {
        "hora": { $type: "string", $exists: true}
      },
      {
        "nivel": { $type: "string", $exists: true}
      },
      {
        "descripcion": { $type: "string", $exists: true}
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
