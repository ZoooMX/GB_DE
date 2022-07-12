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

import sys

f_dict = {}
with open('all_sales_amount.txt', 'r', encoding='utf-8') as file_w:
    inf = file_w.readline().replace('\n', '')
    count = 1
    while inf:
        some_dict = {count: inf}
        f_dict.update(some_dict)
        inf = file_w.readline().replace('\n', '')
        count += 1


if len(sys.argv) == 2:
    x = sys.argv[1]
    a = int(x)
    for key, value in f_dict.items():
        if key >= a:
            print(value)
elif len(sys.argv) == 3:
    x = sys.argv[1]
    y = sys.argv[2]
    a = int(x)
    b = int(y)
    for key, value in f_dict.items():
        if key >= a and key <= b:
            print(value)
else:
    with open('all_sales_amount.txt', 'r', encoding='utf-8') as file_e:
        e = file_e.read()
        print(e)
