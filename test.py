import pandas as pd
import os
import sys

current_path = './test.xlsx'
df =  pd.read_excel(current_path, engine='openpyxl')
# print(df.columns.to_list())

df = df.transpose()
print(df.iloc[0])
df.columns = df.iloc[0]
df = df.drop(df.index[0])

output_file = './new.xlsx'
df.to_excel(output_file, index=False)
