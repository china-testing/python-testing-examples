#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论钉钉群21745728 钉钉群21745728 商务合作钉钉或微信: pythontesting
# CreateDate: 2019-12-29
# https://www.delftstack.com/howto/python-pandas/how-to-get-a-value-from-a-cell-of-a-dataframe/
import pandas as pd

df = pd.DataFrame({
    'name': ['orange','banana','lemon','mango','apple'],
    'price': [2,3,7,21,11],
    'stock': ['Yes','No','Yes','No','Yes']
})
print(df)

# 先获取整行，再找到指定的列 使用iloc
print(df.iloc[2]['price']) 
print(df.iloc[2]['stock'])

# 先获取整行，再找到指定的列 使用loc
print(df.loc[2]['price'])
print(df.loc[2]['stock'])

# 先获取整列，再找到指定的行
print(df.price[2]) 
print(df['stock'][2])

# 先获取整行，再找到指定的列 使用loc
print(df.loc[2]['price'])
print(df.loc[2]['stock'])

# 使用iat或at直接获取坐标值
print(df.iat[2,1])
print(df.at[2,'stock'])
print(df.at[df.index[-3],'stock'])

