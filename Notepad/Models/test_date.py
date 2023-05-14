def test_date(date_from_notepad, input_date):
    flag = False
    list_date = []
    date_from_notepad = date_from_notepad.split(" ")
    date_date = date_from_notepad[0].split('-')
    date_time = date_from_notepad[1].split(':')
    for i in date_date:
        list_date.append(i)
    for j in date_time:
        list_date.append(j)

    year_list = int(list_date[0])
    month_list = int(list_date[1])
    day_list = int(list_date[2])
    hour_list = int(list_date[3])
    minutes_list = int(list_date[4])
    seconds_list = int(list_date[5])

    year_date_start = int(input_date[0][0])
    month_date_start = int(input_date[0][1])
    day_date_start = int(input_date[0][2])
    hour_date_start = int(input_date[0][3])
    minutes_date_start = int(input_date[0][4])
    seconds_date_start = int(input_date[0][5])

    year_date_finish = int(input_date[1][0])
    month_date_finish = int(input_date[1][1])
    day_date_finish = int(input_date[1][2])
    hour_date_finish = int(input_date[1][3])
    minutes_date_finish = int(input_date[1][4])
    seconds_date_finish = int(input_date[1][5])

    if year_list > year_date_start and year_list < year_date_finish:   
        flag = True
    elif year_list == year_date_start:
        if month_list > month_date_start:
            flag = True
        elif month_list == month_date_start:
            if day_list > day_date_start:
                flag = True
            elif day_list == day_date_start:
                if hour_list > hour_date_start:
                    flag = True
                elif hour_list == hour_date_start:
                    if minutes_list > minutes_date_start:
                        flag = True
                    elif minutes_list == minutes_date_start:
                        if seconds_list >= seconds_date_start:
                            flag = True

    elif year_list == year_date_finish:
        if month_list < month_date_finish:
            flag = True
        elif month_list == month_date_finish:
            if day_list < day_date_finish:
                flag = True
            elif day_list == day_date_finish:
                if hour_list < hour_date_finish:
                    flag = True
                elif hour_list == hour_date_finish:
                    if minutes_list < minutes_date_finish:
                        flag = True
                    elif minutes_list == minutes_date_finish:
                        if seconds_list <= seconds_date_finish:
                            flag = True
    return flag
