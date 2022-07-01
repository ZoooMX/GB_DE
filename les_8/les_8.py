"""1. Написать функцию email_parse(<email_address>), которая при помощи
регулярного выражения извлекает имя пользователя и почтовый домен из
email адреса и возвращает их в виде словаря. Если адрес не валиден,
выбросить исключение ValueError.

Пример:
!>>> email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}

!>>> email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть
их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
"""

import re

e_mail = re.compile(r'^\w[0-9a-zA-Z._]+@\w+.\w+$')

def email_parse(email):
    email_dict = {}
    if e_mail.match(email) != None:
        separator = email.find('@')
        username = re.sub(r'[^0-9a-zA-Z_.]', '', email[0:separator])
        domain = re.sub(r'^\w+@', '', email)
        email_dict['username'] = username
        email_dict['domain'] = domain
        return email_dict
    else:
        raise ValueError(f'ValueError: wrong email: {email}')

print(email_parse('Al_pushkin@по@чта.рф'))


"""
2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера 
из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, 
<requested_resource>, <response_code>, <response_size>), например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? 
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
"""

"""
3. Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3

!>>> a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; 
можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов? 
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
>>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""

from functools import wraps


def decor(func):
    @wraps(func)
    def f_info(*args, **kwargs):
        result = func(*args, **kwargs)
        s = ''
        kwargs_l = []
        for i in kwargs:
            kwargs_l.append(kwargs[i])
            print(f'{func.__name__}({kwargs[i]}: {type(i)}) -> {type(func(**kwargs))}')
        for j in args:
            if j == args[-1]:
                s = s + f'{func.__name__}({j}: {type(j)}) -> {type(func(*args))}. '
            else:
                s = s + f'{func.__name__}({j}: {type(j)}) -> {type(func(*args))}, '
        print(s)
        return result

    return f_info


@decor
def calc_cube(*args, **kwargs):
    l = []
    for x in args:
        res = x ** 3
        l.append(res)
        return l
    for x in kwargs.values():
        res = x ** 3
        return res

calc_cube(3.2, 4, 1)
calc_cube(x=10)
print(calc_cube.__name__)


"""
4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные 
значения функции и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


>>> a = calc_cube(5)
125
>>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?
"""
from functools import wraps

def val_checker(func_vch):
    def decor_func(func):
        @wraps(func)
        def wrapper(x):
            if func_vch(x):
                return func(x)
            else:
                raise ValueError(f'wrong val {x}')


        return wrapper

    return decor_func


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


x = 1
print(calc_cube(x))
print(calc_cube.__name__)