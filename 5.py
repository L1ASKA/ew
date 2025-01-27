'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать
программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы 
применимости рекурсивного и итеративного подхода. Результаты сравнительного исследования 
времени вычисления представить в табличной форме. Обязательное требование – минимизация времени 
выполнения и объема памяти. 
4.F(n<2) = 3; F(n) = (-1)^n * (F(n-1)/n! + F(n-5)/(2n)!)'''
from math import factorial
import timeit
fact1, fact2 = 1,2
n=input('Введите натуральное число n < 996 и n > 0: ')
while True:
    try: n = int(n)
    except: n = input('Вы неправильно ввели n. Введите натуральное число n < 996 и n > 0: ')
    else: 
        if n<996 and n>0: break
        else: n = input('Вы неправильно ввели n. Введите натуральное число n < 996 и n > 0: ')
def st1(n):
    if n%2==0: return 1
    else: return -1
def recursive_f(n):
    if n < 2 : return st1(n)*3  
    else: return -(recursive_f(n - 1) / factorial(n) + recursive_f(n - 5) / factorial(2 * n) if n > 5 else 0)    
def iterative_f(n, fact1,fact2):    
    if n < 2: return 3
    f = [3] * n  # Массив для хранения значений
    for i in range(2, n + 1):
        fact1 *=i 
        fact2 *= (i*2) * ((i*2)-1)
        f[i-1] = -(f[i - 2] / fact1 + f[i - 6] / fact2 if i > 5 else 0)
    return -f[n-1]
def compare_methods(n):
    print(f"n: {n}")
    a = timeit.timeit('recursive_f(n)', globals = globals(), number =1)
    print(f'Рекурсивный результат: {recursive_f(n)} \nВремя рекурсивного вычисления: {a}')
    a = timeit.timeit('iterative_f(n, fact1, fact2)', globals = globals(), number =1)
    print(f'Итерационный результат: {iterative_f(n, fact1,fact2)} \nВремя итерационного вычисления: {a}')
compare_methods(n)