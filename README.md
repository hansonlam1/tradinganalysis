# tradinganalysis
Gathering basic statistics for a variety of trading ideas.

# Key Notes
Market data is daily data extracted from IB TWS in csv format

# To Run
- basedf.py contains generic calculations applicable to various strategies
- use settings.py to set the path to the data
- run a specific strategy using ```python <filename>```

# Strategies

- basic8020: intraday play on exhaustion of previous days move
- gapfill: how often does an opening gap get filled
- gap8020: does a gap open after 8020 result in a 8020 win?
- 8020continuation: does a big push on day 1 result in day 2 follow through?
