"""
1. Реализовать вывод информации о промежутке времени
в зависимости от его родолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = 53
print('duration = ' + str(duration))
print(str(duration) + ' sec\n')

duration = 153
print('duration = ' + str(duration))
m = (duration // 60)
s = (duration % 60)
print(str(m) + ' min ' + str(s) + ' sec\n')

duration = 4153
print('duration = ' + str(duration))
h = duration // 3600
m = (duration - 3600) // 60
s = (duration - 3600) % 60
print(str(h) + ' hour ' +
      str(m) + ' min ' +
      str(s) + ' sec\n')

duration = 400153
print('duration = ' + str(duration))
d = duration // 86400
h = (duration - 86400 * d) // 3600
m = (duration - (86400 * d) - (3600 * h)) // 60
s = (duration - (86400 * d) - (3600 * h)) % 60
print(str(d) + ' day ' +
      str(h) + ' hour ' +
      str(m) + ' min ' +
      str(s) + ' sec\n')

#============================================================

min = 60
hour = 3600
day = 86400

some_time = [53, 153, 4153, 400153]
print('\nsome_time: ' + str(some_time))
for duration in some_time:
    """Перебор списка по условиям"""
    if duration <= min:
        print('duration from some_time = ' + str(duration))
        d_sec = duration % min
        print(str(d_sec) + ' sec\n')
    elif duration > min and duration <= hour:
        print('duration from some_time = ' + str(duration))
        d_min = duration // min
        d_sec = (duration - (d_min * min)) % min
        print(str(d_min) + ' min ' + str(d_sec) + ' sec\n')
    elif duration > min and duration <= day:
        print('duration from some_time = ' + str(duration))
        d_hour = duration // hour
        d_min = (duration - (d_hour * hour)) // min
        d_sec = (duration - ((d_hour * hour) + (d_min * min))) % min
        print(str(d_hour) + ' hour ' + str(d_min) + ' min ' + str(d_sec) + ' sec\n')
    elif duration >= day:
        print('duration from some_time = ' + str(duration))
        d_day = duration // day
        d_hour = (duration - (d_day * day)) // hour
        d_min = (duration - ((d_day * day) + (d_hour * hour))) // min
        d_sec = (duration - ((d_day * day) + (d_hour * hour) + (d_min * min))) % min
        print(str(d_day) + ' day ' + str(d_hour) + ' hour ' + str(d_min) + ' min ' + str(d_sec) + ' sec\n')



""" 
2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 
(куб X - третья степень числа X):

a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится 
нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так 
как 6 + 8 +5+9=28– делится нацело на 7. Внимание: использовать только 
арифметические операции!

b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел 
из этого списка, сумма цифр которых делится нацело на 7.

c. * Решить задачу под пунктом b, не создавая новый список.
"""

num_cube = []
finish = []
for num_range in range(1, 1000, 2):
    num_odd = num_range + 17 # - условие d., c.
    num_cube.append(num_odd ** 3)

def sum_digits(numer): # с использованием функции - условие a.
    """Возращает значение суммы цифр числа"""
    digit = 0
    while numer != 0:
        digit += numer % 10
        numer = numer // 10
    return digit

for num in num_cube:
    sum_num = sum_digits(num)
    true_num = sum_num % 7
    if true_num == 0:
        finish.append(sum_num)
print('This is result Ex.2: \n' + str(finish))

# ================================================================

for num in num_cube: # без использования функции - условие a.
    digit = 0
    while num > 0:
        digit += num % 10
        num = num // 10
    # print(digit)
    true_num = digit % 7
    if true_num == 0:
        finish.append(digit)
print('This is result Ex.2: \n' + str(finish))


"""
3. Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из
чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
Задачи со * предназначены для продвинутых учеников, которым мало
сделать обычное задание. Пробуйте их решать, если уверены в своих
силах.
"""

full_perсent = []
for percent in range(1, 101):
    full_perсent.append(percent)
for n in full_perсent:
    if n % 10 == 1 and n != 11:
        print(str(n) + ' процент')
    elif n > 1 and n < 5 or n > 21 and n < 25 or n > 30 and n < 35 or n> 40 and n < 45\
        or n > 50 and n < 55 or n > 60 and n < 65 or n > 70 and n < 75 or n > 80 and n < 85\
        or n > 90 and n < 95:
        print(str(n) + ' процента')
    else:
        print(str(n) + ' процентов')

