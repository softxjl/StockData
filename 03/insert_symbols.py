#!/usr/bin/python
# -*- coding: utf-8 -*-

# insert_symbols.py

from __future__ import print_function

import datetime
from math import ceil

import bs4
import MySQLdb as mdb
import requests

def obtain_parse_wiki_snp500():
    now = datetime.datetime.utcnow()
    response = requests.get(
        "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    )
    soup = bs4.BeautifulSoup(response.text)
    symbolslist = soup.select('table')[0].select('tr')[1:]
    symbols = []
    for i, symbol in enumerate(symbolslist):
        tds = symbol.select('td')
        symbols.append(
            (
                tds[0].select('a')[0].text,  # Ticker
                'stock', 
                tds[1].select('a')[0].text,  # Name
                tds[3].text,  # Sector
                'USD', now, now
            ) 
        )
    return symbols


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


if __name__ == "__main__":
    symbols = obtain_parse_wiki_snp500()
    insert_snp500_symbols(symbols)
    print("%s symbols were successfully added." % len(symbols))
