"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class Check:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def div_by_null(divider, denominator):
        try:
            return f'{divider / denominator}'
        except ZeroDivisionError:
            return f'Ошибка: деление на ноль'


print(Check.div_by_null(10, 0))
print(Check.div_by_null(50, 0))
print(Check.div_by_null(25, 0.001))
