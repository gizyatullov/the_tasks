'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def self(*a):
    try:
        a = int(input('Первое число '))
        b = int(input('Второе число '))
        outcome = a / b
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return 'Ошибка!!! На ноль делить нельзя!!!'
    return outcome


print(f'{self()}')