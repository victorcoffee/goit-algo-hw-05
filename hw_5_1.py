# Модуль 5. Завдання 1

import os

os.system("cls")


# Функція обчислення заданого числа Фібоначчі з кешуванням
def caching_fibonacci(n: int) -> int:
    cache = {}

    # Рекурсивна функція з кешуванням
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n]= fibonacci(n - 2) + fibonacci(n - 1)
            return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci(int)

# Використовуємо функцію fibonacci 
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
