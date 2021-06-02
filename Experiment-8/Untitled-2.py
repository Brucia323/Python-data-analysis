from pandas.io.parsers import read_csv

data = read_csv("wine.data", names=['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
                'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline'])  # 酒精,苹果酸,灰,灰分的碱度,镁,总酚,黄酮类,非黄酮酚,原花青素,颜色强度,色调,稀释酒的OD280/OD315,脯氨酸
import sklearn
sklearn