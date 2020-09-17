"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
total_result = 0
total_numbers = []
while True:
    control = input("Для выхода нажмите 'Q'| Для продолжения 'Enter' | Для просмотра текущего ряда чисел нажмите 'A'   ").upper()
    if control == 'Q':
        break
    if control == 'A':
        print('\n')
        print('Текущий ряд чисел: ', ' '.join(total_numbers))
    else:
        numbers = input('Введите ряд чисел через пробел ')
        numbers = numbers.split(' ')
        print('Ваш ряд чисел:', ', '.join(numbers))
        i = 0
        result = 0
        while i < len(numbers):
            result = result + int(numbers[i])
            total_numbers.append(numbers[i])
            i = i + 1
        total_result = total_result + result
        total_numbers = total_numbers + ['|']
        print('Сумма всего ряда', total_result)
