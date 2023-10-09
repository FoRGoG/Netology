from pprint import pprint

def merge_files(files_list):
    data = {}
    for file in files_list:
        with open(file, encoding='utf-8') as f:
            file_data = f.readlines()
            data[len(file_data)] = (file, ' ', file_data)
    #pprint(data)
    data = dict(sorted(data.items()))
    pprint(data)

    with open('result.txt', 'w', encoding= 'utf-8') as result:
        for key, value in data.items():
            result.write(f"{value[0]} \n")
            result.write(f"{key} \n")
            result.write(f"{value[1]} \n")

files = ['1.txt', '2.txt', '3.txt']
merge_files(files)