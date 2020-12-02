"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения
комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, name):
        self.a = a
        self.b = b
        self.name = name

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z3 = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z3 = {self.a * other.a - (self.b * other.b)} + ' \
               f'{(self.b * other.a + self.a * other.b)}i'

    def __str__(self):
        return f'z{self.name} = {self.a} + {self.b}i'


z1 = ComplexNumber(5, -6, '1')
z2 = ComplexNumber(8, 8, '2')
print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
