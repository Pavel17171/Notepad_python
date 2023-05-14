from Models.get_date import get_date
from Models.get_last_id import get_last_id
from Models.file_csv_to_list import file_csv_to_list


def add_new_note(file_name, separator_character, tittle_of_csv_file, len_title):
    temp_list = file_csv_to_list(file_name)
    with open(file_name, 'a+', encoding='utf-8') as file:
        id = get_last_id(temp_list, separator_character, tittle_of_csv_file) + 1
        title = input("Введите заголовок: ")
        while len(title) > len_title:
            title = input("Длина заголовка не более 16 символов")
        while title[-1] == ',' or title[-1] == '\\':
            title = input("Заголовок не должен заканчиваться: ',' или '\\'\n")
        text = input("Введите текст: ")
        if text[-1] == ',':
            text += ' '
        string = '\n' + str(id) + separator_character + get_date() + separator_character + \
            '"' + str(title) + '"' + separator_character + \
            '"' + str(text) + '"'
        file.write(string)
        file.close()
