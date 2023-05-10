def string_to_list(s, ch):
    new_list = []
    index_start_text = s.find('"')
    index_finish_text = s.rfind('"')
    error_text = (f"Ошибка в строке! Содержание строки: {s[2:-2]}")
    if index_start_text > 0 and index_finish_text == len(s) - 3:
        if s.count(ch, 0, index_start_text) > 1:
            index_A = s.index(ch)
            index_B = s.index(ch, (index_A + 1))
            if index_start_text == index_B + 1:
                new_list.append(s[2:index_A])
                new_list.append(s[index_A+1:index_B])
                new_list.append(s[index_B+2:(len(s)-3)])
            else:
                new_list.append(error_text)
        else:
            new_list.append(error_text)
    else:
        new_list.append(error_text)
    return new_list
