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
n = len(etf_price_values)
cid = 0 #当前点的方向
fpn = 0 #第一个点的索引
highIndex = 0 #波峰点的索引
lowIndex = 0 #波谷点的索引
for i in range(n):
    if etf_price_values[i] > etf_price_values[0] * (1+0.15):
        cid = 1
        fpn = i
        highIndex = i
        break
    if etf_price_values[i] < etf_price_values[0] * (1-0.15):
        cid = -1
        fpn = i
        lowIndex = i
        break
fcid = cid #第一个点的方向
high=[]#波峰点的索引集合
low=[]#波谷点的索引集合
for i in range(fpn+1,n):
    if cid > 0:
        if etf_price_values[i] > etf_price_values[highIndex]:
            highIndex = i
        if etf_price_values[i] < etf_price_values[highIndex] * (1-0.15):
            high.append(highIndex)
            lowIndex = i
            cid = -1
    if cid < 0:
        if etf_price_values[i] < etf_price_values[lowIndex]:
            lowIndex = i
        if etf_price_values[i] > etf_price_values[lowIndex] * (1+0.15):
            low.append(lowIndex)
            highIndex = i
            cid = 1
peakIndex = []
peakIndex.extend(low)
peakIndex.extend(high)
peakIndex.append(0-1)
peakIndex.append(n)
peakIndex.sort()
label = []

def isin(a,l):
    result = False
    for i in l:
        if i == a:
            result = True
            break
    return result

for i in range(n):
    if isin(i,peakIndex) == True:
        label.append(0)
        fcid = fcid * (-1)
    else:
        label.append(fcid)
