"""
1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:

odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
"""

def gen_odd_num(num):
    """
    Генератор. Возвращает нечетные
    числа от 1 до "n" включительно
    """
    for n in range(1, num+1, 2):
        yield n

some_num = gen_odd_num(11)
print(next(some_num))
print(next(some_num))
print(next(some_num))
print(next(some_num))
print(next(some_num))
print(next(some_num))

"""
2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), 
не используя ключевое слово yield.
"""

num = 9
odd_to_num = (n for n in range(1, num+1, 2))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))
print(next(odd_to_num))


"""
3. Есть два списка:

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:

('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке 
klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: 
(<tutor>, None), например:

('Станислав', None)
### Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. 
Подумать, в каких ситуациях генератор даст эффект. 
"""

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]

def gen_some_list(a_list, b_list):
    a = (tutor for tutor in a_list)
    b = (klass for klass in b_list)
    while True:
        try:
            c = (next(a), next(b))
            yield c
        except StopIteration:
            c = (next(a), None)
            yield c
m = gen_some_list(tutors, klasses)
print(type(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

"""
### 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
```
Подсказка: использовать возможности python, изученные на уроке.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
nums_src = (n for n in src)
nums_res = (i for i in src)
b = next(nums_res)
f = True
while f:
    try:
        a = (next(nums_src))
        b = (next(nums_res))
        if a < b:
            result.append(b)
    except StopIteration:
        break
print(result)

"""
5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.

Представлен список чисел. Определить элементы списка, не имеющие повторений. 
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_set = set()
sup = set()
for num in src:
    if num not in sup:
        result_set.add(num)
    else:
        result_set.discard(num)
    sup.add(num)
result = [num for num in src if num in result_set]
print(result)