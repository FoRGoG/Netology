file_names = ['1.txt', '2.txt', '3.txt']
for file_name in file_names:
    with open(file_name, 'r', encoding='utf8') as result:
        lines = result.readlines()
        length = len(lines)
        print(length)