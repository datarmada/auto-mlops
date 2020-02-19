import datetime

def get_current_normalized_date():
    current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
    return current_date