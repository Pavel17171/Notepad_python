import os
from view import menu
from Models.create_file_csv import create_file_csv
from Models.add_new_note import add_new_note
from Models.show_notes import show_notes
from Models.edit_note import edit_note
from Models.delete_a_note import delete_a_note


def button_click():
    file_name = "Notepad.csv"
    tittle_of_csv_file = 'ID;DATE;TITTLE;TEXT'
    separator_character = ';'
    len_title = 16
    create_file_csv(file_name, tittle_of_csv_file)
    flag = True
    while flag:
        answer = menu()
        match answer:
            case '1':
                add_new_note(file_name, separator_character, tittle_of_csv_file, len_title)
                print()
            case '2':
                show_notes(file_name, separator_character, tittle_of_csv_file)
                print()
            case '3':
                reserve_name = ''
                reserve_name = edit_note(file_name, separator_character, tittle_of_csv_file)
                if len(reserve_name) > 0:
                    os.remove(reserve_name)
                print()
            case '4':
                reserve_name = ''
                reserve_name = delete_a_note(separator_character, file_name, tittle_of_csv_file)
                if len(reserve_name) > 0:
                    os.remove(reserve_name)
                print()
            case '0':
                print("Выход")
                print()
                flag = False
            case _:
                print("Некорректный ввод. Попробуйте еще раз")
                print()
                