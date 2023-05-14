from Models.get_date import get_date

def list_to_csv(temp_list, file_name, tittle_of_csv_file):
    now_date = str((get_date()).replace(' ', '_')).replace(':', '-')
    reserve_file_name = str(f'reserve_{now_date}_{file_name}')

    with open(reserve_file_name, 'w', encoding='utf-8') as file:
        file.write(tittle_of_csv_file)
        for i in range(1, len(temp_list)):
            file.write('\n' + temp_list[i][2:-2].replace("', '", ",").replace("\\\\", "\\"))
        file.close()
    return reserve_file_name
