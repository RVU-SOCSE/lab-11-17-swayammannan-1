import pandas as pd


emp = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105],
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Dept': ['HR', 'Eng', 'Eng', 'HR', 'Mkt']
})

sal = pd.DataFrame({
    'ID': [101, 102, 103, 104, 105],
    'Sal': [50000, 70000, 80000, 55000, 60000]
})

sales1 = pd.DataFrame({
    'Date': pd.date_range(start='2026-01-01', periods=5), 
    'Reg': ['N']*5, 
    'Sale': [250, 300, 200, 400, 350]
})

sales2 = pd.DataFrame({
    'Date': pd.date_range(start='2026-01-01', periods=5),
    'Reg': ['S']*5,
    'Sale': [300, 320, 280, 360, 310]
})

print("Employee Data:")
print(emp)

print("\nSalary Data:")
print(sal)

merge_data = pd.merge(emp, sal, on='ID')

print("\nMerged Data:")
print(merge_data)

avg = emp.merge(sal, on='ID').groupby('Dept')['Sal'].mean() .reset_index()
avg.columns=['dept','avgsal']

print("\nAverage Salary by Dept:")
print(avg)

emp1 = emp.set_index('ID')
sal1 = sal.set_index('ID')
join_data = emp1.join(sal1,how='inner')  

print("\nJoined Data:")
print(join_data)

final = pd.concat([sales1, sales2], axis=1)

print("\nConcatenated Sales Data:")
print(final)