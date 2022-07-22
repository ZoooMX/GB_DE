'''Урок 10. Объектно-ориентированное программирование. Продвинутый уровень
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
| 31 22 |
| 37 43 |
| 51 86 |
| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |
| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и пр.
'''


class Matrix:
    def __init__(self, m):
        self.m = m

    def matrix(self):
        for i in self.m:
            str_ = ''
            for a in i:
                str_ += str(f'{a} ')
            print(f'| {str_}|')

    def __add__(self, other):
            sum_matx = []
            count1 = 0
            for i in range(len(self.m)):
                sm1 = []
                if count1 != len(self.m[i]):
                    for j in range(len(self.m[i])):
                        if len(sm1) != len(self.m[i]):
                            sm1.append(self.m[i][count1] + other.m[i][count1])
                        count1 += 1
                    count1 = 0
                sum_matx.append(sm1)
            return sum_matx


    def __str__(self):
        return f'Вывод матрицы в первичном виде: {self.m}'

matx1 = Matrix([[1, 2, 1], [1, 3, 12], [1, 4, 1], [1, 6, 2], [20, 20, 0]])
matx1.matrix()
print(matx1.__str__())
matx2 = Matrix([[2, 3, 1], [2, 3, 12], [2, 3, 4], [1, 1, 3], [10, 11, 0]])
print(matx1 + matx2)



'''
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) 
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся 
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут 
быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для 
костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
'''

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, v=0):
        self.v = v

    @abstractmethod
    def ex_clothes(self):
        pass

class Coat(Clothes, ABC):
    @property
    def ex_clothes(self):
        return round(self.v / 6.5 + 0.5)

class Costume(Clothes, ABC):
    @property
    def ex_clothes(self):
        return round(2 * self.v + 0.3)


cl = Coat(v=100)
print(cl.ex_clothes)
cl = Costume(v=50)
print(cl.ex_clothes)


'''
3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс 
«Клетка». В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание 
(__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только 
к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
Сложение. 
Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. 
Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух 
клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. 
Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
Деление. 
Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества 
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному 
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() 
вернёт строку: *****\n*****\n**.
Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку: 
*****\n*****\n*****.'''


class Cell:
    def __init__(self, num_cell: int, num_row: int = 0):
        self.num_cell = num_cell
        self.num_row = num_row

    def __add__(self, other):
        return self.num_cell + other.num_cell

    def __sub__(self, other):
        sub_cell = self.num_cell - other.num_cell
        if sub_cell > 0:
            return sub_cell
        else:
            return 'Разность количества ячеек двух клеток меньше нуля!'

    def __mul__(self, other):
        return self.num_cell * other.num_cell

    def __floordiv__(self, other):
        return self.num_cell // other.num_cell

    def __truediv__(self, other):
        return self.num_cell // other.num_cell

    def make_order(self):
        i = self.num_cell // self.num_row
        for x in range(i):
            print('*' * self.num_row)
        if type(self.num_cell / self.num_row) == float:
            print('*' * (self.num_cell - (i * self.num_row)))


cell1 = Cell(21, 11)
cell1.make_order()

cell2 = Cell(50)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1 // cell2)
