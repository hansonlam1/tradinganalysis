#does a gap open after 8020 result in a 8020 win?
import pandas as pd
import basedf as basedf

def tradegap8020(prioropen, priorhigh, priorlow, priorclose, todayopen, high, low, close):

    min_perc = 0.20
    max_perc = 0.80
    priordayrange = priorhigh - priorlow

    if priordayrange == 0:
        r = 'notrade'
    else:
        o_perc = (prioropen - priorlow)/priordayrange
        c_perc = (priorclose - priorlow)/priordayrange

        if prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen < priorlow and close > priorlow:
            r = 'long_yesgap_win'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen >= priorlow and close > priorlow:
            r = 'long_nogap_win'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen < priorlow and close <= priorlow:
            r = 'long_yesgap_loss'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen >= priorlow and close <= priorlow:
            r = 'long_nogap_loss'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen > priorhigh and close < priorhigh:
            r = 'short_yesgap_win'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen <= priorhigh and close < priorhigh:
            r = 'short_nogap_win'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen > priorhigh and close >= priorhigh:
            r = 'short_yesgap_loss'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen <= priorhigh and close >= priorhigh:
            r = 'short_nogap_loss'
        else:
            r = 'notrade'

    return r


def rungap8020test(df):
    df['TradeGap8020'] = df.apply(lambda x: tradegap8020(x['PriorOpen']
    ,x['PriorHigh'],x['PriorLow'],x['PriorClose'],x['Open']
    ,x['High'],x['Low'],x['Close']),axis=1)

    
    table = pd.pivot_table(df, index=['TradeGap8020'], aggfunc='count')
    print(table['Close'])


if __name__ == "__main__":
    df = basedf.prepcoredata()
    rungap8020test(df)
