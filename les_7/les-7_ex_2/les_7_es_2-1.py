import yaml
name_dict = {
    1: 'my_project',
    2: 'settings',
    3: 'mainapp',
    4: 'adminapp',
    5: 'authapp'
}
# yml_doc = yaml.dump(name_dict)
# print(yml_doc)

# открываем файл на запись
with open('test.yaml', 'w') as fw:
    # сериализуем словарь `user` в формат YAML
    # и записываем все в файл `test.yaml`
    data = yaml.dump(name_dict, fw, sort_keys=False,
                     default_flow_style=False)