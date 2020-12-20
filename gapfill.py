#how often does a gap from prior day fill?
import pandas as pd
import basedf as basedf


def gapfill(priorhigh, priorlow, open, high, low):

    if open < priorlow and high >= priorlow:
        r = 'gap down closed'
    elif open < priorlow and high < priorlow:
        r = 'gap down not closed'
    elif open > priorhigh and low <= priorhigh:
        r = 'gap up closed'
    elif open > priorhigh and low > priorhigh:
        r = 'gap up not closed'
    else:
        r = 'no gap'
    
    return r


def rungapfill(df):

    df['TradeGapFill'] = df.apply(lambda x: gapfill(x['PriorHigh'],
        x['PriorLow'],x['Open'],x['High'],x['Low']),axis=1)

    #df.shape
    #df.head(20)

    table = pd.pivot_table(df, index=['TradeGapFill'], aggfunc='count')
    print(table['Close'])


if __name__ == "__main__":
    df = basedf.prepcoredata()
    rungapfill(df)