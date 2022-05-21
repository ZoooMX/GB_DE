"""
1. Выяснить тип результата выражений:

15 * 3
15 / 3
15 // 2
15 ** 2
"""

a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2
print(type(a), type(b), type(c), type(d))



"""
2. Дан список:

['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
(добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до 
двух целочисленных разрядов:

['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"',
 '+05', '"', 'градусов']
 
Сформировать из обработанного списка строку:

в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать
 это условие для чисел со знаком?

Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации 
позже. Главное: дополнить числа до двух разрядов нулём!
"""

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
update_lst = []

a_lst = lst.index('5')
lst.insert(a_lst, '"')
b_lst = lst.index('часов')
lst.insert(b_lst, '"')
c_lst = lst.index('17')
lst.insert(c_lst, '"')
d_lst = lst.index('минут')
lst.insert(d_lst, '"')
e_lst = lst.index('+5')
lst.insert(e_lst, '"')
f_lst = lst.index('градусов')
lst.insert(f_lst, '"')

for item in lst:
    if item == '5':
        update_lst.append('05')
    elif item == '+5':
        update_lst.append('+05')
    else:
        update_lst.append(item)

message_a = ' '.join(update_lst[0:2])
message_b = ' '.join(update_lst[3:6])
message_c = ' '.join(update_lst[7:13])
message_d = ' '.join(update_lst[14:15])
for up_item in update_lst:
    if up_item == '05':
        first_item = up_item
    elif up_item == '17':
        second_item = up_item
    elif up_item == '+05':
        third_item = up_item
print(message_a + first_item + message_b + second_item + message_c + third_item + message_d)



"""
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). 
Эта задача намного серьёзнее, чем может сначала показаться.
"""

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a_lst = lst.index('5')
lst.insert(a_lst, '"')
b_lst = lst.index('часов')
lst.insert(b_lst, '"')
c_lst = lst.index('17')
lst.insert(c_lst, '"')
d_lst = lst.index('минут')
lst.insert(d_lst, '"')
e_lst = lst.index('+5')
lst.insert(e_lst, '"')
f_lst = lst.index('градусов')
lst.insert(f_lst, '"')

for item_lst in lst:
    if item_lst == '5':
        a_lst = lst.index('5')
        lst.insert(a_lst, '05')
        a_lst += 1
        lst.pop(a_lst)
    elif item_lst == '+5':
        e_lst = lst.index('+5')
        lst.insert(e_lst, '+05')
        e_lst += 1
        lst.pop(e_lst)

message_a = ' '.join(lst[0:2])
message_b = ' '.join(lst[3:6])
message_c = ' '.join(lst[7:13])
message_d = ' '.join(lst[14:15])
for up_item in lst:
    if up_item == '05':
        first_item = up_item
    elif up_item == '17':
        second_item = up_item
    elif up_item == '+05':
        third_item = up_item
print(message_a + first_item + message_b + second_item + message_c + third_item + message_d)


"""
4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:

['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!' 
Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при 
этом не создавать новый список?
"""

inf_ppl = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for inf in inf_ppl:
    inf_hum = inf.split(' ')
    name = inf_hum.pop(-1)
    print('Привет ' + name.title() + '!') # приветствие по имени из списка inf_ppl



"""
5. Создать список, содержащий цены на товары (10–20 товаров), например:

[57.8, 46.51, 97, ...]

Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп 
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, 
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки 
остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

prices = [57.8, 46.51, 97, 7, 12.3, 14.02, 60.1, 99.99]
print('Проверка изменений: ')
print(prices)
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

print('\nПриведение списка к общему виду цен:')
for price in prices:
    pr = str(price).split('.')
    rub = pr.pop(0)
    if len(pr) == 1:
        kop = pr.pop(0)
        if len(kop) == 1:
            kop = kop + '0'
    else:
        kop = '00'
    print(rub + ' руб ' + kop + ' коп ')

#============================================================

rev_prices = prices[:] # Работа по заданию с новым спиком
print('\nПроверка изменений при копировании: ')
print(prices)
print(id(prices))
rev_prices.reverse()
print(rev_prices)
print(id(rev_prices))

print('\nПриведение 5 самих высоких цен \nсписка к общему виду цен:')
count = 0
for rev_price in rev_prices:
    r_pr = str(rev_price).split('.')
    rub = r_pr.pop(0)
    count += 1
    if count == 6:
        break
    if len(r_pr) == 1:
        kop = r_pr.pop(0)
        if len(kop) == 1:
            kop = kop + '0'
    else:
        kop = '00'
    print(rub + ' руб ' + kop + ' коп ')



