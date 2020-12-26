# setup the main dataframe
import datetime
import os
import pandas as pd

import calculations as calc
import settings as s


def prepcoredata():

    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume','Adjustment']
    df = pd.DataFrame(columns=columns)

    for csvfile in os.listdir(s.PATH):
        if csvfile.endswith('.csv'):
            t = pd.read_csv(s.PATH+csvfile)
            df = df.append(t, sort=True)

    df.drop_duplicates(subset=columns, keep='first', inplace=True)

    # convert date column, sort and reindex
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by=['Date'], inplace=True, ascending=True)
    df.reset_index(drop=True, inplace=True)

    # establish some basic additional data columns
    df['DayDirection'] = df.apply(lambda x: calc.daydir(x['Open'], x['Close']),
        axis=1)
    df['DayRange'] = df.apply(lambda x: calc.dayrange(x['High'],
        x['Low']),axis=1)
    df = calc.priordayvalues(df)

    return df