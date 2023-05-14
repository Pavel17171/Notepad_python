from Models.string_line_to_list import string_line_to_list

def string_to_list(s, ch):
    new_list = []
    error_text = (f"Ошибка в строке! Содержание строки: {s[2:-2]}")
    try:
        new_list = string_line_to_list(s, ch)
    except:
        new_list.append(error_text)
    return new_list
