import numpy as np
import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "name": ['praveen', 'dheeraj', 'yash', 'kunal'],
    "avg_income": [1000, 200, 300, 400],
    "house_age": [10.2, 2.5, 3.0, 4.0],
    "num_rooms": [3, 4, 5, 1],
    "price": [10000, 7000, 15000, 11000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Remove name column
df.drop("name", axis=1, inplace=True)

# Features and Target
X = df[['avg_income', 'house_age', 'num_rooms']]
y = df['price']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model and Scaler
joblib.dump(model, "house_model.joblib")
joblib.dump(scaler, "scaler.joblib")

print("Model saved successfully!")

new_data = pd.DataFrame({
    "avg_income": [900],
    "house_age": [8],
    "num_rooms": [5]
})


new_data_scaled = scaler.transform(new_data)

# Predict Price
predicted_price = model.predict(new_data_scaled)

print("Predicted House Price:", predicted_price[0])
#not working we have to switch for pysql
# mysql connector
# !pip install mysql.connector
#import mysql.connector
#conn = mysql.connector.connect(host="13.220.156.88",user="mluser",database="ml_db",password="mlpass123")
#query = "select avg_income,house_age,num_rooms,price from houses"
#df = pd.read_sql(query,conn)
#print(df)
import pymysql
conn = pymysql.connect(host="13.220.156.88",user="mluser",database="ml_db",password="mlpass123")
print(conn)
query = "select avg_income,house_age,num_rooms,price from houses"
df = pd.read_sql(query,conn)
print(df)