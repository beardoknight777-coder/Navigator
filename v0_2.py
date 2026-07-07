import subprocess

models = {
    "1": "llama3.2:3b",
    "2": "deepseek-r1:7b",
    "3": "gemma3:4b",
    "4": "qwen3:4b"
}

while True:
    print("\n" + "=" * 40)
    print("          NAVIGATOR v0.2")
    print("=" * 40)
    print("1 - Llama")
    print("2 - DeepSeek")
    print("3 - Gemma")
    print("4 - Qwen")
    print("5 - Exit")

    choice = input("\nSelect mission: ")

    if choice == "5":
        print("\nNavigator standing by.")
        break

    if choice not in models:
        print("Invalid choice. Try again.")
        continue

    prompt = input("\nAsk your question: ")

    print("\n--- Response ---\n")

    subprocess.run([
        "ollama",
        "run",
        models[choice],
        prompt
    ])