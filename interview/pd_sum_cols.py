#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论钉钉群21745728 钉钉群21745728 商务合作钉钉或微信: pythontesting
# CreateDate: 2019-12-29
# https://www.dataindependent.com/pandas/pandas-sum/
# https://stackoverflow.com/questions/25748683/pandas-sum-dataframe-rows-for-given-columns
import pandas as pd

df = pd.DataFrame({'a':[1,2], 'b':[3,4]})
print(df)
print('-'*60)

# 使用apply的笨办法
df = pd.DataFrame({'a':[1,2], 'b':[3,4]})
df['c'] = df.apply(lambda row: row.a + row.b, axis=1)
print(df)
print('-'*60)

# 使用sum
df = pd.DataFrame({'a':[1,2], 'b':[3,4]})
df['c'] = df.sum(axis=1)
print(df)
print('-'*60)

# 使用sum分层求和
data = (['Apple','Red',3,1.29],
        ['Apple','Green',9,0.99],
        ['Pear','Red',25,2.59],
        ['Pear','Green',26,2.79],
        ['Lime','Green',99,0.39])
df = pd.DataFrame(data, columns=['Fruit','Color','Count','Price'])
df = df.set_index(['Fruit', 'Color'])
print(df)
print(df.sum())
print(df.sum(level=0))
print(df.sum(level=1))
print('-'*60)

# 求部分列的和
df = pd.DataFrame({'a': [1,2,3], 'b': [2,3,4], 'c':['dd','ee','ff'], 'd':[5,9,1]})
print(df)
col_list= list(df.columns)
col_list.remove('d')
print(df[col_list].sum(axis=1))