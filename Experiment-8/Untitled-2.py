from matplotlib.pyplot import figure, plot, scatter, show, subplot, title
from numpy import array, where
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv
from sklearn import cluster, metrics

data = read_csv("wine.data", names=['identifier', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
                'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline'])  # 酒精,苹果酸,灰,灰分的碱度,镁,总酚,黄酮类,非黄酮酚,原花青素,颜色强度,色调,稀释酒的OD280/OD315,脯氨酸
y = data['identifier']
y = y.replace(1, 0)
y = y.replace(2, 1)
y = y.replace(3, 2)
y = array(y)
X = array(data.drop(['identifier'], axis=1))
kmeans = cluster.KMeans(n_clusters=3)
kmeans.fit(X)
y_pred = kmeans.predict(X)
# 样本距离最近的聚类中心的总和
inertias = kmeans.inertia_

# 调整后的兰德指数
adjusted_rand_s = metrics.adjusted_rand_score(y, y_pred)

# 互信息
mutual_info_s = metrics.mutual_info_score(y, y_pred)

# 调整后的互信息
adjusted_mutual_info_s = metrics.adjusted_mutual_info_score(y, y_pred)

# 同质化得分
homogeneity_s = metrics.homogeneity_score(y, y_pred)

# 完整性得分
completeness_s = metrics.completeness_score(y, y_pred)

# V-measure得分
v_measure_s = metrics.v_measure_score(y, y_pred)

# 平均轮廓系数
silhouette_s = metrics.silhouette_score(X, y_pred, metric='euclidean')

# Calinski 和 Harabaz 得分


df_metrics = DataFrame([[inertias, adjusted_rand_s, mutual_info_s, adjusted_mutual_info_s, homogeneity_s, completeness_s, v_measure_s, silhouette_s]],
                       columns=['ine', 'tARI', 'tMI', 'tAMI', 'thomo', 'tcomp', 'tv_m', 'tsilh'])

print(df_metrics)


# 模型可视化
centers = kmeans.cluster_centers_
# 颜色设置
colors = ['green', 'pink', 'blue']
# 创建画布
figure(figsize=(12, 6))
titles = ['Real', 'Predict']
for j, y_ in enumerate([y, y_pred]):
    subplot(1, 2, j+1)
    title(titles[j])
    # 循环读类别
    for i in range(3):
        # 找到相同的索引
        index_sets = where(y_ == i)
        # 将相同类的数据划分为一个聚类子集
        cluster = X[index_sets]
        # 展示样本点
        scatter(cluster[:, 0], cluster[:, 1], c=colors[i], marker='.')
        print(str(len(cluster))+" "+colors[i])
        if j == 1:
            # 簇中心
            plot(centers[i][0], centers[i][1], 'o',
                 markerfacecolor=colors[i], markeredgecolor='k', markersize=6)
show()
