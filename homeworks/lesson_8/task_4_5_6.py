"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""
list_all = []


class Warehouse:
    def __init__(self):
        self.list_all = list_all

    @staticmethod
    def show():
        print('\nВ данный момент на складе: ')
        for el in list_all:
            print(el)


class Equipment:
    def __init__(self, name, quantity, department):
        self.name = name
        self.quantity = quantity
        self.department = department

    def add_equipment(self):
        try:
            quantity = int(self.quantity)
            local_list = f'Имя: {self.name}, Количество: {quantity}, Отдел: {self.department}'
            list_all.append(local_list)
        except ValueError:
            print(f'количество {self.name} должно быть указано цифрой')
            return None


class Printer(Equipment):
    def to_print(self):
        print('Идет печать...')
        return None


class Scanner(Equipment):
    def to_scan(self):
        print('Идет сканирование...')
        return None


class Copier(Equipment):
    def to_copier(self):
        print('Создание ксерокопии...')
        return None


pr1 = Printer('Hp', 50, 'Store')
pr1.add_equipment()
pr1.to_print()
sc1 = Scanner('Xerox', 8, 'Office')
sc1.add_equipment()
sc1.to_scan()
cop1 = Copier('Hp', 100, 'Office')
cop1.add_equipment()
cop1.to_copier()

Warehouse.show()
