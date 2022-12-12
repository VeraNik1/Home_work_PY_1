# Задача 2
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
#способ 1
while True:  
    try:
        num = int(input("Введите трехзначное число: "))
        if 99 < num < 1000:
            print(f'сумма цифр трехзначного числа равна: {num // 100 + num // 10 % 10  + num % 10}')
            break
        else: print('Вы ввели не трехзначное число, попробуйте еще раз)')
    except:
        print('Вы ввели не трехзначное число, попробуйте еще раз)')
#способ 2
while True:  
    num2 = input("Введите трехзначное число: ")
    if num2.isdigit() and 99 < int(num2) < 1000: #второе условие выбрано не через длину строки, чтобы исключить из трезначных чисел данные 001, 055 и т.д. 
        print(f'сумма цифр трехзначного числа равна: {int(num2[0]) + int(num2[1]) + int(num2[2])}')
        break
    else: print('Вы ввели не трехзначное число, попробуйте еще раз)')

# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
while True:
    try:
        S = int(input("Введите общее количество журавликов:"))
        if not S % 6:
            x = S // 6
            print(f'Петя, Катя и Сережа сделали {x}, {x * 4}, {x} журавликов соответственно')
        else:
            print('Введенное число не соответствует условиям задачи')
        break
    except:
        print('Вы ввели не число, попробуйте еще раз')

# Задача 6
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no
while True:
    number = input('Введите шестизначный номер Вашего билета: ')
    if number.isdigit() and len(number) == 6:
        if sum(map(int, number[:3])) == sum(map(int, number[3:])):
            print('Ура, Ваш билет счастливый!')
        else:
            print('Увы, Ваш билет не счастливый(')
        break
    else:
        print('Введен некорректный номер билета, попробуйте еще раз)')

# Задача 8
# Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите один размер шоколадки в дольках: "))
m = int(input("Введите другой размер шоколадки в дольках: "))

k = int(input("Введите количество долек, которое хотите отломить: "))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Да')
else:
    print('Нет')