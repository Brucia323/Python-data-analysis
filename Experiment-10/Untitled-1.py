import pandas
from pandas.core.frame import DataFrame
data = pandas.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
# print(data.isnull().any())
target = data['Churn']
basicData = DataFrame()
# basicData['customerID'] = data['customerID']
basicData['gender'] = data['gender']
basicData['SeniorCitizen'] = data['SeniorCitizen']
basicData['Partner'] = data['Partner']
basicData['Dependents'] = data['Dependents']
basicData['tenure'] = data['tenure']
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
