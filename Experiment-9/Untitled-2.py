from pandas.io.parsers import read_csv
from sklearn import datasets, model_selection, naive_bayes, neighbors, svm

breast_cancer_wisconsin = datasets.load_breast_cancer()
x_train, x_test, y_train, y_test = model_selection.train_test_split(
    breast_cancer_wisconsin.data, breast_cancer_wisconsin.target, test_size=0.25)
gaussian = naive_bayes.GaussianNB()
bernoulli = naive_bayes.BernoulliNB()
complement = naive_bayes.ComplementNB()
categorical = naive_bayes.CategoricalNB()
multinomial = naive_bayes.MultinomialNB()
linearsvc = svm.LinearSVC()
kneighborsClassifier = neighbors.KNeighborsClassifier()
