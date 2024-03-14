import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,MinMaxScaler

data=pd.read_csv("flood/kerala.csv")
data.drop("SUBDIVISION",axis=1,inplace=True)
x_input=data.drop("FLOODS",axis=1)
# x_input = x_input.drop("YEAR",axis = 1)
y_output=data["FLOODS"]
# year = data["YEAR"]

ldr=LabelEncoder()
y_output=ldr.fit_transform(y_output)
x_input.to_csv("created_data.csv",index=False,header=False)  
fetched_data = np.loadtxt("created_data.csv",delimiter=",")   # this is the input_data and y_output is the output data


from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(fetched_data,y_output,test_size=0.08)


from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()

model.fit(x_train,y_train)

prediction = model.predict(x_test)

from sklearn.metrics import accuracy_score

score = accuracy_score(prediction,y_test)

print("accuracy score is", score)


def predict1(year,monthly):
    year = year
    monthly_data = monthly
    annual_fall = round(sum(monthly_data),3)
    monthly_data.append(annual_fall)
    print(monthly_data)
    input_data = []
    input_data.append(year)
    input_data.extend(monthly_data)
    input_array = np.array(input_data).reshape(1,len(input_data))
    print(input_array)
    prediction = model.predict(input_array)
    print(prediction)
    return prediction