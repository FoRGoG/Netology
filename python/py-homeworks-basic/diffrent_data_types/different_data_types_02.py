import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    xml_items= root.findall('channel/item')
    new_list = list()
    new_dict = dict()
    for xmli in xml_items:
        result = [i for i in xmli.find('description').text.split() if len(i) > word_max_len]
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
    print(read_xml('newsafr.xml'))