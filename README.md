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
````
## 📂 Project Structure
├── jarvis_agent.py # main interactive AI agent
├── test_agent_bug.py # intentionally buggy sample code
├── README.md # documentation
````

## 🚀 How To Run
````markdown
---

## 🚀 How To Run

### 1) Install Dependency
```bash
pip install google-generativeai
````

### 2) Add Your API Key

open `nexus_agent.py` and set your Gemini API key:

```
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
```
### 3) Run the Agent

```bash
python nexus_agent.py
```



