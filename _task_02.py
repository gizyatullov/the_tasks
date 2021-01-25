'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''

name = input('enter name ')
surname = input('enter surname ')
year = int(input('enter year '))
city = input('enter city ')
email = input('enter email ')
telephone = input('input telephone ')

def task(name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(task)