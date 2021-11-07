use ubademyLog;
db.createCollection("Log", {
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

db.Log.insertOne({
   userId: "us45Y67RTdZxx",
   fecha: "05/10/21",
   hora: "08:22:22 PM",
   nivel: "ERROR",
   descripcion: "Usuario ya creado"
});
