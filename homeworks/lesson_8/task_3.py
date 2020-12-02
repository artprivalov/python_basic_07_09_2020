"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class Check:
    def __init__(self):
        self.list = []

    def new_input(self):

        while True:
            try:
                new = int(input('\nВведите значения и Enter '))
                self.list.append(new)
                print(f'Результирующий список - {self.list}')
            except ValueError:
                print(f'Недопустимое значение - строка')
                y_or_n = input(f'Повторить? Да -- Y Выход -- Q: ')
                if y_or_n == 'Y' or y_or_n == 'y':
                    print(el.new_input())
                elif y_or_n == 'Q' or y_or_n == 'q':
                    return exit(0)
                else:
                    return exit(0)


el = Check()
print(el.new_input())
