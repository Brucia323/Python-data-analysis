# In[0]:
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from pandas.core.reshape.concat import concat

plt.rcParams['font.sans-serif'] = ['simhei']
# In[1]:
train = pd.read_csv("./bike/train.csv", sep=",", encoding='utf8')
test = pd.read_csv("./bike/test.csv", sep=",", encoding='utf8')
# In[2]:
print(train)
print(test)
# In[3]:
datetime1 = pd.to_datetime(train['datetime'], format='%Y/%m/%d')
date = datetime1.apply(lambda x: datetime.strftime(x, "%Y/%m/%d"))
train['date'] = date
date = train['count'].groupby(train['date']).sum()
plt.plot(date)
plt.show()
train = train.drop(['date'], axis=1)
# In[4]:
casual = sum(train['casual'])
registered = sum(train['registered'])
count = [casual, registered]
plt.pie(count, labels=['非会员租车人次:'+str(casual), '会员租车人次:'+str(registered)])
plt.show()
# In[5]:
train['hour'] = datetime1.dt.hour
workingday = train[train['workingday'] == 1]
workingday = workingday['count'].groupby(workingday['hour']).sum()
holiday = train[train['workingday'] == 0]
holiday = holiday['count'].groupby(holiday['hour']).sum()
plt.plot(workingday, label='工作日')
plt.plot(holiday, label='休息日')
plt.legend()
plt.show()
train = train.drop(['hour'], axis=1)
# In[6]:
trainstd = train['count'].std()*3
trainmean = train['count'].mean()
train = train[train['count'].between(trainmean-trainstd, trainmean+trainstd)]
# In[7]:
temp = train['count'].groupby(train['temp']).sum()
plt.plot(temp)
plt.show()
# In[8]:
data = concat([train, test])
# In[9]:
data = data.drop(['atemp', 'humidity', 'casual', 'registered'], axis=1)
# In[10]:
"""二选一"""
data = data.fillna(method='pad')
# data=data.fillna(method='bfill')
# In[11]:
data['windspeed'].replace(0, data['windspeed'].mean(), inplace=True)
# In[12]:
data.to_csv("result.csv", sep=',', index=False, header=True)
