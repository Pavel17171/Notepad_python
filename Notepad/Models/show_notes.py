from Models.string_to_list import string_to_list
from Models.file_csv_to_list import file_csv_to_list


def show_notes(file_name, separator_character):
    temp_list = file_csv_to_list(file_name)
    len_id = 10
    len_date = 19
    title = str(temp_list[0]).split(';')
    print(
        f"{title[0][2:].ljust(len_id)} | {title[1].ljust(len_date)} | {title[2][:-2]}")
    if len(temp_list) > 1:
        for i in range(1, len(temp_list)):
            temp_row = string_to_list(temp_list[i], separator_character)
            if len(temp_row) == 3:
                print(f'{temp_row[0].ljust(len_id)}', end=' | ')
                print(f'{temp_row[1].ljust(len_date)}' + ' | ' +
                      temp_row[2].replace("', '", ",").replace("\\\\", "\\"))
            else:
                print(f'{temp_row[0]}')
    print(f'Количество записей: {len(temp_list)-1}')
