import pandas as pd

churn = pd.read_excel(r"""C:\Users\Admin\Downloads\deployment\CHURNDATA.xlsx""")

churn=churn.drop(['CUS_DOB','CUS_Customer_Since','CUS_Marital_Status', 'CIF','# total debit transactions for S1',
       '# total debit transactions for S2',
       '# total debit transactions for S3', 'total debit amount for S1',
       'total debit amount for S2', 'total debit amount for S3',
       '# total credit transactions for S1',
       '# total credit transactions for S2',
       '# total credit transactions for S3', 'total credit amount for S1',
       'total credit amount for S2', 'total credit amount for S3', 'total transactions', 'CUS_Target',
       'TAR_Desc'], axis=1)

churn=churn.dropna()

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
encoded = label_encoder.fit(churn['CUS_Gender'])
churn['CUS_Gender'] = encoded.transform(churn['CUS_Gender'])

churn['Status'] = churn['Status'].replace(to_replace='ACTIVE', value=1)
churn['Status'] = churn['Status'].replace(to_replace='CHURN', value=0)

x = churn.iloc[:,:8]
y = churn.iloc[:,8:]

from sklearn.model_selection import train_test_split
xtr, xte,ytr,yte = train_test_split(x,y, test_size=0.2, random_state = 1)

from sklearn.ensemble import RandomForestClassifier

model3 = RandomForestClassifier()
model3.fit(xtr, ytr.values.ravel())

expected = yte
predicted = model3.predict(xte)

# from sklearn import metrics
# print(metrics.classification_report(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))
#
# from sklearn.model_selection import cross_val_score
# accuracies = cross_val_score(estimator = model3, X = x,\
#      y = y, cv = 10)
# print("Accuracy Mean {} Accuracy Variance \
#      {}".format(accuracies.mean(),accuracies.std()))
#
# from sklearn.metrics import accuracy_score
# accuracy_score(expected, predicted)

import pickle
pickle.dump(model3, open('churn.pkl', 'wb'))

model = pickle.load(open('churn.pkl','rb'))
# pickle.dump(model3, open("churn.pkl", "wb"))
# model=pickle.load(open("churn.pkl", "rb"))