import datetime

def get_date():
    now_date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return now_date
