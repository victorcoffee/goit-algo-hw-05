# Модуль 5. Завдання 1

from typing import Callable


def caching_fibonacci(n: int) -> Callable([[int], int]):
    cach = {}

    def fibonacci(n: int) -> int:
        # nonlocal cach

        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        elif n in cach:
            result = cach[n]
        else:
            result = fibonacci(n - 2) + fibonacci(n - 1)
            cach[n] = result
        return result

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
