use ubademyLog;
db.createCollection("Login", {
  validator: {
    $and: [
      {
        "userId": {$type: "string", $exists: true}
      },
      {
        "date": { $type: "string", $exists: true}
      },
      {
        "hour": { $type: "string", $exists: true}
      },
      {
        "type": { $type: "string", $exists: true}
      },
      {
        "description": { $type: "string", $exists: true}
      }
            ]
    }
  }
);

db.Login.insertOne({
    userId: "mriarte@gmail",
    type: "Info",
    date: "10/10/2021",
    hour: "10:41:34 AM",
    description: "Usuario Logueado"
});
