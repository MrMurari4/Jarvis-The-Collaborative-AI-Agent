import google.generativeai as genai
import re


genai.configure(api_key="YOUR_API_KEY_HERE")


SYSTEM_PROMPT = """
You are 'Jarvis', a friendly collaborative AI skilled in:
1. Creative writing (stories, ideas, scripts, dialogues)
2. Analytical reasoning (debugging code, solving problems, explaining logic)
Behave like a helpful teammate. Keep replies concise, intelligent, and interactive.
"""

def detect_task_type(text: str) -> str:
    if re.search(r"(def |import |error|traceback|code|bug|debug|syntax|function|variable)", text, re.I):
        return "analytical"
    elif re.search(r"(story|plot|character|poem|imagine|creative)", text, re.I):
        return "creative"
    else:
        return "neutral"

# Start model session
model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat(history=[{"role": "user", "parts": [SYSTEM_PROMPT]}])

print("Jarvis (Gemini): Ready to collaborate! Type '/exit' to quit or '/reset' to start new session.\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue

    if user_input.lower() == "/exit":
        print("Nexus: Goodbye . Keep creating!")
        break

    if user_input.lower() == "/reset":
        chat = model.start_chat(history=[{"role": "user", "parts": [SYSTEM_PROMPT]}])
        print(" Conversation reset.\n")
        continue

    task_type = detect_task_type(user_input)
    tagged_input = f"[{task_type.upper()} TASK] {user_input}"

    try:
        response = chat.send_message(tagged_input)
        print(f"\nNexus: {response.text.strip()}\n")

    except Exception as e:
        print(f"Error: {e}")
