"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи
— верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей
(начинаем с 0), например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import os
from os.path import relpath
root_folder = './my_project'

count_n1 = 0
count_n10 = 0
count_n100 = 0
count_n1000 = 0
info_dict = {}

for root, dirs, files in os.walk(root_folder):
    for file in files:
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        rel_path = relpath(os.path.join(root, file), root_folder)
        rp = os.path.join(root_folder, rel_path)
        print(rp)
        st = os.stat(rp)
        inf = int('{s}'.format(s=st.st_size))
        if 0 <= inf <= 10:
            count_n1 += 1
            n1_dict = {1: count_n1}
            info_dict.update(n1_dict)
        elif 10 <= inf <= 100:
            count_n10 += 1
            n10_dict = {10: count_n10}
            info_dict.update(n10_dict)
        elif 100 <= inf <= 1000:
            count_n100 += 1
            n100_dict = {100: count_n100}
            info_dict.update(n100_dict)
        elif 1000 <= inf <= 10000:
            count_n100 += 1
            n1000_dict = {1000: count_n1000}
            info_dict.update(n1000_dict)
print(info_dict)
