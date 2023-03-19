'''1. Реализовать класс «Дата», функция-конструктор которого должна
принимать дату в виде строки формата «день-месяц-год». В рамках класса
реализовать два метода. Первый, с декоратором @classmethod. Он должен
извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй,
с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.'''

from datetime import date
class Date:
    def __init__(self, date_txt):
        self.date_txt = data_txt.split('-')

    @classmethod
    def format_type(cls, date_txt):
        try:
            day, month, year = [int(i) for i in date_txt.split('-')]
            return f'День: {type(day), day}\nМесяц: {type(month), month}\nГод: {type(year), year}'
        except ValueError:
            return 'Указана неправильная дата!'

    @staticmethod
    def validation(date_txt):
        try:
            day, month, year = date_txt.split('-')
            date(int(year), int(month), int(day))
            return 'Есть такая дата!'
        except ValueError:
            return 'Указана неправильная дата!'

print(Date.format_type('06-09-1990'))
print(Date.format_type('we-09-1990'))
print(Date.validation('06-09-1990'))
print(Date.validation('14-12-1889'))
print(Date.validation('06-13-1990'))
print(Date.validation('06-09'))


'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на 
ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля 
в качестве делителя программа должна корректно обработать эту ситуацию и не 
завершиться с ошибкой.'''

class Error1 (Exception):
    def __init__(self, txt):
        self.txt = txt

input1 = input('Введите число: ')
input2 = input('Введите число, не равное 0: ')

try:
    num1 = int(input1)
    num2 = int(input2)
except FileExistsError:
    print()
if num2 == 0:
    raise Error1 ('Вы ввели число равное 0')
else:
    print(f'Результат деления: {num1 / num2}')

'''3. Создайте собственный класс-исключение, который должен проверять 
содержимое списка на наличие только чисел. Проверить работу исключения на 
реальном примере. Запрашивать у пользователя данные и заполнять список 
необходимо только числами. Класс-исключение должен контролировать типы 
данных элементов списка. Примечание: длина списка не фиксирована. Элементы 
запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, 
введя, например, команду «stop». При этом скрипт завершается, сформированный 
список с числами выводится на экран. Подсказка: для этого задания примем, 
что пользователь может вводить только числа и строки. Во время ввода 
пользователем очередного элемента необходимо реализовать проверку типа 
элемента. Вносить его в список, только если введено число. Класс-исключение 
должен не позволить пользователю ввести текст (не число) и отобразить 
соответствующее сообщение. При этом работа скрипта не должна завершаться.'''

class Error2 (Exception):
    def __init__(self, txt):
        self.txt = txt

list = []

while True:
    try:
        data_input = input('Введите число, чтобы внести его в список, '
                           'или "абв", чтобы выйти из программы: ')
        if data_input == 'абв':
            break
    except FileExistsError:
        print()
    if not data_input.isdigit():
        raise Error2('Вводить можно только числа!')
    else:
        list.append(data_input)

print(f'Вы вышли из программы. Итоговый список: {list}')

'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, 
описывающий склад. А также класс «Оргтехника», который будет базовым для 
классов-наследников. Эти классы — конкретные типы оргтехники (принтер, 
сканер, ксерокс). В базовом классе определите параметры, общие для 
приведённых типов. В классах-наследниках реализуйте параметры, уникальные 
для каждого типа оргтехники.'''

'''5. Продолжить работу над первым заданием. Разработайте методы, которые 
отвечают за приём оргтехники на склад и передачу в определённое 
подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую 
подходящую структуру (например, словарь).'''

'''6. Продолжить работу над вторым заданием. Реализуйте механизм валидации 
вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных. Подсказка: 
постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП.'''

class Error3 (Exception):
    def __init__(self, txt):
        self.txt = txt

class Warehouse:
    items = {}
    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity

    def receive(self):
        try:
            model = input(f'Введите модель: ')
            price = input(f'Введите цену за ед: ')
            quantity = input(f'Введите количество: ')
        except FileExistsError:
            print()
        if not quantity.isdigit() or not price.isdigit():
            raise Error3('Количество и цена могут быть только числом')
        else:
            item = {'Модель устройства': model, 'Цена за ед': price,
                        'Количество': quantity}
            self.items.update(item)
            print(f'В базу данных добавлено оборудование: {self.items}')

class Equipment(Warehouse):
    year = '2023'
    def __init__(self, power, weight, brand):
        self.power = power
        self.weight = weight
        self.brand = brand

class Printer(Equipment):
    def __init__(self, power, weight, brand, tech):
        super().__init__(power, weight, brand)
        self.tech = tech

class Scanner(Equipment):
    def __init__(self, power, weight, brand, max_speed):
        super().__init__(power, weight, brand)
        self.max_speed = max_speed

class Copier(Equipment):
    def __init__(self, power, weight, brand, size):
        super().__init__(power, weight, brand)
        self.size = size

a = Scanner(25, 6, 'Cannon', 300)
b = Printer(22, 3, 'HP', 'laser')
c = Copier(45, 15, 'Xerox', 'A4')
a.receive()
b.receive()
c.receive()

'''7. Реализовать проект «Операции с комплексными числами». Создайте класс 
«Комплексное число». Реализуйте перегрузку методов сложения и умножения 
комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры 
класса (комплексные числа), выполните сложение и умножение созданных 
экземпляров. Проверьте корректность полученного результата.'''

class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел: {self.a + other.a} +' \
               f' {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел: {self.a * other.a} +' \
               f' {self.a * other.b} *i + {self.b * other.a} *i +' \
               f' {self.b * other.b} *i^2'

num1 = ComplexNumber(5, -3)
num2 = ComplexNumber(2, -1)
print(num1 + num2)
print(num1 * num2)