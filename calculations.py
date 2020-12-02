import datetime as dt
import pandas as pd


def daydir(o_price, c_price):
    if o_price > c_price:
        direction = 'down'
    elif c_price > o_price:
        direction = 'up'
    else:
        direction = 'flat'
    return direction


def dayrange(high, low):
    rng = high - low
    return rng


def nextday8020(o,h,l,c):
    min_perc = 0.20
    max_perc = 0.80
    dayrange = h - l
    # if dayrange is 0 no need to calc
    if dayrange == 0:
        d = 'no setup'
    else:
        o_perc = (o - l)/dayrange
        c_perc = (c - l)/dayrange
    
        if o > c and c_perc < min_perc and o_perc > max_perc:
            d = 'long'
        elif c > o and c_perc > max_perc and o_perc < min_perc:
            d = 'short'
        else:
            d = 'no setup'
    return d


def opengap(df):
    # add a column with the opening gap
    df['opengap'] = df['Open'] - df['Close'].shift()
    df['opengap'].fillna(0, inplace=True)
    df['opengap_perc'] = (df['opengap'] / df['Close'].shift()) * 100
    df['gapclosed'] = (df['Low'] <= df['Close'].shift()) & (df['High'] >= df['Close'].shift())
    return df


def smaclose(df, s, f):
    df['fast_sma'] = df['Close'].rolling(f).mean()
    df['slow_sma'] = df['Close'].rolling(s).mean()
    #also includes an indicator based on something I read from Linda Raschke
    df['lbrosc'] = df['fast_sma'] - df['slow_sma']
    df['lbrosc_signal'] = df['lbrosc'].rolling(16).mean()
    return df


def simpletrend(df, t):
    #add a sma
    df['simplesma'] = df['Close'].rolling(t).mean()
    #yesterday did it close above or below the sma
    df['uptrend'] = (df['Close'].shift() > df['simplesma'])
    return df
