import json

def read_json(file_path, word_max_len=6, top_words_amt=10):
    with open('newsafr.json', encoding='utf-8') as f:
        json_data = json.load(f)
    new_list = list()
    new_dict = dict()
    for x in json_data['rss']['channel']['items']:
        result = [i for i in x['description'].split() if len(i) > word_max_len]
        new_list.extend(result)
    new_set = set(new_list)
    for word in new_set:
        new_dict[word] = new_list.count(word)
    sorted_dict = sorted(new_dict.items(), key= lambda x:x[1], reverse=True)
    finish = list()
    for i in sorted_dict:
        finish.append(i[0])
    return finish[:top_words_amt]


if __name__ == '__main__':
    print(read_json('newsafr.json'))