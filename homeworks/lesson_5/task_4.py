"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_str = ''
try:
    with open('task_4.txt', 'r', encoding='UTF-8') as my_file:
        for line in my_file:
            new_str += my_dict.get(line.split()[0]) + " — " + line.split()[2] + '\n'
    with open('task_4_new.txt', 'w', encoding='UTF-8') as my_file_new:
        my_file_new.write(new_str)
except FileNotFoundError or FileExistsError:
    print('Файл task_4.txt отсутствует в директории')
