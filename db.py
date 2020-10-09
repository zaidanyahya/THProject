# -*- coding: utf-8 -*-

import sqlite3
from contextlib import closing

dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()

    # executeメソッドでSQL文を実行する
    create_table = '''create table data (time varchar(64),
                      temp real, humid real)'''
    c.execute(create_table)
    conn.commit()
    print("データベースが作成した")

