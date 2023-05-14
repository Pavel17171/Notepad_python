import os

def create_file_csv(file_name, tittle_of_csv_file ):
    if not os.path.exists(file_name):
        f = open(file_name, 'w', encoding='utf-8')
        f.write(tittle_of_csv_file )
        f.close()
    else:
        if os.stat(file_name).st_size < 1:
            with open(file_name, 'a+', encoding='utf-8') as file:
                file.write(tittle_of_csv_file)
                file.close()
