# Модуль 5. Завдання 3

import os
import sys
import collections
from pathlib import Path
from collections import defaultdict


def main():
    os.system("cls")

    # Варіанти запуску з командного рядка
    # Командний рядок 1: python hw_5_3.py logfile.log
    # Командний рядок 2: python hw_5_3.py logfile.log error
    # Командний рядок 3: python hw_5_3.py bad_logfile.log error

    file_path = sys.argv[1]
    logs = load_logs(file_path)  # Завантаження логів з файлу "logfile.log"
    print("Аналізуємо: ", file_path)
    print()

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # Якщо є 2 параметр рядка виведення детально по рівню
    if len(sys.argv) > 2:
        level = sys.argv[2]
        level = level.upper()
        print(f"\nДеталі логів для рівня '{level}':")
        filtered_logs = filter_logs_by_level(logs, level)
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")

    print("\nПрограма завершена")


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

    except FileNotFoundError:
        print("Помилка: файл не знайдено")

    except PermissionError:
        print("Помилка: в доступі до файлу відмовлено")

    except Exception as e:
        print(f"Помилка: {e}")

    return new_lines


# Функція парсінгу логів
def parse_log_line(line: str) -> dict:

    dict = {}
    # Зразок логу: 2024-01-22 08:30:01 INFO User logged in successfully.
    words = line.split(maxsplit=3)
    dict["date"] = words[0]
    dict["time"] = words[1]
    dict["level"] = words[2]
    dict["message"] = words[3].strip()

    # Варіант парсінгу з перевіркою коректності логів
    # Поки не реалізовано

    return dict


# Не використовується
def is_level(log: dict, level: str) -> bool:
    print(log["level"] == level)
    return log["level"] == level


# Функція фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_logs = []

    # Варіант з List Comprehesion
    # filtered_logs = [log for log in logs if log["level"] == level]

    # Варіант з filter і lambda
    filtered_logs = list(filter(lambda log: log["level"] == level, logs))

    return filtered_logs


# Функція для підрахунку записів за рівнем логування
def count_logs_by_level(logs: list) -> dict:
    levels = []
    dict = defaultdict(str)

    # Створення словника з логів за ключами-рівнями
    for log in logs:
        dict[log["level"]] = log
        levels.append(log["level"])

    group_level = collections.Counter(levels)

    return group_level


# Функція для виведення результатів
def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for key, value in counts.items():
        print(f"{key:16} | {value:5}")

    return


if __name__ == "__main__":
    main()
