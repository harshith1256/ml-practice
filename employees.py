import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from  sklearn.metrics import accuracy_score
scalar = StandardScaler()
model = LogisticRegression()

df = pd.read_csv('employees.csv')
print(df)

df_encoded = pd.get_dummies(df)
print(df_encoded)

X = df_encoded.drop('will_leave_Yes', axis=1)
Y = df_encoded['will_leave_Yes']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

model.fit(X_train_scaled,Y_train)
predictions = model.predict(X_test_scaled)
print(predictions)

accuracy = accuracy_score(Y_test, predictions)
print(accuracy)

print(model.coef_)
print(model.intercept_)