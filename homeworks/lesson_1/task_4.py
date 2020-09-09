"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
maximum = 0
print('Введите число n: ',)
n = input()
n = int(n)
while n:
    tmp = n % 10
    n = n // 10
    maximum = tmp if tmp > maximum else maximum
print('Самая большая цифра в числе ', maximum)
