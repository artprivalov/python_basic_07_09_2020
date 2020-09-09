"""
2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
print('Введите количество секунд: ',)
sec = input()
sec = int(sec)
hour = sec // 3600
minute = (sec - (hour*3600)) // 60
sec = sec % 60
if hour < 10:
    hour = '0' + str(hour)
if minute < 10:
    minute = '0' + str(minute)
if sec < 10:
    sec = '0' + str(sec)
print('Часы, минуты и секунды в формате чч:мм:сс ',)
print(hour, ':', minute, ':', sec)
