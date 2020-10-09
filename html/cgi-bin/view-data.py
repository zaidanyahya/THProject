#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import sqlite3
from contextlib import closing

dbname = '../../database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    select_sql = 'select * from data'
    
    print("Content-Type: text/html")
    print()
    head = '''
	<!DOCTYPE html>
	<html>
		<head><meta charset="utf-8" />
		<title>温度</title>
		</head>
	<body>	
	
	'''
    print(head)
    for row in c.execute(select_sql):
        print("<p>"+row+"</p>")
        
    foot = '''
    <a href="../">戻る</a>　
    </body>
	</html>
	'''
    print(foot)
