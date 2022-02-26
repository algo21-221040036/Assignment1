import pandas as pd
etf = pd.read_csv(r'.\zz500etf.csv',index_col=0,parse_dates=True)

for i in range(1,12):
    etf = pd.concat([etf,etf.iloc[:,0].shift(i)],axis=1)

etf = etf.dropna()