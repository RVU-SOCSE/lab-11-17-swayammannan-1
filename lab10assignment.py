import pandas as pd 
df = pd.read_csv("laptop.csv") 
print(df) 
pd.get_dummies(df)  

from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder() 
enc_data = enc.fit_transform(df[['Category']])  
print(enc_data) 
print(enc.categories_)  
enc_data.toarray() 
enc_df = pd.DataFrame(enc_data.toarray())   
print(enc_df) 
enc_df = pd.DataFrame(enc_data.toarray(), columns = ['2 in 1 Convertible', 
'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation']) 
print(enc_df) 
df1 = df.join(enc_df) 
print(df1) 

from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder() 
df['RAM'] = le.fit_transform(df['RAM']) 
print(df)

print(le.classes_ )  