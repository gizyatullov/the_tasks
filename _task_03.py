'''
Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.
'''
def self(a, b, c):
    if a >= b and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c