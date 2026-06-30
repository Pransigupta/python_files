# poly reg -> over fitting
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
 
df = pd.DataFrame({
    "label":[1,2,3,4,5]
})
x = df
y = [10, 20, 50, 90, 150]
 
# poly convert
poly  = PolynomialFeatures(degree=3)
x_poly = poly.fit_transform(x)
 
# model
model = LinearRegression()
model.fit(x_poly,y)
 
# predict
input_data = int(input('enter the label: '))
new_data = pd.DataFrame({
    "label":[input_data]
})
 
# input data to poy
u_new_data = poly.fit_transform(new_data)
 
# prediction
predicted_data = model.predict(u_new_data)
print(predicted_data[0])
 