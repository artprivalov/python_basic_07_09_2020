"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""
from itertools import count
from itertools import cycle

number = int(input('Введите значение number: '))
print(f'Целые числа, начиная с {number} до 200:')
for number in count(number):
    if number > 200:
        break
    else:
        print(number, end=' ')
print('\n')

my_list = [179, 177, 'aBc']
number_list = int(input(f'Сколько элементов списка {my_list} вывести в консоль? '))
count = 1
for item in cycle(my_list):
    if count > number_list:
        break
    print(item, end=' ')
    count += 1
