from math import factorial
import timeit
'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать
программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы 
применимости рекурсивного и итеративного подхода. Результаты сравнительного исследования 
времени вычисления представить в табличной форме. Обязательное требование – минимизация времени 
выполнения и объема памяти. 
4.F(X<2)=3,F(n)=(-1)h*(F(n-1)/n!+-F(n-2)/(2n)!)'''
# Функция для определения знака (-1)^n
def st1(n):
    return -1 if n % 2 else 1

# Рекурсивная реализация функции
def recursive_f(n):
    if n < 2:
        return 3
    return st1(n) * (
        recursive_f(n - 1) / factorial(n) - recursive_f(n - 2) / factorial(2 * n)
    )

# Итеративная реализация функции
def iterative_f(n):
    if n < 2:
        return 3

    f = [3] * (n + 1)  # Массив для хранения значений

    fact_n = 1  # Хранение факториала n!
    fact_2n = 2  # Хранение факториала (2n)!

    for i in range(2, n + 1):
        fact_n *= i
        fact_2n *= 2 * i * (2 * i - 1) if i > 1 else 2

        f[i] = st1(i) * (f[i - 1] / fact_n - f[i - 2] / fact_2n)

    return f[n]

# Функция для сравнения методов и замера времени выполнения
def compare_methods(n):
    print(f"n: {n}")

    # Рекурсивный метод
    recursive_start = timeit.default_timer()
    recursive_result = recursive_f(n)
    recursive_time = timeit.default_timer() - recursive_start
    print(f"Рекурсивный результат: {recursive_result}")
    print(f"Время рекурсивного вычисления: {recursive_time:.6f} секунд")

    # Итеративный метод
    iterative_start = timeit.default_timer()
    iterative_result = iterative_f(n)
    iterative_time = timeit.default_timer() - iterative_start
    print(f"Итерационный результат: {iterative_result}")
    print(f"Время итерационного вычисления: {iterative_time:.6f} секунд")

# Основная программа
while True:
    try:
        n = int(input("Введите натуральное число n (n > 0): "))
        if n > 0:
            break
    except ValueError:
        pass
    print("Некорректный ввод. Попробуйте снова.")

compare_methods(n)
