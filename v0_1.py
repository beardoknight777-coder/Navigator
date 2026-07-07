import subprocess

print("=" * 40)
print("      NAVIGATOR v0.1")
print("=" * 40)
print()

models = {
    "1": "llama3.2:3b", 
    "2": "deepseek-r1:7b",
    "3": "gemma3:4b",
    "4": "qwen3:4b"
}

print("Choose your AI:")
print("1 - Llama")
print("2 - DeepSeek")
print("3 - Gemma")
print("4 - Qwen")

choice = input("\nSelection: ")

if choice not in models:
    print("Invalid choice.")
    exit()

prompt = input("Ask your question: ")

subprocess.run([
    "ollama",
    "run",
    models[choice],
    prompt
])