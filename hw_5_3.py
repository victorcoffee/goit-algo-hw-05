# Модуль 5. Завдання 3
import os
import sys
import collections
from pathlib import Path
from collections import defaultdict


def main(*args, **kwargs):
    os.system("cls")

    # # Командний рядок 1: python hw_5_3.py logfile.log
    # # Командний рядок 2: python hw_5_3.py logfile.log error
    # # Командний рядок ?: python main.py logfile.log error

    file_path = sys.argv[1]
    print("file_path:", file_path)
    logs = load_logs(file_path)  # Завантаження логів з файлу "logfile.log"
    # print("logs:", logs)

    counter = count_logs_by_level(logs)
    print(counter)

    # Якщо є 2 параметр
    if len(sys.argv) > 2:
        level = sys.argv[2]
        level = level.upper()
        print("level:", level)
        filtered_logs = filter_logs_by_level(logs, level)
        print("filtered_logs:", filtered_logs)

    print("Програма завершена")


def load_logs(file_path: str) -> list:
    lines = []
    new_lines = []
    try:
        path = Path(file_path)
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                parse_line = parse_log_line(line)
                new_lines.append(parse_line)
                # new_line = " ".join(parse_line.values())
                # print(new_line)

    except FileNotFoundError:
        print("Помилка File Not Found")

    except Exception as e:
        print(f"Помилка {e}")

    return new_lines


def parse_log_line(line: str) -> dict:

    dict = {}
    # Зразок логу: 2024-01-22 08:30:01 INFO User logged in successfully.
    words = line.split(maxsplit=3)
    dict["date"] = words[0]
    dict["time"] = words[1]
    dict["level"] = words[2]
    dict["message"] = words[3].strip()

    return dict


def is_level(log: dict, level: str) -> bool:
    print(log["level"] == level)
    return log["level"] == level


# В роботі
# Командний рядок 2: python hw_5_3.py logfile.log error
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []

    # Варіант через цикл. Працює
    # for log in logs:
    #     if log["level"] == level:
    #         filtered_logs.append(log)

    # Варіант через List Comprehesion. Працює
    filtered_logs = [log for log in logs if log["level"] == level]

    # Не працює <filter object at 0x000002BBB4DF3BB0>
    # filtered_logs = filter(lambda log: log["level"] == level, logs)

    # Не працює
    # filtered_logs = filter(is_level(logs, level), logs)

    print(filtered_logs)

    return filtered_logs


# Працюючий варіант. Прибрати зайвий код і debugging code
# Командний рядок 2: python hw_5_3.py logfile.log error


def count_logs_by_level(logs: list) -> dict:
    levels = []
    dict = defaultdict(str)
    count_log = 0
    # count_log_info = 0

    for log in logs:
        count_log += 1
        dict[log["level"]] = log
        levels.append(log["level"])

        # if log["level"] == "INFO":
        #     count_log_info += 1
        #     print("log:", count_log_info, log)

    # Debugging code

    # print("dict.keys:", dict.keys())
    # print("levels:", levels)
    # print("count_log:", count_log)
    # print("count_log_info:", count_log_info)

    group_level = collections.Counter(levels)
    # print(group_level)

    return group_level


def display_log_counts(counts: dict):
    pass


if __name__ == "__main__":
    main()
