from Models.get_date import get_date

def test_line_from_csv(line_from_csv, separator_character):
    max_len_tittle = 16
    text_separator = '"'
    d = get_date()
    flag = False
    try:
        index_A = line_from_csv.find(separator_character)
        index_B = index_A + 1 + len(d)
        index_C = line_from_csv.find(separator_character + text_separator, index_B + 1)
        if line_from_csv[index_A] == separator_character \
                and line_from_csv[index_B] == separator_character \
                and line_from_csv[index_C] == separator_character \
                and index_C - index_B <= max_len_tittle:
            if line_from_csv[index_B + 1] == text_separator \
                    and line_from_csv[index_C - 1] == text_separator \
                    and line_from_csv[index_C + 1] == text_separator \
                    and line_from_csv[len(line_from_csv) - 3] == text_separator:
                flag = True
        return flag
    except:
        return flag