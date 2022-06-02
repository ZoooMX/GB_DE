"""
1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл
логов web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
"""
final_list = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f_file:
    reading = f_file.readline()
    while reading:
        s = []
        addr_idx = reading.find(' ')
        remote_addr = reading[0: addr_idx] # remote_addr
        req_idx_1 = reading.find('G')
        req_idx_2 = reading.find('T') + 1
        request_type = reading[req_idx_1:req_idx_2] # request_type
        rr_idx_1 = reading.find('T') + 2
        rr_idx_2 = reading.find('H') - 1
        requested_resource = reading[rr_idx_1:rr_idx_2] # requested_resource
        s.append(remote_addr)
        s.append(request_type)
        s.append(requested_resource)
        s = tuple(s)
        final_list.append(tuple(s))
        reading = f_file.readline()
print(final_list)


"""
2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла 
логов из предыдущего задания.

Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с 
файлами, размер которых превышает объем ОЗУ компьютера.
"""

final_list = []

with open('nginx_logs.txt', 'r', encoding='utf-8') as f_file:
    reading = f_file.readline()
    while reading:
        addr_idx = reading.find(' ')
        remote_addr = reading[0: addr_idx] # remote_addr
        final_list.append(remote_addr)
        reading = f_file.readline()

from collections import Counter
c = Counter(final_list)
m = 0
for value in c.values():
    if value > m:
        m = value
for key, value in c.items():
    if m == value:
        print(key)

"""
3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель 
между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них 
словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые 
данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре 
значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём 
данных в файлах во много раз меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""

import sys

dict_f = {}
user = []
hobby = []

with open('users.csv', 'r', encoding='utf-8-sig') as u_file:
    r_user = u_file.readline()
    while r_user:
        user_idx = r_user.find(' ')-1
        r_u = r_user[0: user_idx]
        user.append(r_u)
        r_user = u_file.readline()
    # print(user)

with open('hobby.csv', 'r', encoding='utf-8-sig') as h_file:
    r_hobby = h_file.readline().replace('\n', '').replace('\r', '')
    while r_hobby:
        hobby.append(r_hobby)
        r_hobby = h_file.readline().replace('\n', '').replace('\r', '')
    # print(hobby)
y = True
while y:
    try:
        some_dict = {user.pop(): hobby.pop()}
        dict_f.update(some_dict)
    except IndexError:
        try:
            some_dict = {'None': hobby.pop()}
            dict_f.update(some_dict)
        except IndexError:
            sys.exit(1)

with open('dict_user_hobby.txt', 'w', encoding='utf-8') as f_file:
    for key, value in dict_f.items():
        f_file.write(f'{key}- {value}\n')
with open('dict_user_hobby.txt', 'r', encoding='utf-8') as f_file:
    reading = f_file.read()
    print(reading)


"""
4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ 
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для 
пользователей и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, 
кортеж, множество, словарь). Обосновать выбор типа. Подумать, какие могут возникнуть проблемы 
при парсинге. В словаре должны храниться данные, полученные в результате парсинга.
"""

dict_f = {}
user = []
hobby = []
with open('users.csv', 'r', encoding='utf-8-sig') as u_file:
    r_user = u_file.readline().replace('\n', '').replace('\r', '')
    lst_user = r_user.split(',')
    t_user = (*lst_user,) # преобразовывание в кортеж - (экономим память)
    while r_user:
        user.append(t_user)
        r_user = u_file.readline().replace('\n', '').replace('\r', '')
        lst_user = r_user.split(',')
        t_user = (*lst_user,)
    print(user)
    print(type(user))

with open('hobby.csv', 'r', encoding='utf-8-sig') as h_file:
    r_hobby = h_file.readline().replace('\n', '').replace('\r', '')
    lst_hobby = r_hobby.split(',')
    t_hobby = (*lst_hobby,) # преобразовывание в кортеж - (экономим память)
    while r_hobby:
        hobby.append(t_hobby)
        r_hobby = h_file.readline().replace('\n', '').replace('\r', '')
        lst_hobby = r_hobby.split(',')
        t_hobby = (*lst_hobby,)
    print(hobby)
    print(type(hobby))

y = True
while y:
    try:
        some_dict = {user.pop(): hobby.pop()}
        dict_f.update(some_dict)
    except IndexError:
        try:
            some_dict = {'None': hobby.pop()}
            dict_f.update(some_dict)
        except IndexError:
            some_dict = {user.pop(): 'None'}
            dict_f.update(some_dict)
        y = False
print(dict_f)

with open('dict_user_hobby2.txt', 'w', encoding='utf-8') as f_file:
    for key, value in dict_f.items():
        f_file.write(f'{key}- {value}\n')
with open('dict_user_hobby2.txt', 'r', encoding='utf-8') as f_file:
    reading = f_file.read()
    print(reading)

"""
5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было 
задать путь к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу 
скрипта для случая, когда все файлы находятся в разных папках.
"""

"""
Отдельно запустил скрипт как "test.py" и результат в скриншоте les_6_ex_5.jpg
"""
dict_f = {}
user = []
hobby = []

u = input('Путь к файлу user: ')
h = input('Путь к файлу hobby: ')
with open(u, 'r', encoding='utf-8-sig') as u_file:
    r_user = u_file.readline()
    while r_user:
        user_idx = r_user.find(' ')-1
        r_u = r_user[0: user_idx]
        user.append(r_u)
        r_user = u_file.readline()

with open(h, 'r', encoding='utf-8-sig') as h_file:
    r_hobby = h_file.readline().replace('\n', '').replace('\r', '')
    while r_hobby:
        hobby.append(r_hobby)
        r_hobby = h_file.readline().replace('\n', '').replace('\r', '')

y = True
while y:
    try:
        some_dict = {user.pop(): hobby.pop()}
        dict_f.update(some_dict)
    except IndexError:
        try:
            some_dict = {'None': hobby.pop()}
            dict_f.update(some_dict)
        except IndexError:
            some_dict = {user.pop(): 'None'}
            dict_f.update(some_dict)
        y = False

dict_user_hobby = input('Введите путь и имя файла для сохранения: ')
print('\nпуть к файлу: ' + dict_user_hobby)
with open(dict_user_hobby, 'w', encoding='utf-8') as f_file:
    for key, value in dict_f.items():
        f_file.write(f'{key}- {value}\n')
with open(dict_user_hobby, 'r', encoding='utf-8') as f_file:
    reading = f_file.read()
    print('\nСодержание созданного файла: \n' + reading)

"""
6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два 
скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных 
данных. При записи передавать из командной строки значение суммы продаж. Для чтения данных 
реализовать в командной строке следующую логику:

просто запуск скрипта — выводить все записи;
запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, 
равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.

Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. 
Примеры запуска скриптов:

python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
"""


# скрипт les_6_ex_6-1.py - запись данных в файл
# скрипт les_6_ex_6-2.py - чтение данных с файла


"""
7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта: 
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — 
обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи, 
которой не существует.
"""

# отстал от группы, пока оставил на потом
