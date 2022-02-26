import pandas as pd
import numpy as np

etf = pd.read_csv(r'.\zz500etf.csv',index_col=0,parse_dates=True)
etf_price = etf.iloc[:,0]

#做维度扩张，扩张长度是11天
for i in range(1,12):
    etf = pd.concat([etf,etf.iloc[:,0].shift(i)],axis=1)

etf = etf.dropna()

#做论文中提及的标准化方法
etf_ = pd.DataFrame((etf.values-etf.mean(axis=1).values.reshape(-1,1))/etf.mean(axis=1).values.reshape(-1,1)
                    ,index=etf.index,columns=etf.columns)

etf_price_values = etf_price.values

#找到局部最小值和局部最大值，最大值和最小值一定是交替的
l=[]
for i in range(1,len(etf_price_values)-1):
    if etf_price_values[i] > etf_price_values[i-1] and etf_price_values[i] > etf_price_values[i+1]:
        l.append(etf_price_values[i])
    elif etf_price_values[i] < etf_price_values[i-1] and etf_price_values[i] < etf_price_values[i+1]:
        l.append(etf_price_values[i])
l = np.array(l)

del_values_index=[]
for i in range(1,len(l)-1):
    if np.abs((l[i]-l[i-1])/l[i-1]) < 0.15 and np.abs((l[i]-l[i+1])/l[i]) < 0.15:
        if np.abs((l[i]-l[i-1])/l[i-1]) < 0.15:
            del_values_index.extend([i-1,i])
        elif np.abs((l[i]-l[i+1])/l[i]) < 0.15:  
            del_values_index.extend([i+1,i])    