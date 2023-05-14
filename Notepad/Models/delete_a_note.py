from Models.file_csv_to_list import file_csv_to_list
from Models.string_to_list import string_to_list
from Models.ask_yes_no import ask_yes_no
from Models.list_to_csv import list_to_csv
from Models.test_line_from_csv import test_line_from_csv


def delete_a_note(separator_character, file_name, tittle_of_csv_file):
    temp_list = file_csv_to_list(file_name)
    flag_error = False
    for i in range(1, len(temp_list)):
        if test_line_from_csv(temp_list[i], separator_character) == False:
            flag_error = True
    reserve_name = list_to_csv(temp_list, file_name, tittle_of_csv_file)
    with open(file_name, 'w', encoding='utf-8') as file:
        if flag_error:
            print("В файле есть строки с ошибками. \nДля их удаления введите: 00")
        del_id = (input("Введите ID записи: "))
        while del_id.isdigit() == False:
            del_id = input("Введите ID записи: ")
        flag = False
        file.write(tittle_of_csv_file)
        for i in range(1, len(temp_list)):
            temp_row = string_to_list(temp_list[i], separator_character)
            if len(temp_row) == len(tittle_of_csv_file.split(separator_character)) and test_line_from_csv(temp_list[i], separator_character) == True:
                if int(temp_row[0]) != int(del_id):
                    file.write(
                        '\n' + temp_list[i][2:-2].replace("', '", ",").replace("\\\\", "\\"))
                else:
                    flag = True
            else:
                if str(del_id) == '00':
                    print("Удалить запись?")
                    answer = ask_yes_no(
                        '\n' + 'Ошибка в строке! Содержание строки: ' + temp_list[i][2:-2])
                    if answer:
                        flag = True
                    else:
                        file.write(
                            '\n' + temp_list[i][2:-2].replace("', '", ",").replace("\\\\", "\\"))
                else:
                    file.write(
                        '\n' + temp_list[i][2:-2].replace("', '", ",").replace("\\\\", "\\"))
        if flag:
            print("Запись удалена")
        else:
            print("ID не найден")
        file.close()
    return reserve_name
