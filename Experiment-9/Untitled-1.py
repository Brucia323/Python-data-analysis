from pandas.io.parsers import read_csv
from sklearn import linear_model, metrics, model_selection

train = read_csv("kc_train.csv", names=['销售日期', '销售价格', '卧室数', '浴室数', '房屋面积',
                 '停车面积', '楼层数', '房屋评分', '建筑面积', '地下室面积', '建筑年份', '修复年份', '纬度', '经度'])
test = read_csv("kc_test.csv", names=['销售日期', '卧室数', '浴室数', '房屋面积',
                '停车面积', '楼层数', '房屋评分', '建筑面积', '地下室面积', '建筑年份', '修复年份', '纬度', '经度'])
train1, train2 = model_selection.train_test_split(train, test_size=0.25)
y = train1['销售价格']
x = train1.drop('销售价格', axis=1)
y2 = train2['销售价格']
x2 = train2.drop('销售价格', axis=1)
linearRegression = linear_model.LinearRegression()
model = linearRegression.fit(x, y)
y2_predict = model.predict(x2)
print("Explain variance score =", round(
    metrics.explained_variance_score(y2, y2_predict), 2))
print("R2 score =", round(metrics.r2_score(y2, y2_predict), 2))
test_predict = model.predict(test)
