#!/usr/bin/python
# -*- coding: utf-8 -*-

# insert_symbols.py


import tushare as ts
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql://root:123456@localhost/tushare?charset=utf8')

#stockList=ts.get_stock_basics()
#try:
    #stockList.to_sql('tick_data',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
    #pd.io.sql.to_sql(stockList,'tick_data', engine, schema='tushare', if_exists='append')
    #df1 = pd.read_sql('tick_data',engine)#从数据库中读取表存为DataFrame
#except:
 #   stockList.to_sql('tick_data',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么


df = ts.get_today_all()
try:
    df.to_sql('hqlist',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
except:
    df.to_sql('hqlist',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么

