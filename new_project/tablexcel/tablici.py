import pandas as pd

sales = pd.read_excel('customers.xlsx', sheet_name='customers')
states = pd.read_excel('orders.xlsx', sheet_name='orders')
newtrem = sales.merge(states, left_on='id', right_on='customer_id', suffixes=('_left', '_right'))
newtrem.to_excel('newtab.xlsx', sheet_name='Sheet1')



# print(sales.head())
# print('-' * 100)
# print(states.head())
# result = sales.pivot_table(index='city', values='id', aggfunc='sum')
# result_2 = states.pivot_table(index='customer_id', values='sales', aggfunc='sum')
# #sales = pd.merge(sales, states, how='left_on', on='name')
# states['MoreThan500'] = ['Yes' if x > 500 else 'No' for x in states['sales']]
# # print('-' * 100)
# # print(states['sales'])
# # print('-' * 100)
# print(result)
# print('-' * 100)
# print(result_2)
# newtrem = sales.merge(states, left_on='id', right_on='customer_id', suffixes=('_left', '_right'))
# newtrem.to_excel('newtab.xlsx', sheet_name='Sheet1')
# print('-' * 100)
# print(newtrem)
