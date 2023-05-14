from Models.string_to_list import string_to_list
from Models.file_csv_to_list import file_csv_to_list
from Models.date_selection import date_selection
from Models.test_date import test_date

def show_notes(file_name, separator_character, tittle_of_csv_file):
    full_date = answer_on_question()
    temp_list = file_csv_to_list(file_name)
    len_id = 10
    len_date = 19
    len_title = 16
    count = 0
    title_of_notepad = str(temp_list[0]).split(separator_character)
    print(
        f'{title_of_notepad[0][2:].ljust(len_id)} | ' 
        + f'{title_of_notepad[1].ljust(len_date)} | '
        + f'{title_of_notepad[2].ljust(len_title)} | '
        + f'{title_of_notepad[3][:-2]}')
    if len(temp_list) > 1:
        for i in range(1, len(temp_list)):
            temp_row = string_to_list(temp_list[i], separator_character)
            flag = test_date(temp_row[1], full_date)
            if flag:
                if len(temp_row) == len(tittle_of_csv_file.split(separator_character)):
                    print(f'{temp_row[0].ljust(len_id)}' + ' | '
                        + f'{temp_row[1].ljust(len_date)}' + ' | '
                        + (temp_row[2].replace("', '", ",").replace("\\\\", "\\")).ljust(len_title)
                        + ' | ' + temp_row[3].replace("', '", ",").replace("\\\\", "\\"))
                    count += 1
    print(f'Количество записей: {count}')

def question():
    print('Введине номер команды:\n'
          '1. Показать весь список заметок\n'
          '2. Показать заметки до определенной даты\n'
          '3. Показать заметки в диапазоне дат\n'
          '4. Показать заметки после определенной даты\n')
    answer = input('Выполняется команда: ')
    if answer.isdigit() == True:
        if int(answer) >= 0 and int(answer) <= 4:
            return answer
        else:
            print("Некорректный ввод")
            question()
    else:
        print("Некорректный ввод")
        question()

def answer_on_question():
    answer = question()
    match answer:
        case '1':
            date_start = ['0000', '01', '01', '00', '00', '00']
            date_end = ['9999', '12', '31', '23', '59', '59']
            full_date = [date_start, date_end]
            return full_date
        case '2':
            date_start = ['0000', '01', '01', '00', '00', '00']
            date_end = date_selection("окончания")
            full_date = [date_start, date_end]
            return full_date
        case '3':
            date_start = date_selection("начала")
            date_end = date_selection("окончания")
            full_date = [date_start, date_end]
            return full_date
        case '4':
            date_start = date_selection("начала")
            date_end = ['9999', '12', '31', '23', '59', '59']
            full_date = [date_start, date_end]
            return full_date
