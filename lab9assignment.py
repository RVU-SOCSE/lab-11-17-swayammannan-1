
import pandas as pd 
df=pd.read_csv("exp.csv")
print(df) 
print(df.describe()) 
print(df.quantile([0.25,0.5,0.75]))

skewness = df['YearsExperience'].skew() 
kurtosis = df['YearsExperience'].kurt() 
print(df.skew())
print(df.kurt())

quantiles = df['YearsExperience'].quantile([0.25, 0.5, 0.75]) 
print(quantiles)

data = [10, 20, 20, 30, 100]
print(pd.Series(data).skew())

descreption = df.describe() 
print(descreption)
print(df.describe())

