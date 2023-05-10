import os


def create_file_csv(file_name):
    if not os.path.exists(file_name):
        f = open(file_name, 'w', encoding='utf-8')
        f.write("ID;DATE;TEXT")
        f.close()
    else:
        if os.stat(file_name).st_size < 1:
            with open(file_name, 'a+', encoding='utf-8') as file:
                file.write('ID;DATE;TEXT')
                file.close()
