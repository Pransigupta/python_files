import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"

data = {
    "experience": [300, 600, 900, 1500],
    "salary": [1000, 1500, 2000, 3000]
}

# DataFrame
df = pd.DataFrame(data)
print(df)

# Standard Scaler
scaler = StandardScaler()
df['experience'] = scaler.fit_transform(df[['experience']])

print(df)

# Split features and target
X = df[['experience']]   # keep as 2D
y = df['salary']

print(X)
print(y)

# Plot
plt.plot(data["experience"], data["salary"], marker='o', linewidth=2)
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Train Test Split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("x train:\n", x_train)
print("x test:\n", x_test)
print("y train:\n", y_train)
print("y test:\n", y_test)