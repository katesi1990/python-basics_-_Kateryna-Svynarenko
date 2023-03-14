'''1. Создать класс TrafficLight (светофор). определить у него один атрибут
color (цвет) и метод running (запуск); атрибут реализовать как приватный; в
рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный; продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и
вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка
режимов. При его нарушении выводить соответствующее сообщение и завершать
скрипт.'''

from time import sleep
class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 6}

    @staticmethod
    def running():
        for key, value in TrafficLight.__color.items():
            print(f'Traffic color: {key}')
            sleep(value)

TL = TrafficLight
TL.running()


'''2. Реализовать класс Road (дорога). определить атрибуты: length (длина), 
width (ширина); значения атрибутов должны передаваться при создании 
экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта 
массы асфальта, необходимого для покрытия всей дороги; использовать формулу: 
длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна; проверить работу метода. Например: 
20 м*5000 м*25 кг*5 см = 12500 т.'''

class Road:
    thickness = 15
    unit_m = 35

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_mass(self):
        m = self._length * self._width * Road.thickness * Road.unit_m
        print(f'Масса асфальта на дорожное покрытие: {m} кг')

r_obj = Road(1000, 4)
r_obj.road_mass()

'''3. Реализовать базовый класс Worker (работник). определить атрибуты: 
name, surname, position (должность), income (доход); последний атрибут 
должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и 
премия, например, {"wage": wage, "bonus": bonus}; создать класс Position (
должность) на базе класса Worker; в классе Position реализовать методы 
получения полного имени сотрудника (get_full_name) и дохода с учётом премии 
(get_total_income); проверить работу примера на реальных данных: создать 
экземпляры класса Position, передать данные, проверить значения атрибутов, 
вызвать методы экземпляров.'''

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

pos_obj = Position("Joh", "Kwick", "sales manager", 2600, 550)
pos_obj.get_full_name()
print(f'Доход: {pos_obj.get_total_income()}')

'''4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). А также методы: go, stop, 
turn(direction), которые должны сообщать, что машина поехала, остановилась, 
повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, 
WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который 
должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar 
переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 
40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте 
экземпляры классов, передайте значения атрибутов. Выполните доступ к 
атрибутам, выведите результат. Вызовите методы и покажите результат.'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police == True)

    def go(self):
        print("Автомобиль поехал")

    def stop(self):
        print("Автомобиль остановился")

    def turn(self):
        direction = input('Введите направление поворота: ')
        print(f'Поворот автомобиля {direction}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текушая скорость: {self.speed} км/ч')
        if self.speed > 60:
            print("Вы превысили лимит скорости 60 км/ч")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текушая скорость: {self.speed} км/ч')

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текушая скорость: {self.speed} км/ч')
        if self.speed > 40:
            print("Вы превысили лимит скорости 40 км/ч")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текушая скорость: {self.speed} км/ч')

AUDI = TownCar(70, 'black', 'A7', False)
Biyadi = WorkCar(60, 'white', 'BR5', False)
Nissan = SportCar(120, 'Green', 'X8', False)
Toyota = PoliceCar(80, 'Blue', 'MX5', True)

print(f'{Toyota.name} полицейская машина? - {Toyota.is_police}')
print(f'{Nissan.name} полицейская машина? - {Nissan.is_police}')

print(AUDI.show_speed())
print(Biyadi.show_speed())
print(Toyota.show_speed())

print(AUDI.turn())

'''5. Реализовать класс Stationery (канцелярская принадлежность). определить 
в нём атрибут title (название) и метод draw (отрисовка). Метод выводит 
сообщение «Запуск отрисовки»; создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер); в каждом классе реализовать 
переопределение метода draw. Для каждого класса метод должен выводить 
уникальное сообщение; создать экземпляры классов и проверить, что выведет 
описанный метод для каждого экземпляра.'''

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Запуск отрисовки маркером")

pn_obj = Pen("blue123")
pnl_obj = Pencil("2B")
hnl_obj = Handle("MR1")
print(pn_obj.draw())
print(pnl_obj.draw())
print(hnl_obj.draw())