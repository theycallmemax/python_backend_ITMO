# Кэш для функций факториала и Фибоначчи
factorial_cache = {}
fibonacci_cache = {}


# функция для вычисления факториала
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('Negative number')

    # Проверка, есть ли значение в кэше
    if n in factorial_cache:
        return factorial_cache[n]

    if n == 0:
        return 1

    result = n * factorial(n - 1)
    # Сохраняем результат в кэш
    factorial_cache[n] = result
    return result


# Функция вычисляет n-е число Фибоначчи
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('Negative number')

    # Проверка, есть ли значение в кэше
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        # Кэшируем результат
        fibonacci_cache[n] = result
        return result


# Функция возвращает среднее значение списка чисел
def mean_value(numbers: list) -> float:
    return sum(numbers) / len(numbers)
