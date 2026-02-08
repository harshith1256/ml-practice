import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()

my_df = pd.read_csv("sample.csv")
print(my_df)
my_df_encoded = pd.get_dummies(my_df)
print(my_df_encoded)
x = my_df_encoded.drop("pass_Yes", axis=1)
y = my_df_encoded["pass_Yes"]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

x_train_scaled = scalar.fit_transform(x_train)
x_test_scaled = scalar.transform(x_test)

print(x_test_scaled)
print(x_test_scaled)


