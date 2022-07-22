"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками»
в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены
в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные
ситуации; это реальная задача, которая решена, например, во фреймворке django.
"""
import os
import shutil

dir_name = 'templates'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

all_folders = []

root_folder = './my_project'
f_files = [os.path.join(root_folder, item)
           for item in os.listdir(root_folder)
           if os.path.isdir(os.path.join(root_folder, item))
           ]
# print(f_files)
for dirs in f_files:
    f_files = [os.path.join(dirs, item)
               for item in os.listdir(dirs)
               if os.path.isdir(os.path.join(dirs, item))
               ]
    if f_files != []:
        # print(f_files)
        for dirs in f_files:
            h_files = [os.path.join(dirs, item)
                       for item in os.listdir(dirs)
                       if item.lower().endswith('.html')
                       ]
            if h_files != []:
                all_folders.append(h_files)
            f_files = [os.path.join(dirs, item)
                       for item in os.listdir(dirs)
                       if os.path.isdir(os.path.join(dirs, item))
                       ]
            if f_files != []:
                # print(f_files)
                for dirs in f_files:
                    h_files = [os.path.join(dirs, item)
                               for item in os.listdir(dirs)
                               if item.lower().endswith('.html')
                               ]
                    # print(os.path.basename(os.path.dirname('index.html')))
                    if h_files != []:
                        all_folders.append(h_files)
                    f_files = [os.path.join(dirs, item)
                               for item in os.listdir(dirs)
                               if os.path.isdir(os.path.join(dirs, item))
                               ]


def copy_file(full_dir):
    """
    Принимает полный путь к файлу
    и возвращаетя копию в отдельную папку: dir_name/b_dir/file
    """
    a_dir = os.path.dirname(full_dir)
    a_dir = os.path.split(a_dir)[-0]
    a_dir = os.path.split(a_dir)[-0]
    b_dir = os.path.split(a_dir)[-1]
    new_dir = os.path.join(dir_name, b_dir)
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
    return shutil.copy2(full_dir, new_dir)


for all_f in all_folders:
    for full_forder in all_f:
        copy_file(full_forder)
