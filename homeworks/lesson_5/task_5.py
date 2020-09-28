"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import os
import random

try:
    with open('task_5.txt', 'w', encoding='UTF-8') as my_file:
        for i in range(random.randint(10, 250)):
            my_file.write(str(i) + ' ')
    with open('task_5.txt', 'r', encoding='UTF-8') as my_file:
        print(f"Сумма чисел в файле: {sum(map(int, my_file.read().split()))}")
except FileNotFoundError or FileExistsError:
    print('Файл task_4.txt отсутствует в директории')
