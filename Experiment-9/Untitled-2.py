from pandas.io.parsers import read_csv
from sklearn import naive_bayes

breast_cancer_wisconsin = read_csv("breast-cancer-wisconsin.data", names=[
                                   '身份证号码', '半径', '纹理', '周长', '面积', '平滑度', '紧凑性', '凹度', '凹点', '对称性', '分形维数'])
breast_cancer_wisconsin = breast_cancer_wisconsin.drop(['身份证号码'], axis=1)
breast_cancer_wisconsin = breast_cancer_wisconsin.drop_duplicates()
breast_cancer_wisconsin = breast_cancer_wisconsin.reset_index(drop=True)
gaussian = naive_bayes.GaussianNB()
bernoulli = naive_bayes.BernoulliNB()
complement = naive_bayes.ComplementNB()
categorical = naive_bayes.CategoricalNB()
multinomial = naive_bayes.MultinomialNB()
