def que():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
        ]

    dictionary = {}

    for meaning in queries:
        words = meaning.split()

        if len(words) in dictionary.keys():
            dictionary[len(words)] += 1
        else:
            dictionary.update({len(words):1})
    result = {}
    for key, value in dictionary.items():
        percentage = round((value / len(queries)) * 100, 2)
        result[key] = percentage
    return f'Запросов из 2-х слов: {result[2]}%, Запросов из 3-х слов: {result[3]}%'
