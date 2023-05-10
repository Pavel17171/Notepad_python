from Models.get_date import get_date
from Models.get_last_id import get_last_id
from Models.file_csv_to_list import file_csv_to_list

def add_new_note(file_name, separator_character):
    temp_list = file_csv_to_list(file_name)
    with open(file_name, 'a+', encoding='utf-8') as file:
        id = get_last_id(temp_list, separator_character) + 1
        text = input("Введите текст: ")
        if text[-1] == ',':
            text += ' '
        string = '\n' + str(id) + separator_character + get_date() + \
            separator_character + '"' + str(text) + '"'
        file.write(string)
        file.close()
