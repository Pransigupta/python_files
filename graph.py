import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"

df = pd.read_json(url)
df1 = pd.read_json(url)
pd.concat([df,df1])
df1.loc[2,"name"] = "Pransi"
#df.isnull()
#df.loc[4, 'marks'] = np.nan
#df.dropna()
#inplace = True #Modify the existing object itself.
#df.fillna({"roll no":200,"marks":100})


#df = df.fillna({"roll no": 200,"marks": 100}, inplace=True)
 
#print(df)
#print(df.fillna({"marks":df["marks"].mean()}))
#mean_marks = df["marks"].mean()
##df["marks"].fillna(mean_marks, inplace=True)
print(pd.concat([df, df1], axis=1))
print(pd.concat([df, df1]))

#print("Mean =", df["marks"].mean())

# aab ham mean nikalenge or avg value se nan ko fill kardo 
#df["marks"] = df["marks"].astype(object)
#df.loc[df["name"] == "anjali", "marks"] = 'Null'
#print(df)


