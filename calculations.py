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


def priordayvalues(df):
    df['PriorOpen'] = df['Open'].shift()
    df['PriorClose'] = df['Close'].shift()
    df['PriorHigh'] = df['High'].shift()
    df['PriorLow'] = df['Low'].shift()

    return df


def opengap(df):
    # add a column with the opening gap
    df['OpenGap'] = df['Open'] - df['Close'].shift()
    df['OpenGap'].fillna(0, inplace=True)
    df['OpenGap_Perc'] = (df['opengap'] / df['Close'].shift()) * 100
    df['GapClosed'] = (df['Low'] <= df['Close'].shift()) & (df['High'] 
        >= df['Close'].shift())
    return df


def smaclose(df, s, f):
    df['FastSMA'] = df['Close'].rolling(f).mean()
    df['SlowSMA'] = df['Close'].rolling(s).mean()
    #an indicator based on something from Linda Raschke
    #df['lbrosc'] = df['fast_sma'] - df['slow_sma']
    #df['lbrosc_signal'] = df['lbrosc'].rolling(16).mean()
    return df


def simpletrend(df, t):
    #add a sma
    df['SimpleSMA'] = df['Close'].rolling(t).mean()
    #yesterday did it close above or below the sma
    df['Uptrend'] = (df['Close'].shift() > df['simplesma'])
    return df