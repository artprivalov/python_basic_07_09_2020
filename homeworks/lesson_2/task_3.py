"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
month_dict = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'}
season_dict = {1: 'Зима',
               2: 'Зима',
               3: 'Весна',
               4: 'Весна',
               5: 'Весна',
               6: 'Лето',
               7: 'Лето',
               8: 'Лето',
               9: 'Осень',
               10: 'Осень',
               11: 'Осень',
               12: 'Зима'}
print("Введите номер месяца ", end=' ')
num_month = int(input())
print('Сейчас ' + str(month_dict.get(num_month)) + ', ' + str(season_dict.get(num_month)))
print('')
"""Решение через list"""
list_of_month = list(month_dict.values())
list_of_seasons = list(season_dict.values())
print("Введите номер месяца ", end=' ')
num_month = int(input())
if 0 < num_month < 3 or num_month == 12:
    print('Сейчас ' + str(list_of_month[num_month - 1]) + ', Зима')
elif 2 < num_month < 6:
    print('Сейчас ' + str(list_of_month[num_month - 1]) + ', Весна')
elif 5 < num_month < 9:
    print('Сейчас ' + str(list_of_month[num_month - 1]) + ', Лето')
elif 8 < num_month < 12:
    print('Сейчас ' + str(list_of_month[num_month - 1]) + ', Зима')
else:
    print('Вы допустили ошибку')
