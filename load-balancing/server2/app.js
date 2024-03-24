// api1.js
const express = require("express");
const app = express();
const port = 3002;

app.get("/", (req, res) => {
  res.send("Response from Server 2");
});

app.listen(port, () => {
  console.log(`Service 1 listening at http://localhost:${port}`);
});
