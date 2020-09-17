"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""
x = input("Введите число x, x: ")
y = input("Введите число y, y: ")
z = input("Введите число z, z: ")


def my_func(x, y, z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        if x + y > y + z and x + y > x + z:
            return f'Сумма больших аргументов, а именно {x} и {y}, равна {x + y}'
        elif y + z > x + y and y + z > x + z:
            return f'Сумма больших аргументов, а именно {y} и {z}, равна {y + z}'
        elif x + z > x + y and x + z > y + z:
            return f'Сумма больших аргументов, а именно {x} и {z}, равна {x + z}'
        else:
            return f'Сумма {x} + {y}, равна {y} + {z}, как и {x} + {z}, а именно {x + y}'
    except ValueError:
        return 'Используйте цифры'


print(my_func(x, y, z))
