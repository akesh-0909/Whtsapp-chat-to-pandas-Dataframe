import pandas as pd
def datetime(data):
    try:

        datetime_data = pd.to_datetime(data,format="%m/%d/%y, %I:%M %p - ")

    except:
        try:
            datetime_data = pd.to_datetime(data,format="%m/%d/%y, %H:%M - ")
        except ValueError:
            raise ValueError('Invalid date-time format')

    return datetime_data

def filereader(path):
    file = open(path,'r',encoding='utf-8')
    data = file.read()
    return data