from datetime import datetime
def log_mission(choice, prompt, models):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logs/mission_log.txt", "a", encoding="utf-8") as log:
        log.write("=" * 50 + "\n")
        log.write(f"Mission Time : {timestamp}\n")
        log.write(f"Model        : {models[choice]}\n")
        log.write(f"Question     : {prompt}\n\n")