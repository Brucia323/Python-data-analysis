from pandas.io.parsers import read_csv


breast_cancer_wisconsin = read_csv("breast-cancer-wisconsin.data", names=[
                                   '身份证号码', '半径', '纹理', '周长', '面积', '平滑度', '紧凑性', '凹度', '凹点', '对称性', '分形维数'])
