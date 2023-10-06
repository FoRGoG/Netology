documents = [
    {
        "type": "passport",
        "number": "2207 876234",
        "name": "Василий Гупкин"
    }, {
        "type": "invoice",
        "number": "11-2",
        "name": "Геннадий Покемонов"
    }, {
        "type": "insurance",
        "number": "10006",
        "name": "Аристарх Павлов"
    }
]
directories = {  # словарь
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people():
    num_doc = input("Введите номер документа: ")
    for information in documents:
        if information.get("number") == num_doc:
            return information.get("name")
    else:
        return "Такого документа нет"


def get_shelf():
    num_shelf = input("Введите номер документа: ")
    for key in directories:
        if num_shelf in directories.get(key):
            return key
    else:
        return "Неправильно"


def list():
    for doc in documents:
        a = f'{doc["type"]} {doc["number"]} {doc["name"]}'
        return a


def add(docs, shelfs, shelf, type, number, name):
    doc = {"type": type, "number": number, "name": name}
    docs.append(doc)
    shelfs[shelf].append(doc["number"])
    return "Документ добавлен"


def main():
    print(
        "\n Введите команду: p – номер документа и имя человека; s – спросит номер документа и выведет номер полки, на которой он находится; l – которая выведет список всех документов; a – команда, которая добавит новый документ в каталог и в перечень полок. quit - завершить.\n"
    )
    while (True):
        command = input().lower()
        if command == "p":
            print(people())
        elif command == "s":
            print(get_shelf())
        elif command == "l":
            print(list())
        elif command == "a":
            shelf = input("Введите номер полки куда положить документ: ")
            if shelf in directories.keys():
                type = input("Введите тип документа: ")
                number = input("Введите номер документа: ")
                name = input("Введите имя владельца документа: ")
                add(documents, directories, shelf, type, number, name)
            elif shelf not in directories:
                print("Такой полки нет")
        elif command == "quit":
            break
        else:
            print("Введите корректную команду")


main()
