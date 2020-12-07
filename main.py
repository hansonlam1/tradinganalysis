# setup the main dataframe
import datetime
import os
import pandas as pd

import calculations as calc
import tradecalcs as tradecalcs

PATH = './data/'

def prepcoredata():

    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume','Adjustment']
    df = pd.DataFrame(columns=columns)

    for csvfile in os.listdir(PATH):
        if csvfile.endswith('.csv'):
            t = pd.read_csv(PATH+csvfile)
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

def run8020test(df):

    df['Trigger8020'] = df.apply(lambda x: tradecalcs.trigger8020(x['PriorHigh'],
        x['PriorLow'],x['PriorOpen'],x['PriorClose']),axis=1)

    df['Trade8020'] = df.apply(lambda x: tradecalcs.trade8020(x['Close'],
        x['PriorHigh'],x['PriorLow'],x['PriorClose'],x['Trigger8020']),axis=1)

    df.shape
    df.head(20)

    table = pd.pivot_table(df, index=['Trade8020'], aggfunc='count')
    print(table['Close'])


if __name__ == "__main__":
    df = prepcoredata()
    run8020test(df)
