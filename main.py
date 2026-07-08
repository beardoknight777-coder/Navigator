# ============================================
# Navigator
# Version: 0.3
# Built by Jo
# Started: July 6, 2026
# Mission: Personal AI Command Console
# Motto: "For the King."
# ============================================
from modules.menu import show_menu
import subprocess
from datetime import datetime
import os
print("=" * 45)
print("         NAVIGATOR v0.3")
print("     Personal AI Command Console")
print("=" * 45)
print()

print("Welcome back, Nomad.")
print("Mission Control Online.")
print("Mission Time:",datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print()

models = {
    "1": "llama3.2:3b",
    "2": "deepseek-r1:7b",
    "3": "gemma3:4b",
    "4": "qwen3:4b"
}

# Create logs folder if it dosen't exist 
os.makedirs("logs", exist_ok=True)

while True:
    show_menu()

    choice = input("\nSelect mission: ")

    if choice == "5":
        print("\nNavigator standing by.")
        break

    if choice not in models:
        print("Invalid choice. Try again.")
        continue

    prompt = input("\nAsk your question: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/mission_log.txt", "a", encoding="utf-8") as log:
        log.write("=" * 50 + "\n")
        log.write(f"Mission Time : {timestamp}\n")
        log.write(f"Model        : {models[choice]}\n")
        log.write(f"Question     : {prompt}\n\n")

    print("\n--- Response ---\n")
    print("DEBUG: About to run Ollama...")

    subprocess.run([
        "ollama",
        "run",
        models[choice],
        prompt
    ])