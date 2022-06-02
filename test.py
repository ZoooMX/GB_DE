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
