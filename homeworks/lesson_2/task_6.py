"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
"""
goods = []
specifications = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
structure = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
feature = None
control = None
while True:
    control = input("Для выхода нажмите 'Q'| Для продолжения 'Enter'| Для вывода структуры 'A' ").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':
        print('\n')
        print('Текущая структура')
        for key, value in structure.items():
            print(f'{key[:25]}: {value}')
        print('\n')
    for f in specifications.keys():
        feature = input(f'Введите характеристику "{f}" ')
        specifications[f] = int(feature) if (f == 'price' or f == 'quantity') else feature
        structure[f].append(specifications[f])
    goods.append((num, specifications))
