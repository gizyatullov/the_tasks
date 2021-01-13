a = int(input('Целое положительное число '))
max_a = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > max_a:
        max_a = a % 10
    if a > 9:
        continue
    else:
        print(f'Самая большая цифра в числе:', max_a)
        break
#