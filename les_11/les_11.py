"""Урок 11. Объектно-ориентированное программирование. Полезные дополнения

1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен
проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить
работу полученной структуры на реальных данных.
"""

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def form_date(cls, f_date):
        day, month, year = map(int, f_date.split('-'))
        final_date = cls(day, month, year)
        return final_date

    @staticmethod
    def valid_date(v_date):
        day, month, year = map(int, v_date.split('-'))
        return day <= 31 and month <= 12 and year >= 2022


date1 = Data.form_date('11-11-2022')
print(type(date1))
print(date1.day)
print(type(date1.day))

date2 = Data.valid_date('11-11-1988')
print(date2)

"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве 
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("Введите положительное число: ")

try:
    inp_data = int(inp_data)
    if inp_data == 0:
        raise OwnError('На ноль делить нельзя')
    print(1/inp_data)
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)


"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на 
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у 
пользователя данные и заполнять список необходимо только числами. Класс-исключение должен 
контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается, 
сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю 
ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не 
должна завершаться.
"""

class OwnError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


some_list = []

while True:
    inp_data = input("Введите число: ")
    try:
        if inp_data.isdigit():
            some_list.append(inp_data)
        elif inp_data != 'Q':
            raise OwnError('На ноль делить нельзя')
    except OwnError:
        print('Вы ввели не число')
        continue
    if inp_data == 'Q':
        break
print(some_list)

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также 
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы 
оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""

class Stock:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name


class Office_Equipment:
    def __init__(self, item, name, type_ec):
        self.type_ec = type_ec
        self.name = name
        self.item = item


class Printer(Office_Equipment):
    def __init__(self, item, name, num_color):
        super().__init__(self, item, name)
        self.num_color = num_color


class Xerox(Office_Equipment):
    def __init__(self, item, name, work_speed):
        super().__init__(self, item, name)
        self.work_speed = work_speed


class Scanner(Office_Equipment):
    def __init__(self, item, name, size):
        super().__init__(self, item, name)
        self.size = size


"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники 
на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class Stock:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name


class Office_Equipment:
    def __init__(self, name, company_department, amount):
        self.name = name
        self.company_department = company_department
        self.amount = amount
        self.info = {}


class Printer(Office_Equipment):
    def __init__(self, name, num_color, company_department, amount):
        super().__init__(name, company_department, amount)
        self.num_color = num_color

    def Input_Item(self):
        self.info['printer'] = {'name': self.name, 'num_color': self.num_color,
                                'company_department': self.company_department, 'amount': self.amount}


class Xerox(Office_Equipment):
    def __init__(self, name, work_speed, company_department, amount):
        super().__init__(name, company_department, amount)
        self.work_speed = work_speed

    def Input_Item(self):
        self.info['xerox'] = {'name': self.name, 'num_color': self.work_speed,
                              'company_department': self.company_department, 'amount': self.amount}


class Scanner(Office_Equipment):
    def __init__(self, name, size, company_department, amount):
        super().__init__(name, company_department, amount)
        self.size = size

    def Input_Item(self):
        self.info['scanner'] = {'name': self.name, 'num_color': self.size,
                                'company_department': self.company_department, 'amount': self.amount}


"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

class OwnError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


class Stock:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name


class Office_Equipment:
    def __init__(self, name, company_department, amount):
        self.name = name
        self.company_department = company_department
        self.amount = amount
        self.info = {}


class Printer(Office_Equipment):
    def __init__(self, name, num_color, company_department, amount):
        super().__init__(name, company_department, amount)
        self.num_color = num_color

    def Input_Item(self):
        try:
            if self.amount.isdigit():
                self.info['printer'] = {'name': self.name, 'num_color': self.num_color,
                                        'company_department': self.company_department, 'amount': self.amount}
                return print(self.info)
            else:
                raise OwnError(f'{self.amount} - вы ввели не число!')
        except OwnError:
            print(f'{self.amount} - вы ввели не число!')


class Xerox(Office_Equipment):
    def __init__(self, name, work_speed, company_department, amount):
        super().__init__(name, company_department, amount)
        self.work_speed = work_speed

    def Input_Item(self):
        try:
            if self.amount.isdigit():
                self.info['xerox'] = {'name': self.name, 'num_color': self.work_speed,
                                      'company_department': self.company_department, 'amount': self.amount}
                return print(self.info)
            else:
                raise OwnError(f'{self.amount} - вы ввели не число!')
        except OwnError:
            print(f'{self.amount} - вы ввели не число!')


class Scanner(Office_Equipment):
    def __init__(self, name, size, company_department, amount):
        super().__init__(name, company_department, amount)
        self.size = size

    def Input_Item(self):
        try:
            if self.amount.isdigit():
                self.info['scanner'] = {'name': self.name, 'num_color': self.size,
                                        'company_department': self.company_department, 'amount': self.amount}
                return print(self.info)
            else:
                raise OwnError(f'{self.amount} - вы ввели не число!')
        except OwnError:
            print(f'{self.amount} - вы ввели не число!')


pr = Printer('printer', 'bi-color', 'administration', 'six')
pr.Input_Item()
pr = Printer('printer', 'bi-color', 'administration', '6')
pr.Input_Item()

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение 
созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex_Operation:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        a = self.complex_num
        b = other.complex_num
        count_1 = 0
        count_2 = 0

        for i in a[1:-1]:
            count_1 += 1
            if i == '+' or i == '-':
                break

        for i in b[1:-1]:
            count_2 += 1
            if i == '+' or i == '-':
                break

        f_1 = str(int(a[0:count_1]) + int(b[0:count_2]))
        f_2 = str(int(a[count_1:-1]) + int(b[count_2:-1]))

        if f_2[0].isdigit():
            return f_1 + '+' + f_2 + 'j'
        else:
            return f_1 + f_2 + 'j'

    def __mul__(self, other):
        a = self.complex_num
        b = other.complex_num
        count_1 = 0
        count_2 = 0

        for i in a[1:-1]:
            count_1 += 1
            if i == '+' or i == '-':
                break

        for i in b[1:-1]:
            count_2 += 1
            if i == '+' or i == '-':
                break

        f_1 = str(int(a[0:count_1]) * int(b[0:count_2]))
        f_2 = str(int(a[count_1:-1]) * int(b[count_2:-1]))

        if f_2[0].isdigit():
            return f_1 + '+' + f_2 + 'j'
        else:
            return f_1 + f_2 + 'j'


x = '-24-20j'
y = '+40+26j'
co1 = Complex_Operation(x)
co2 = Complex_Operation(y)
print(co1 + co2)
print(co1 * co2)
