def ask_yes_no(text):
    print(text)
    answer = input("Y или Д - да \nN или Н - нет \n")
    answer = answer.lower()
    if answer == 'y' or answer == 'д':
        return True
    elif answer == 'n' or answer == 'н':
        return False
    else:
        ask_yes_no(text)
        