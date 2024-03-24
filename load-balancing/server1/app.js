// api1.js
const express = require("express");
const app = express();
const port = 3000 || process.argv[2];

app.get("/", (req, res) => {
  res.send("Response from Server 1");
});

app.listen(port, () => {
  console.log(`Service 1 listening at http://localhost:${port}`);
});
