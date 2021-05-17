# In[1]:
from matplotlib.pyplot import plot, show
from numpy import arange
from pandas.core.tools.datetimes import to_datetime
from pandas.io.parsers import read_csv


data = read_csv("data.csv")
print(data)
print(data.describe())
# In[2]:
data['game_date'] = to_datetime(data['game_date'])
# In[3]:
shot_made_flag = data[data['shot_made_flag'].isnull()]
shot_made_flag.to_csv("shot_made_flag.csv")
# In[4]:
data = data.dropna(subset=['shot_made_flag'])
# In[5]:
kobe_data = data
kobe = kobe_data.drop(['team_id', 'team_name'], axis=1)
kobe['home'] = kobe['matchup'].apply(lambda x: 0 if x[4] == '@' else 1)
kobe = kobe.drop(['matchup'], axis=1)
kobe['remaining'] = data['minutes_remaining']*60+data['seconds_remaining']
kobe = kobe.drop(['seconds_remaining', 'minutes_remaining'], axis=1)
# In[6]:


def box_plot_outliers(data_ser, box_scale):
    # IQR即尺度*（上四分位点-下四分位点）
    IQR = box_scale*(data_ser.quantile(0.75)-data_ser.quantile(0.25))
    val_low = data_ser.quantile(0.25)-IQR  # 计算下边缘
    val_up = data_ser.quantile(0.75)+IQR  # 计算上边缘
    rule_low = (data_ser < val_low)  # 小于下边缘的值
    rule_up = (data_ser > val_up)  # 大于上边缘的值
    return (rule_low, rule_up), (val_low, val_up)


scale = 3
rule, value = box_plot_outliers(kobe['shot_distance'], box_scale=scale)
kobe=kobe.reset_index(drop=True)
index=arange(kobe['shot_distance'].shape[0])[rule[0]|rule[1]]
kobe=kobe.drop(index)
# In[7]:
kobe=kobe.fillna(method='pad')
# In[8]:
print(kobe.corr())
# In[9]:
plot((kobe['loc_x'], kobe['loc_y']), (kobe['lat'], kobe['lon']), '.')
# plot(kobe['lat'], kobe['lon'],'.')
show()
# In[10]:
