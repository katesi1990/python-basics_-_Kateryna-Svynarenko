'''1. Создать программный файл в текстовом формате, записать в него
построчно данные, вводимые пользователем. Об окончании ввода данных будет
свидетельствовать пустая строка.'''

with open ('urok5.txt', 'w', encoding='utf-8') as file:
    user_input = []
    while user_input != '':
        user_input = input('Введите текст: ')
        file.write(user_input)
    else:
        exit()

'''2. Создать текстовый файл (не программно), сохранить в нём несколько
строк, выполнить подсчёт строк и слов в каждой строке.'''
#Writing lines into document:
with open('urok5-2.txt', 'w', encoding='utf-8') as file:
    line1 = 'Good morning!'
    line2 = 'Good afternoon!'
    line3 = 'Good evening!'
    line4 = 'Good night!'
    file.writelines([line1 + '\n', line2 + '\n', line3 + '\n', line4 + '\n'])

#Read document and count lines:
with open('urok5-2.txt', 'r', encoding='utf-8') as file:
    lines_n = len(file.readlines())
    print(f'Количество строк: {lines_n}')

#Read document and count words:
with open('urok5-2.txt', 'r', encoding='utf-8') as file:
    words_n = 0
    for line in file:
        words_n += len(line.split())
    print(f'Количество слов: {words_n}')

'''3. Создать текстовый файл (не программно). Построчно записать фамилии 
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из 
сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников. Пример файла:

Иванов 23543.12
Петров 13749.32'''

# Список сотрудников с окладом:
dict = {
        "Ivanov" : '34899',
        "Petrov" : '23456',
        "Sidorov" : '50489',
        "Kovalchuk" : '47890',
        "Grishenko" : '32987',
        "Maslov": '19007',
        "Golub": '31098',
        "Vasiliev": '67890',
        "Fedorov": '19345',
        "Litvin": '77234',
        }
# Построчно записываем данные в текстовый документ:
file = open("urok5_3.txt", "w")
for key,value in dict.items():
    file.write(key + ": " + value + '\n')
file.close()
# Проверяем содержимое документа:
with open("urok5_3.txt", "r") as document:
    print(document.read())
#Сотрудники с окладом < 20000:
with open("urok5_3.txt", "r") as document:
    for line in document:
        key, value = line.split()
            if int(value) < 20000:
                print("Сотрудник с окладом < 20000:" + key)
# Общая сумма окладов:
with open("urok5_3.txt", "r") as document:
    sum_salary = 0
    for line in document:
        key, value = line.split()
        sum_salary += int(value)
# Общая сумма окладов:
with open('urok5_3.txt', 'r', encoding='utf-8') as file:
    staff_n = 0
    for line in file:
        staff_n += 1
# Значение среднего оклада:
avg_salary = sum_salary / staff_n
print(f"Средний оклад: {avg_salary}")

'''4. Создать (не программно) текстовый файл со следующим содержимым: One — 
1 Two — 2 Three — 3 Four — 4 Напишите программу, открывающую файл на чтение 
и считывающую построчно данные. При этом английские числительные должны 
заменяться на русские. Новый блок строк должен записываться в новый 
текстовый файл.'''

words = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
with open ('urok5_4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        for key in words.keys():
            line = line.replace(key, words[key])
        print(line)
        with open ('urok5_4(1).txt', 'w', encoding='utf-8') as file2:
            file2.write(f"\n {line}")

'''5. Создать (программно) текстовый файл, записать в него программно набор 
чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в 
файле и выводить её на экран.'''

with open ('urok5_5.txt', 'w', encoding='utf-8') as file3:
    numbers = [2, 3, 6, 5, 67, 12]
    num_str = ''
    for i in numbers:
        num_str += f'{i} '
    file3.write(num_str)
with open ('urok5_5.txt', 'r', encoding='utf-8') as file3:
    sum_num = 0
    for line in file3:
        nums = line.split()
        for i in nums:
            sum_num += int(i)
        print(sum_num)

'''6. Сформировать (не программно) текстовый файл. В нём каждая строка 
должна описывать учебный предмет и наличие лекционных, практических и 
лабораторных занятий по предмету. Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество 
занятий по нему. Вывести его на экран. Примеры строк файла: Информатика: 
100(л) 50(пр) 20(лаб). Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) — 
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

import re
with open ('urok5_6.txt', 'r', encoding='utf-8') as file6:
    subj_dict = {}
    subjects = file6.readlines()
    for line in subjects:
        subj, etc = line.split(':')
        subj_sum = 0
        numbers = re.findall('\d+', line)
        if not numbers:
            continue
        else:
            for num in numbers:
                subj_sum += int(num)
        subj_dict.update({subj: subj_sum})
print(subj_dict)

'''7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название,
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО
10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
прибыли её не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их
прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, 
{"average_profit": 2000}]
Подсказка: использовать менеджер контекста.'''

import json
with open ('urok5_7.txt', 'r', encoding='utf-8') as file7:
    content = file7.readlines()
    #print(content)
    firm_num = 0
    profit_sum = 0
    dictionary = {}
    for line in content:
        firm, ownr, rev, exp = line.split()
        profit = int(rev) - int(exp)
        dictionary.update({firm: profit})
        if profit > 0:
            firm_num += 1
            profit_sum += profit
        else:
            firm_num += 0
            profit_sum += 0
    profit_avg = profit_sum / firm_num
    dictionary.update({'average_profit': profit_avg})
print(dictionary)

with open("my_file.json", "w") as write_f:
    json.dump(dictionary, write_f)