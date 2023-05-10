def string_line_to_list(string_line, separator_character):
    new_list = []
    index_A = string_line.index(separator_character)
    index_B = string_line.index(separator_character, (index_A + 1))
    new_list.append(string_line[2:index_A])
    new_list.append(string_line[index_A+1:index_B])
    new_list.append(string_line[index_B+2:(len(string_line)-3)])
    return new_list
