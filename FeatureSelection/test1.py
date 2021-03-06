import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

from FeatureSelection import performance

data = pd.read_csv('predict_house.csv')
x = data.iloc[:, 0:79]
y = data.iloc[:, -1]
sum = 0.0
for i in range(100):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    rd = GradientBoostingRegressor()
    rd.fit(x_train, y_train)
    result = rd.predict(x_test)
    sum = sum + performance.performance(y_test, result)
print(sum/100)