"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []
        for i in day_month_year.split():
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year:
                    return f'{day}-{month}-{year} корректная дата'
                else:
                    return f'ошибка в дате {day}-{month}-{year}, {year}й год ещё не наступил :)'
            else:
                return f'ошибка в дате {day}-{month}-{year}, {month} - некорректный месяц'
        else:
            return f'ошибка в дате {day}-{month}-{year}, {day} - некорректный номер дня'

    def __str__(self):
        return f'дата: {Data.extract(self.day_month_year)}'


today = Data('1 - 12 - 2020')
print(today)
print(Data('9 - 05 - 2017'))
print(Data('2 - 08 - 1997'))
print('')
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.valid(1, 11, 2000))
