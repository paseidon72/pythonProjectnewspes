import pandas as pd

orders = pd.read_csv('orders.csv', index_col='id')
customers = pd.read_csv('customers.csv', index_col='id')
pd.options.display.float_format = '{:,.1f}'.format
cust_filter = 'CG-12520'
ser = orders.query('customer_id == @cust_filter')
new_df = pd.merge(orders, customers, how='inner', left_on='customer_id', right_index=True)
orders_2016 = orders.query("order_date >= '2016-01-01' & order_date <= '2016-12-31'")
with_customers_2016 = pd.merge(customers, orders_2016, how='inner', left_index=True, right_on='customer_id')
grouped_2016 = with_customers_2016.groupby('city')['sales'].sum()
top5 = grouped_2016.sort_values(ascending=False).head(5)
pro = top5
# sales_filter = 1000
# ship_mode_filter = 'First'
res = orders.groupby(['ship_mode', 'order_date'])['sales']\
    .agg(['sum']).sort_values(by='sum', ascending=False).head(10)

# print(res)
# print(ser)
print(pro)
