const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// 🔹 Change this later if needed
const userName = "Abhimanyu";

app.get("/", (req, res) => {
  res.send("Nexus API is running 🚀");
});

app.post("/chat", async (req, res) => {
  const { message, mode } = req.body;

  let prompt = "";

  // 🔥 Mode system
  if (mode === "coding") {
    prompt = `
You are Nexus, a private offline programming assistant.

User: ${userName}

Solve the following coding problem step by step:

${message}

Response format:
1. Understanding
2. Approach
3. Code
4. Complexity

Rules:
- Be correct and concise
- Handle edge cases
- If unsure, say you don't know
`;
  } 
  else if (mode === "debug") {
    prompt = `
You are Nexus, a debugging assistant.

User: ${userName}

Fix the following code and explain the issue clearly:

${message}

Response format:
1. Issue
2. Fix
3. Correct Code
`;
  } 
  else {
    // default chat mode
    prompt = `
You are Nexus, a private offline AI assistant.

User: ${userName}

${message}
`;
  }

  try {
    const response = await fetch("http://localhost:11434/api/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        model: "nexus",
        prompt: prompt,
        stream: false
      })
    });

    const data = await response.json();

    res.json({
      reply: data.response
    });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Error connecting to Nexus model" });
  }
});

app.listen(3000, () => {
  console.log("🚀 Nexus API running at http://localhost:3000");
});