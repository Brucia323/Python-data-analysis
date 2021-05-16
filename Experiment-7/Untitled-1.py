# In[1]:
from matplotlib.pyplot import boxplot, show
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
boxplot(kobe['shot_distance'])
show()
# %%
