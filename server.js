const express = require("express");
const cors = require("cors");
const bcrypt = require("bcrypt");
const db = require("./database");

const app = express();
app.use(cors());
app.use(express.json());

/* REGISTER */
app.post("/api/register", async (req, res) => {
  const { user, pass } = req.body;
  if (!user || !pass) {
    return res.status(400).json({ error: "Missing data" });
  }

  const hash = await bcrypt.hash(pass, 10);

  db.run(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    [user, hash],
    function (err) {
      if (err) {
        return res.status(400).json({ error: "User already exists" });
      }
      res.json({ success: true });
    }
  );
});

/* LOGIN */
app.post("/api/login", (req, res) => {
  const { user, pass } = req.body;

  db.get(
    "SELECT * FROM users WHERE username = ?",
    [user],
    async (err, row) => {
      if (!row) {
        return res.status(401).json({ error: "Invalid login" });
      }

      const ok = await bcrypt.compare(pass, row.password);
      if (!ok) {
        return res.status(401).json({ error: "Invalid login" });
      }

      res.json({
        success: true,
        user: row.username
      });
    }
  );
});

app.listen(3000, () =>
  console.log("API running on http://localhost:3000")
);
