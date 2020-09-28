"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
try:
    with open('task_3.txt', 'r', encoding='UTF-8') as my_file:
        string_num = 0
        sum_all = 0
        for line in my_file:
            sum_all = sum_all + float(line.split()[1])
            if float(line.split()[1]) < 20000:
                print(line.split(':')[0], end=', ')
            string_num = string_num + 1
        print('имеет (имеют) доход менее 20000 ')
        print(f'Средний доход сотрудника составляет {sum_all / string_num}')
except FileNotFoundError or FileExistsError:
    print('Файл task_2.txt отсутствует в директории')
my_file.close()
