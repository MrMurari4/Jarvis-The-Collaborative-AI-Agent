
```markdown
███████╗███╗   ██╗███████╗██╗  ██╗██╗   ██╗
██╔════╝████╗  ██║██╔════╝██║ ██╔╝██║   ██║
█████╗  ██╔██╗ ██║█████╗  █████╔╝ ██║   ██║
██╔══╝  ██║╚██╗██║██╔══╝  ██╔═██╗ ██║   ██║
███████╗██║ ╚████║███████╗██║  ██╗╚██████╔╝
╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
             J A R V I S  A I  A G E N T

# 🤖 Jarvis – AI Collaboration Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Gemini API](https://img.shields.io/badge/Gemini%20API-Enabled-orange.svg)
![Status](https://img.shields.io/badge/Project-Active-brightgreen.svg)

### **Tagline:**  
**A smart AI agent that collaborates with you in real-time — for both creative writing & code debugging.**

---

## 📌 Overview

Jarvis is an intelligent AI assistant powered by **Google Gemini API**.  
It automatically detects whether the user is asking for a **creative** or **analytical** task — and responds accordingly.

| Task Type | Examples |
|-----------|----------|
| 🧠 Analytical | Debug Python code, explain errors, break down logic |
| 🎨 Creative | Story writing, plots, character ideas, brainstorming |

This project is built for live demonstration, academic presentation, and portfolio showcase.

---

## ✨ Features

- Gemini API powered agent (Gemini 1.5 Pro)
- Command-line interactive chat
- Auto detects intent from message
- `/reset` → resets chat context
- `/exit` → closes session
- Includes buggy mini Python script for test debugging

---

## 📂 Project Structure

```

📦 Nexus-AI-Agent
├── jarvis_agent.py        # main interactive AI agent
├── test_agent_bug.py     # intentionally buggy sample code
├── README.md             # documentation
└── .gitignore            # git ignore rules

````

---

## 🚀 How To Run

### 1) Install Dependency
```bash
pip install google-generativeai
````

### 2) Insert Your API Key

Inside `nexus_agent.py`:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```

> ⚠️ DO NOT COMMIT YOUR REAL KEY TO GITHUB

### 3) Run Agent

```bash
python nexus_agent.py
```

---

## 🧪 Test The Debugging Ability

Run the buggy file:

```bash
python test_agent_bug.py
```

Bug in code:

```python
return mesage   # ❌ should be message
```

Ask Jarvis:

> “Why does this code crash?”

He should point out the typo.

---

## 💡 Example Chat Commands

| Command  | Meaning            |
| -------- | ------------------ |
| `/reset` | Reset conversation |
| `/exit`  | Quit agent         |

---

## ✅ Ideal Use Cases

* Python learning assistant
* Proving reasoning ability of LLM
* AI lab / project submission
* Showcase in portfolio
* Debugging helper for beginners

---

## 📄 License

This project is for **learning, experimentation, and academic use**.

---

### ⭐ If you liked this project — star the repo!

```
git add .
git commit -m "Added README / documentation"
git push
```

```
Jarvis IS ALWAYS READY TO COLLABORATE ⚡
```



Tell me which one you want next.
```
