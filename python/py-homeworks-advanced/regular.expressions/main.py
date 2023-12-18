import csv
import re

def open_file(file_name):
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def correct_name(contacts_list):
    new_list = list()
    exp1 = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    exp2 = r'\1\3\10\4\6\9\7\8'
    for name in contacts_list:
        string_name = ','.join(name)
        replace_name = re.sub(exp1, exp2, string_name)
        split_name = replace_name.split(',')
        new_list.append(split_name)
    return new_list


def correct_number(contacts_list):
    new_list = list()
    exp3 = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\-*)(\s*)(\d{3})(\-*)(\d{2})(\-*)(\d{2})(\s*)(\(*)([А-ЯЁа-яё]*)(\.*)(\s*)(\d*)(\)*)'
    exp4 = r'+7(\4)\8-\10-\12\13\15\16\18'
    for number in contacts_list:
        string_number = ','.join(number)
        replace_number = re.sub(exp3, exp4, string_number)
        split_number = replace_number.split(',')
        new_list.append(split_number)
    return new_list


def duplicates(contacts_list):
    new_list = list()
    for contact in contacts_list:
        fio_list = ' '.join(contact[0:3]).split()
        if len(fio_list) != 3:
            fio_list.append('')
        full_list = fio_list + contact[3:]
        for contacts_new in new_list:
            if contacts_new[:2] == full_list[:2]:
                full_list = [x if x != '' else y for x, y in zip(contacts_new, full_list)]
                new_list.remove(contacts_new)
        new_list.append(full_list)
    return new_list


def write_file(contacts_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

if __name__ == '__main__':
    result = open_file('phonebook_raw.csv')
    result = correct_name(result)
    result = correct_number(result)
    result = duplicates(result)
    write_file(result)