month = str(input('Введите месяц: '))
number = int(input('Введите число: '))
if month == 'март' and number >= 21 and number <= 31 or month == 'апрель' and number >=1 and number <= 19:
  print('Овен')
elif month == 'апрель' and number >= 20 and number <= 30 or month == 'май' and number >=1 and number <= 20:
  print('Телец')
elif month == 'май' and number >= 21 and number <= 31 or month == 'июнь' and number >=1 and number <= 20:
  print('Близнецы')
elif month == 'июнь' and number >= 21 and number <= 30 or month == 'июль' and number >=1 and number <= 22:
  print('Рак')
elif month == 'июль' and number >= 23 and number <= 31 or month == 'август' and number >=1 and number <= 22:
  print('Лев')
elif month == 'август' and number >= 23 and number <= 31 or month == 'сентябрь' and number >=1 and number <= 22:
  print('Дева')
elif month == 'сентябрь' and number >= 23 and number <= 30 or month == 'октябрь' and number >=1 and number <= 22:
  print('Весы')
elif month == 'октябрь' and number >= 23 and number <= 31 or month == 'ноябрь' and number >=1 and number <= 21:
  print('Скорпион')
elif month == 'ноябрь' and number >= 22 and number <= 30 or month == 'декабрь' and number >=1 and number <= 21:
  print('Стрелец')
elif month == 'декабрь' and number >= 22 and number <= 31 or month == 'январь' and number >=1 and number <= 19:
  print('Козерог')
elif month == 'январь' and number >= 20 and number <= 31 or month == 'февраль' and number >=1 and number <= 18:
  print('Водолей')
elif month == 'февраль' and number >= 19 and number <= 29 or month == 'март' and number >=1 and number <= 20:
  print('Рыбы')