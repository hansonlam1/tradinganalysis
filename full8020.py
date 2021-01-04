#detailed 8020 to include analysis of trigger
import pandas as pd
import basedf as basedf

def full8020(prioropen, priorhigh, priorlow, priorclose, todayopen, high, low, close):

    min_perc = 0.20
    max_perc = 0.80
    priordayrange = priorhigh - priorlow

    if priordayrange == 0:
        r = 'notrade'
    else:
        o_perc = (prioropen - priorlow)/priordayrange
        c_perc = (priorclose - priorlow)/priordayrange

        #only need to check non gaps for triggers
        if prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen < priorlow and low <= priorlow and close > priorlow:
            r = 'long_yesgap_win'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen >= priorlow and low <= priorlow and close > priorlow:
            r = 'long_nogap_trigger_win'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen >= priorlow and low > priorlow and close > priorlow:
            r = 'notrigger'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen < priorlow and close <= priorlow:
            r = 'long_yesgap_loss'

        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen >= priorlow and low <= priorlow and close <= priorlow:
            r = 'long_nogap_trigger_loss'
        elif prioropen > priorclose and c_perc < min_perc and o_perc > max_perc \
            and todayopen >= priorlow and low > priorlow and close <= priorlow:
            r = 'notrigger'

        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen > priorhigh and close < priorhigh:
            r = 'short_yesgap_win'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen <= priorhigh and high >= priorhigh and close < priorhigh:
            r = 'short_nogap_trigger_win'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen <= priorhigh and high < priorhigh and close < priorhigh:
            r = 'notrigger'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen > priorhigh and close >= priorhigh:
            r = 'short_yesgap_loss'

        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen <= priorhigh and high >= priorhigh and close >= priorhigh:
            r = 'short_nogap_trigger_loss'
        elif priorclose > prioropen and c_perc > max_perc and o_perc < min_perc \
            and todayopen <= priorhigh and high < priorhigh and close >= priorhigh:
            r = 'notrigger'
        else:
            r = 'notrigger'

    return r


def runfull8020test(df):
    df['TradeGap8020'] = df.apply(lambda x: full8020(x['PriorOpen']
    ,x['PriorHigh'],x['PriorLow'],x['PriorClose'],x['Open']
    ,x['High'],x['Low'],x['Close']),axis=1)

    
    table = pd.pivot_table(df, index=['TradeGap8020'], aggfunc='count')
    print(table['Close'])


if __name__ == "__main__":
    df = basedf.prepcoredata()
    runfull8020test(df)
