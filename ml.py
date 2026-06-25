#preprocessing

import pandas as pd
import numpy as np 
data = {
    "colors":['red','green','blue','orange','green','blue',np.nan]
}
df = pd.DataFrame(data)
print(df) 
#handling nullvalue 
#df['colors'] = df['colors']
df.dropna(inplace = True)
print(df)
# label encoding
from sklearn.preprocessing import LabelEncoder
 
# method 1
le = LabelEncoder()
df['colors_encoder1'] = le.fit_transform(df['colors'])
 
# method 2
df['colors_encoder2'] = LabelEncoder().fit_transform(df['colors'])
# print(df)
 
# method 3
import sklearn
df['colors_encoder3'] = sklearn.preprocessing.LabelEncoder().fit_transform(df['colors'])
print(df)
 
# one hot encoding
from sklearn.preprocessing import OneHotEncoder
print(df)
 
# drop cols of label encoding
if 'colors_encoder' in df.keys():
  df.drop(df[['colors_encoder','colors_encoder1','colors_encoder2','colors_encoder3']],axis=1,inplace=True)
 
print(df)
 
# one hot encoding
 
from sklearn.preprocessing import OneHotEncoder
print(df)
 
# drop cols of label encoding
if 'colors_encoder' in df.keys():
  df.drop(df[['colors_encoder','colors_encoder1','colors_encoder2','colors_encoder3']],axis=1,inplace=True)
 
print(df)
 
# one hot encoding (by the help of pandas)
df_encoder = pd.get_dummies(df,columns=['colors'])
print(df_encoder)