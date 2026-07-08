import subprocess


def run_ai(model, prompt):
    print("\n--- Response ---\n")
    print("DEBUG: About to run Ollama...")

    subprocess.run([
        "ollama",
        "run",
        model,
        prompt
    ])