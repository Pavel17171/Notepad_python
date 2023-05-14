from Models.file_csv_to_list import file_csv_to_list
from Models.string_to_list import string_to_list
from Models.list_to_csv import list_to_csv
from Models.get_date import get_date
from Models.ask_yes_no import ask_yes_no

def edit_note(file_name, separator_character, tittle_of_csv_file):
    temp_list = file_csv_to_list(file_name)
    reserve_name = list_to_csv(temp_list, file_name, tittle_of_csv_file)
    with open(file_name, 'w', encoding='utf-8') as file:
        edit_id = (input("Введите ID записи: "))
        while edit_id.isdigit() == False:
            edit_id = input("Введите ID записи: ")
        flag = False
        file.write(tittle_of_csv_file)
        for i in range(1, len(temp_list)):
            temp_row = string_to_list(temp_list[i], separator_character)
            if len(temp_row) == len(tittle_of_csv_file.split(separator_character)):
                if int(temp_row[0]) != int(edit_id):
                    file.write('\n' + temp_list[i][2:-2].replace("', '", ",").replace("\\\\", "\\"))
                else:
                    print('Старая запись: ')
                    print('Заголовок: ' + temp_row[2].replace("', '", ",").replace("\\\\", "\\"))
                    print('Текст заметки: ' + temp_row[3].replace("', '", ",").replace("\\\\", "\\"))
                    if ask_yes_no('Редактировать заголовок?'):
                        temp_row[2] = input("Введите текст заголовка: ").replace("', '", ",")                        
                        print(temp_row[2][-1])
                        if temp_row[2][-1] == ',':
                            temp_row[2] += ' '
                    if ask_yes_no('Редактировать заметку?'):
                        temp_row[3] = input("Введите текст заметки: ").replace("', '", ",")
                        print(temp_row[3][-1])
                        if temp_row[3][-1] == ',':
                            temp_row[3] += ' '
                    print(
                        f'{str(temp_row[0])};{str(get_date())};{str(temp_row[2])};{str(temp_row[3])}')
                    file.write(
                        '\n' + (f'{str(temp_row[0])};{str(get_date())};"{str(temp_row[2])}";"{str(temp_row[3])}"'))
                    flag = True
            else:
                file.write('\n' + temp_list[i][2:-2].replace("', '", ",").replace("\\\\", "\\"))
        if flag:
            print("Запись отредактирована")
        else:
            print("ID не найден")
        file.close()
    return reserve_name
