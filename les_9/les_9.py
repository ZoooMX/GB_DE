"""
Урок 9. Объектно-ориентированное программирование (ООП)

1. Создать класс TrafficLight (светофор).
- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный,жёлтый, зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2
секунды, третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке (красный,
жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import itertools
import time

class TrafficLight:

    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):
        c = itertools.cycle(self.__color)
        print(f'Traffic - {next(c)} - 7 sec')
        time.sleep(7)
        print(f'Traffic - {next(c)} - 2 sec')
        time.sleep(2)
        print(f'Traffic - {next(c)} - 4 sec')
        time.sleep(4)
        print(tl.running())

tl = TrafficLight()
print(tl.running())

"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. 
метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asp(self):
        ma = self._width * self._length * 25 * 5
        return ma

r = Road(20, 5000)
print(r.mass_asp())

"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать 
данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name, surname, position, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return f'{self.position} - wage={self.income["wage"]}$, bonus={self.income["bonus"]}$'


w = Position('peter', 'parker', 'dev', 200, 800)
print(w.get_full_name())
print(w.get_total_income())

"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также 
методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) 
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат.
"""

class Car:
    def __init__(self, speed, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Car {self.name} {self.color} is started.'

    def stop(self):
        return f'Car {self.name} {self.color} is stop.'

    def turn(self, direction):
        return f'Car {self.name} {self.color} turned {direction}.'

    def show_speed(self):
        return f'Car {self.name} {self.color} current speed = {self.speed} km/h'

class TownCar(Car):
    def info(self):
        return f'{self.name} {self.color} - town car'

    def show_speed(self):
        if self.speed > 60:
            return f'WARNING! Over speed! {self.speed} km/h'

class SportCar(Car):
    def info(self):
        return f'{self.name} {self.color} - sport car'

class WorkCar(Car):
    def info(self):
        return f'{self.name} {self.color} - work car'

    def show_speed(self):
        if self.speed > 40:
            return f'WARNING! Over speed! {self.speed} km/h'

class PoliceCar(Car):
    def info(self):
        if self.is_police == True:
            return f'{self.name} {self.color} - police car'
        else:
            return f'{self.name} {self.color} - civil car'

car = PoliceCar(350, 'red', 'AUDI TT',  False)
print(car.info())
print(car.go())
print(car.stop())
print(car.turn('left'))
print(car.show_speed())


"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'«Запуск отрисовки»'

class Pen(Stationery):
    def draw(self):
        return f'«Запуск отрисовки - {self.title}»'

class Pencil(Stationery):
    def draw(self):
        return f'«Запуск отрисовки - {self.title}»'

class Handle(Stationery):
    def draw(self):
        return f'«Запуск отрисовки - {self.title}»'

s = Pen('ручка')
print(s.draw())
s = Pencil('каранжаш')
print(s.draw())
s = Handle('маркер')
print(s.draw())