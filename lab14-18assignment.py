# lab 14 to 18
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
'Salary': [50000, 60000, 75000, 80000, 120000, 95000, 40000, 70000],
'Years_Experience': [1, 2, 3, 4, 5, 6, 1.5, 3.5],
'Experience_Level': ['Junior', 'Junior', 'Mid', 'Mid', 'Senior', 'Senior', 'Junior', 'Mid']
}
df = pd.DataFrame(data)

# 1) Salary Distribution
sns.histplot(df['Salary'], kde=True)
plt.title("Salary Distribution")
plt.show()

# 2) Pair Plot (Salary vs Years_Experience)
sns.pairplot(df[['Salary', 'Years_Experience']])
plt.show()

# 3) Correlation Heatmap
sns.heatmap(df[['Salary', 'Years_Experience']].corr(), annot=True, cmap='coolwarm')
plt.show()


# 4) Line Plot: Salary Trend by Years of Experience
sns.lineplot(x='Years_Experience', y='Salary', data=df, marker='o')      
 				 # 'o' - circle  's' (square), '^' (triangle), '*' (star) (don’t type)
plt.title("Salary Trend by Experience")
plt.show()

# 5) Scatter Plot: Salary vs Years of Experience
sns.scatterplot(x='Years_Experience', y='Salary', data=df, s=100)  
                                                           # s = size of each scatter point.
plt.title("Salary vs Experience")
plt.show()

# 6) Bar Plot: Experience Level vs Salary
sns.barplot(x='Experience_Level', y='Salary', data=df)
plt.title("Salary by Experience Level")
plt.show()
