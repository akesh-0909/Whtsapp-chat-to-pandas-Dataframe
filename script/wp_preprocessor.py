import re
import pandas as pd
import helper
def preprocessor(path):
    data = helper.filereader(path)
    pattern ='\d{1,2}\/\d{1,2}\/\d{2},\s\d{1,2}:\d{2}\s(?:am\s|pm\s)?-\s'
    messages = re.split(pattern,data)[1:]
    dates = re.findall(pattern,data)
    df = pd.DataFrame({'Dates':dates,'Messages':messages})
    usernames = list()
    messages = list()
    
    for i in df['Messages']:
        values = re.split('([\w\W]+):\s',i)

        if len(values)>2:
            usernames.append(values[1])
            messages.append(values[2])
        else:
            usernames.append('Notifications')
            messages.append(values[0])
    df['User'] = usernames
    df['Message'] = messages
    df.drop(columns='Messages',inplace=True)
    
    df['Dates'] = helper.datetime(df['Dates'])
    return df