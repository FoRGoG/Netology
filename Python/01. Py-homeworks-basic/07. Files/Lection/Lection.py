file = open('data.txt', 'w') # Создаем файл
file.write('Привет, файл!') # Добавляем строчку
file.close()

file = open('data.txt') # Открываем файл
print(type(file), '\n')

data = file.read() # Выполняем работу (пока читаем файл)
print(data)
print(type(data), '\n')

file.close() # Закрываем файл

print(f'То, что у нас в памяти - {data}')
