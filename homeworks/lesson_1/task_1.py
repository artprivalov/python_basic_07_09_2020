"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
print('Ваше Имя: ',)
name = input()
print('Привет,', name, '!')
print('Введите два числа')
number1 = input()
number2 = input()
concatenation = number1 + number2
print('Конкатенация цифр:', concatenation)
number1 = int(number1)
number2 = int(number2)
print('Сумма чисел:', number1+number2)
