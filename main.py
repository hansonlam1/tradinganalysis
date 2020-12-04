# setup the main dataframe
import datetime
import os
import pandas as pd

import calculations as calc

PATH = './data/'

columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume','Adjustment']
df = pd.DataFrame(columns=columns)

for csvfile in os.listdir(PATH):
    if csvfile.endswith('.csv'):
        t = pd.read_csv(PATH+csvfile)
        df = df.append(t, sort=True)

df.drop_duplicates(subset=columns, keep='first', inplace=True)

# convert date column and sort
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values(by=['Date'], inplace=True, ascending=True)


# use lambda calcs where no dependencies on prior rows
df['daydirection'] = df.apply(lambda x: calc.daydir(x['Open'], x['Close']),
    axis=1)
df['dayrange'] = df.apply(lambda x: calc.dayrange(x['High'],
    x['Low']),axis=1)
df['today8020'] = df.apply(lambda x: calc.today8020(x['Open'],
    x['High'], x['Low'],x['Close']),axis=1)

# other calcs where prior day(s) are involved
df.shape