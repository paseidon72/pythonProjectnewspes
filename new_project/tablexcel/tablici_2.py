import pandas as pd
import numpy as np
df = pd.read_excel("excel-comp-data.xlsx")
df["total"] = df["Jan"] + df["Feb"] + df["Mar"] #додати загальний стовпець "total", показати загальний обсяг
# продажів за січень, лютий і березень.
result = df["Jan"].sum()
result2 = df["Jan"].mean()
result3 = df["Jan"].min()
result4 = df["Jan"].max() #щоб отримати підсумки за місяць.
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum() #створіть суму для стовпців місяця та підсумку.
df_sum = pd.DataFrame(data=sum_row).T #якщо ви хочете додати підсумки у вигляді рядка.
# Ця T функція дозволяє нам переключати дані з рядків на стовпці.
df_sum=df_sum.reindex(columns=df.columns) #додати відсутні стовпці
# а потім заповнити значення, яких немає.
df_final = df.append(df_sum, ignore_index=True) #Тепер відформатований DataFrame,
df_final.tail() # ми можемо додати його до існуючого за допомогою append .
df.head()
print(df)
print('*' * 50)
print("Jan:", "sum", result, "mean", result2, "min", result3, "max", result4)
print('*' * 50)
print(sum_row)
print('*' * 50)
print(df_sum)
print('*' * 50)
print(df_final)

