from matplotlib import rcParams
from matplotlib.pyplot import bar, show, title
from pandas.core.frame import DataFrame
from pandas.io.parsers import read_csv

data = read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
# print(data.isnull().any())
target = data['Churn']
basicData = DataFrame()
basicData['customerID'] = data['customerID']
basicData['gender'] = data['gender']
basicData['SeniorCitizen'] = data['SeniorCitizen']
basicData['Partner'] = data['Partner']
basicData['Dependents'] = data['Dependents']
basicData['tenure'] = data['tenure']
basicData['Churn'] = data['Churn']
businessData = DataFrame()
businessData['PhoneService'] = data['PhoneService']
businessData['MultipleLines'] = data['MultipleLines']
businessData['InternetService'] = data['InternetService']
businessData['OnlineSecurity'] = data['OnlineSecurity']
businessData['OnlineBackup'] = data['OnlineBackup']
businessData['DeviceProtection'] = data['DeviceProtection']
businessData['TechSupport'] = data['TechSupport']
businessData['StreamingTV'] = data['StreamingTV']
businessData['StreamingMovies'] = data['StreamingMovies']
contractData = DataFrame()
contractData['Contract'] = data['Contract']
contractData['PaperlessBilling'] = data['PaperlessBilling']
contractData['PaymentMethod'] = data['PaymentMethod']
contractData['MonthlyCharges'] = data['MonthlyCharges']
contractData['TotalCharges'] = data['TotalCharges']
rcParams['font.sans-serif'] = ['SimHei']
y = basicData.groupby(['gender', 'Churn'])['gender'].count()
bar(['Female+No', 'Female+Yes', 'Male+No', 'Male+Yes'], y)
title('性别')
show()
y = basicData.groupby(['SeniorCitizen', 'Churn'])['SeniorCitizen'].count()
bar(['0+No', '0+Yes', '1+No', '1+Yes'], y)
title('是否为老年人')
show()
y = basicData.groupby(['Partner', 'Churn'])['Partner'].count()
bar(['No+No', 'No+Yes', 'Yes+No', 'Yes+Yes'], y)
title('是否有配偶')
show()
y = basicData.groupby(['Dependents', 'Churn'])['Dependents'].count()
bar(['No+No', 'No+Yes', 'Yes+No', 'Yes+Yes'], y)
title('是否有家庭')
show()
y = basicData.groupby(['tenure', 'Churn'])['tenure'].count()
x = list()
for i in range(len(y)//2+1):
    x.append(str(i)+'+No')
    if(i > 0):
        x.append(str(i)+'+Yes')
bar(x, y)
title('入网月数')
show()
