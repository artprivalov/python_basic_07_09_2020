"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также
словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
(со значением убытков).
"""
import json

try:
    with open('task_7.txt', 'r', encoding='UTF-8') as my_file:
        sum_dict = {}
        profit = 0
        count = 0
        for line in my_file:
            if float(line.split()[2]) - float(line.split()[3]) >= 0:
                profit += float(line.split()[2]) - float(line.split()[3])
                count += 1
            sum_dict[line.split()[0]] = round(float(line.split()[2]) - float(line.split()[3]), 3)
        medium_profit = {'medium_profit': round(profit / count, 3)}
    with open('task_7.json', 'w', encoding='UTF-8') as json_file:
        json.dump([sum_dict, medium_profit], json_file)
except FileNotFoundError or FileExistsError:
    print('Файл task_7.txt отсутствует в директории')
