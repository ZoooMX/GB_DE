"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше
хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный
проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах
(добавлять детали)?
"""

import os
names_dir = []
with open('name_dir.csv', 'r', encoding='utf-8-sig') as files:

    some_files = files.readline()
    while some_files:
        x = some_files.find(' ')
        s_f = some_files[0: x]
        names_dir.append(s_f)
        some_files = files.readline()
    s_dir = os.path.join(names_dir[0], names_dir[1])
    if not os.path.exists(s_dir):
        os.makedirs(s_dir)
        for file in names_dir[1:]:
            s_dir = os.path.join(names_dir[0] + '/' + file)
            if os.path.exists(s_dir):
                continue
            elif not os.path.exists(s_dir):
                os.makedirs(s_dir)

folder = './'
l_dir1 = [item
          for item in os.listdir(folder)
          if os.path.isdir(os.path.join(folder, item))
          ]
for dir1 in l_dir1:
    if dir1 == names_dir[0]:
        l_dir2 = [os.path.join(dir1, item)
                  for item in os.listdir(dir1)
                  if os.path.isdir(os.path.join(dir1, item))
                  ]
        f_dir2= [os.path.join(dir1, item)
                 for item in os.listdir(dir1)
                 ]
        if f_dir2 != []:
            print(f_dir2)
        for dir2 in l_dir2:
            l_dir3 = [os.path.join(dir2, item)
                      for item in os.listdir(dir2)
                      if os.path.isdir(os.path.join(dir2, item))
                      ]
            f_dir3 = [os.path.join(dir2, item)
                      for item in os.listdir(dir2)
                      ]
            if f_dir3 != []:
                print(f_dir3)

