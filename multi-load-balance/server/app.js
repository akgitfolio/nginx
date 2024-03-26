// api1.js
const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send(`Response from Server ${port}`);
});

app.listen(port, () => {
  console.log(`Service 1 listening at http://localhost:${port}`);
});
