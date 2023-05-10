from Models.get_date import get_date


def test_line_from_csv(line_from_csv, separator_character):
    index_A = line_from_csv.find(separator_character)
    d = get_date()
    if index_A > 0:
        index_B = line_from_csv.find(separator_character, (index_A + 1))
        if index_B > 0 and ((index_B - index_A - 1) == (len(d))):
            return True
        else:
            return False
    else:
        return False
