from Models.string_to_list import string_to_list


def get_last_id(temp_list, separator_character):
    id = 0
    if len(temp_list) > 1:
        for i in range(1, len(temp_list)):
            temp_row = string_to_list(temp_list[i], separator_character)
            if len(temp_row) == 3:
                if int(temp_row[0]) > id:
                    id = int(temp_row[0])
    return id
