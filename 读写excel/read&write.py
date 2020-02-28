import pandas as pd
import numpy as np
import time

time_start = time.time()

df = pd.read_excel('嘉豪测试.xlsx')
time_read = time.time()
print('读数据时间', time_read - time_start)

s1 = ['ORDER_CODE', '删除1', '删除2', '删除3', '删除4', '删除5', '删除6', '删除7']
s2 = ['删除1', '删除2', '删除3', '删除4', '删除5', '删除6', '删除7']
df_del = df[s1]

# print(df_del.head())
df.drop(columns=s2, axis=1, inplace=True)
# print(df.head())
df_del = df_del.replace(0, np.nan)
df_new = pd.merge(df, df_del, how='outer', on='ORDER_CODE')
time_process = time.time()
print('处理数据时间', time_process - time_read)

df_new.to_excel('删完0的数据.xlsx', encoding='gbk')
time_write = time.time()
print('输出数据时间', time_write - time_process)
time_end = time.time()
print('总体时间', time_end - time_start)
