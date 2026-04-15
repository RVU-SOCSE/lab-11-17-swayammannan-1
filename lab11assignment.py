import pandas as pd
data=pd.read_csv("11p.csv")
df = pd.DataFrame(data)
from sklearn.preprocessing import StandardScaler        

scaler = StandardScaler()  
scaled_data = scaler.fit_transform(df)   

print(scaled_data)

print (" ")
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

print(scaled_data)
print (" ")
from sklearn.preprocessing import Normalizer

scaler = Normalizer()          
normalized_data = scaler.fit_transform(df)

print(normalized_data)

data=[1,2,3]
df = pd.DataFrame(data)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)  

print(scaled_data)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()  
scaled_data = scaler.fit_transform(df)

print(scaled_data)

from sklearn.preprocessing import Normalizer

scaler = Normalizer()  
normalized_data = scaler.fit_transform(df)

print(normalized_data)