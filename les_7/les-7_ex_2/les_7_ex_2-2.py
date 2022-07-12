import os
import yaml
from yaml.loader import SafeLoader
data_list = []
with open('test.yaml', 'r', encoding='utf-8') as file:
    data_dict = yaml.load(file, Loader=SafeLoader)
    for value in data_dict.values():
        data_list.append(value)
s_dir = os.path.join(data_list[0], data_list[1])
if not os.path.exists(s_dir):
    os.makedirs(s_dir)
    for file in data_list[1:]:
        s_dir = os.path.join(data_list[0] + '/' + file)
        if os.path.exists(s_dir):
            continue
        elif not os.path.exists(s_dir):
            os.makedirs(s_dir)