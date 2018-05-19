#!/usr/bin/python
# -*- coding: utf-8 -*-

# insert_symbols.py


import tushare as ts
import MySQLdb as mdb


def insert_snp500_symbols(symbols):
    db_host = 'localhost'
    db_user = 'root'
    db_pass = '123456'
    db_name = 'stockdata'
    con = mdb.connect(
        host=db_host, user=db_user, passwd=db_pass, db=db_name
    )
    column_str = """ticker, instrument, name, sector, 
                 currency, created_date, last_updated_date
                 """
    insert_str = ("%s, " * 7)[:-2]
    final_str = "INSERT INTO symbol (%s) VALUES (%s)" % \
        (column_str, insert_str)
    with con:
        cur = con.cursor()
        cur.executemany(final_str, symbols)

stockList=ts.get_stock_basics()




