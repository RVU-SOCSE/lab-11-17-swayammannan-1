import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

df=pd.read_csv("12lap.csv")
print("Dataset:")
print(df)

print("\nBoxplot for Screen Size")

plt.boxplot(df["Screen"], notch=True, vert=False, showmeans=True)
plt.xlabel("Screen")
plt.title("Boxplot - Screen Size")
plt.show()

print("\nBoxplot for Weight")

plt.boxplot(df["Weight"])
plt.ylabel("Weight")
plt.title("Boxplot - Weight")
plt.show()

print("\nSeaborn Boxplot for Weight")

sns.boxplot(x=df["Weight"])
plt.title("Seaborn Boxplot - Weight")
plt.show()

print("\nSeaborn Boxplot - Weight vs RAM")

sns.boxplot(x=df["Weight"], y=df["RAM"])
plt.title("Weight vs RAM")
plt.show()

print("\nIQR Method Calculation")

Q1 = df["Weight"].quantile(0.25)
Q3 = df["Weight"].quantile(0.75)

print("Q1:", Q1)
print("Q3:", Q3)

IQR = Q3 - Q1
print("IQR:", IQR)

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Lower Bound:", lower)
print("Upper Bound:", upper)

outliers = df[(df["Weight"] < lower) | (df["Weight"] > upper)]

print("\nOutliers in Weight:")
print(outliers)