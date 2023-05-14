import csv

def file_csv_to_list(file_name):
    with open(file_name, encoding='utf-8') as file:
        reader = csv.reader(file)
        temp_list = []
        for row in reader:
            if len(row) > 0:
                temp_list.append(str(row))
        return temp_list
