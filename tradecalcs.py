import datetime as dt
import pandas as pd


def trigger8020(priorhigh, priorlow, prioropen, priorclose):
    min_perc = 0.20
    max_perc = 0.80
    priordayrange = priorhigh - priorlow
    # if priordayrange is 0 no need to calc
    if priordayrange == 0:
        t = 'not8020'
    else:
        o_perc = (prioropen - priorlow)/priordayrange
        c_perc = (priorclose - priorlow)/priordayrange
    
        if prioropen > priorclose and c_perc < min_perc and o_perc > max_perc:
            t = 'long'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc:
            t = 'short'
        else:
            t = 'not8020'
    return t


def trade8020(close, priorhigh, priorlow, priorclose, trigger8020):

    if trigger8020 == 'long' and close > priorlow:
        r = 'longwin'
    elif trigger8020 == 'long' and close <= priorlow:
        r = 'longloss'
    elif trigger8020 == 'short' and close < priorhigh:
        r = 'shortwin'
    elif trigger8020 =='short' and close >= priorhigh:
        r = 'shortloss'
    else:
        r = 'notrade'

    return r