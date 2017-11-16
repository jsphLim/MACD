import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

stock=pd.read_excel(r'C:\Users\sd\Documents\WeChat Files\cherstalst\Files\data.xlsx',header=0,index_col=0)
# with open(r'data.pkl','rb') as f:
#     stock = pickle.load(f)
#
# print(stock)
stock = stock[0]

def sma(data,period):
    a=pd.DataFrame(data).copy()
    a=a.rolling(period).mean()
    return a

b=sma(stock,2)

def wma(data,weight):
    wei=np.array(weight)
    k=len(wei)
    wma=pd.Series(data=None,index=data.index)
    for i in range(k-1,len(data)): 
        wma[i]=sum(wei*data[(i-k+1):(i+1)]) 
    return wma

b=wma(stock,[0.2,0.2,0.2,0.2,0.2])

def ewma(data,period):
    wei=2/(period+1)
    ewma=pd.Series(data=None,index=data.index)
    ewma[period-1]=data[:period+1].mean()
    for i in range(period,len(data)):
        ewma[i]=wei*data[i]+(1-wei)*ewma[i-1]
    return ewma

b=ewma(stock,12)

dif=ewma(stock,12)-ewma(stock,26)

dea=ewma(dif.dropna(),9)

macd=(dif-dea)*2

print(dif['2017-03-14':])

plt.rcParams['axes.unicode_minus']=False #设置负数显示


dif.plot(label='DIF',color='b')
dea.plot(label='DEA',color='r')
macd.plot(kind='bar',color='y')
# plt.plot(dif['2017-03-14':],label='DIF',color='b')
# plt.plot(dea['2017-03-14':],label='DEA',color='r')
# plt.bar(left=macd['2017-03-14':],height=macd['2017-03-14':],label='MACD',color='y')
# plt.title("MACD")
plt.xlabel('Date')
plt.show()
