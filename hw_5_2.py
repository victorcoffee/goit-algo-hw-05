# Модуль 5. Завдання 2

import os, re
from typing import Callable

os.system("cls")


# Генератор чисел з тексту
def generator_numbers(text: str) -> Callable:
    pattern = r"\d*\.\d+"
    matches = re.findall(pattern, text)
    for number in matches:
        yield number


# Функція для знаходження підсумку всіх дійсних чисел у тексті
def sum_profit(text: str, func: Callable):
    sum = 0
    for x in generator_numbers(text):
        sum += float(x)
    return sum


# Основна програма
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний\
дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
