def date_selection(text):
    end_year = input_year(f"Введите год {text} поиска в формате: гггг\n")
    end_month = input_month(f"Введите месяц {text} поиска в формате: мм\n")
    end_day = input_day(f"Введите день {text} поиска в формате: дд\n", end_year, end_month)
    end_hour = input_hour(f"Введите час {text} поиска в 24 часовом формате: чч\n")
    end_minutes = input_minutes(f"Введите минуты {text} поиска в формате: мм\n")
    end_seconds = input_seconds(f"Введите секунды {text} поиска в формате: cc\n")
    full_date = [end_year, end_month, end_day, end_hour, end_minutes, end_seconds]
    return full_date

def input_year(text):
    flag = False
    while flag == False:
        year = input(text)
        if year.isdigit() == True and len(year) == 4:
            flag = True   
        else:
            print("Некорректный ввод")
    return year

def input_month(text):
    flag = False
    while flag == False:
        month = input(text)
        if month.isdigit() == True and len(month) == 2:
            if int(month) >= 1 and int(month) <= 12:  
                flag = True
            else:
                print("Номер месяца от 01 до 12 включительно")     
        else:
            print("Некорректный ввод")
    return month

def input_day(text, year, month):
    flag = False
    month31 = ['01', '03', '05', '08', '10', '12']
    month30 = ['04', '06', '07', '09', '11']
    len_month = 0
    if month in month31:
        len_month = 31
    elif month in month30:
        len_month = 30
    elif month == '02':
        len_month = size_of_February(year)
    while flag == False:
        day = input(text)
        if day.isdigit() == True and len(day) == 2:
            if int(day) <= len_month:
                    flag = True
            else:
                print("В этом месяце меньше дней")          
        else:
            print("Некорректный ввод")
    return day

def input_hour(text):
    flag = False
    while flag == False:
        hour = input(text)
        if hour.isdigit() == True and len(hour) == 2:
            if int(hour) >= 0 and int(hour) <= 23:  
                flag = True
            else:
                print("Часы от 00 до 23 включительно")       
        else:
            print("Некорректный ввод")
    return hour

def input_minutes(text):
    flag = False
    while flag == False:
        minutes = input(text)
        if minutes.isdigit() == True and len(minutes) == 2:
            if int(minutes) >= 0 and int(minutes) <= 59:  
                flag = True
            else:
                print("Минуты от 00 до 59 включительно")
        else:
            print("Некорректный ввод")
    return minutes

def input_seconds(text):
    flag = False
    while flag == False:
        seconds = input(text)
        if seconds.isdigit() == True and len(seconds) == 2:
            if int(seconds) >= 0 and int(seconds) <= 59:  
                flag = True
            else:
                print("Секунды от 00 до 59 включительно")    
        else:
            print("Некорректный ввод")
    return seconds

def size_of_February(year):
    year = int(year)
    if year % 4 != 0:
        return 28
    elif year % 100 == 0:
        if year % 400 == 0:
            return 29
        else:
            return 28
    else:
        return 29
