# 实验 7 Pandas 数据预处理

### 实验目的

1. 检测数据中存的重复值、缺失值和异常值。
1. 处理数据中存的重复值、缺失值和异常值。

### 实验时间和地点

2 课时，计算机机房 C2-416

实验内容  
**数据来源：科比布莱恩特 20 年职业篮球生涯中的投篮命中率相关数据。[https://www.kaggle.com/c/kobe-bryant-shot-selection](https://www.kaggle.com/c/kobe-bryant-shot-selection)。**  
该数据的终极任务是预测是否进球（shot_made_flag），因此有 5000 个 shot_made_flags 缺失。  
本题要求读懂数据并对数据进行**预处理**。  
变量说明：

|     | 字段               | 含义                                                |
| --- | ------------------ | --------------------------------------------------- |
| 1   | action_type        | 动作类型（细分类，用什么方式投的篮）                |
| 2   | combined_shot_type | 动作类型（结合什么方式投篮）                        |
| 3   | game_event_id      | 事件 ID                                             |
| 4   | game_id            | 比赛 ID                                             |
| 5   | lat                | 纬度                                                |
| 6   | loc_x              | 球场上位置的横坐标                                  |
| 7   | loc_y              | 球场上位置的纵坐标                                  |
| 8   | lon                | 经度                                                |
| 9   | minutes_remaining  | 本节剩余时间（分钟部分）                            |
| 10  | period             | 节                                                  |
| 11  | playoffs           | 是否为季后赛                                        |
| 12  | season             | 赛季                                                |
| 13  | seconds_remaining  | 本节剩余时间（秒钟部分）                            |
| 14  | shot_distance      | 投篮距离篮筐的距离                                  |
| 15  | shot_made_flag     | 是否进球                                            |
| 16  | shot_type          | 2 分球/3 分球区域                                   |
| 17  | shot_zone_area     | 投篮区域（左、中、右）                              |
| 18  | shot_zone_basic    | 投篮区域（场地位置，例如禁区、中场等）              |
| 19  | shot_zone_range    | 投篮距离范围                                        |
| 20  | team_id            | 球队 ID                                             |
| 21  | team_name          | 队名                                                |
| 22  | game_date          | 比赛日期                                            |
| 23  | matchup            | 比赛双方队名（用@分隔代表客场，用 VS 分隔代表主场） |
| 24  | opponent           | 对手队名                                            |
| 25  | shot_id            | 进球 id/镜头 ID                                     |

处理建议(请自己根据题目和分析来进行，顺序)：

1. 导入数据、查看数据信息，进行数据探索
1. 将字段 game_date 改为 datetime 类型
1. 将 shot_made_flag 值为空的记录放入另一个 DataFrame，并保存
1. 删除 shot_made_flag 值为空的记录
1. 增加、删除或改写一些字段，去除一些不完整的数据。

比如某些 ID、重复的位置信息、重复的对手信息，列的值没有变化的列；添加：主/客场，本节剩余比赛时间等。

1. 删除异常值的数据（可使用箱式图查看异常数据）
1. 填充缺失值
1. 分析字段间的相关性
1. 画出散点图来分析(loc_x, loc_y)和 (lat, lon)的关系
1. 计算每节的命中率，计算各个位置的命中率，计算进球方式的命中率

### 实验原理（理论支持）

- 科比在职业生涯中始终在湖人队效力，故球队 ID 和队名没有必要存在。

```Python
kobe=kobe_data.drop(['team_id','team_name'],axis=1)
```

- 比赛双方队名在 matchup 和对手队名 opponent 重复出现，可以只保留 opponent，但应当增加新的字段“主/客场”

```Python
kobe["home"]=kobe.matchup.apply(lambda x:0 if x[4]=='@' else 1)
kobe=kobe.drop(['matchup'],axis=1)
```

### 实验步骤

1. 打开 Spyder 或 Jupyter NoteBook
2. 新建 3.输入 4.保存 5.运行

### 实验报告要求

    实验报告以电子文档形式提交。

实验报告主要内容：**思路（重点，说明处理的方式、原因和效果）**，主要数据结构说明，运行结果和过程记录、**实验总结（不少于 200 字）。**  
**同时提交源代码（独立文件）**
