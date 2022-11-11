import pandas as pd

months = ['jan', 'feb', 'mar', 'apr']
sales = {
    'revenue': [100, 200, 300, 400],
    'items_sold': [23, 43, 55, 65],
    'new_clients': [10, 20, 30, 40]
}
sales_df = pd.DataFrame(data=sales, index=months)

print(sales_df)

