"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
try:
    with open("task_2.txt", "r", encoding="UTF-8") as my_file:
        string_num = 0
        for line in my_file:
            string_num = string_num + 1
            print(f"Количество слов в {string_num}-ой строке: {len(line.split(' '))}")
        print(f"Количество строк: {string_num}")
except FileNotFoundError or FileExistsError:
    print('Файл task_2.txt отсутствует в директории')
my_file.close()
