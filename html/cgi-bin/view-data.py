#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import sqlite3
from contextlib import closing

dbname = '../database.db'

with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    select_sql = 'select * from data'
    
    print("Content-Type: text/html")
    print()
    head = '''
	<!DOCTYPE html>
	<html>
		<head><meta charset="utf-8" />
		<title>温度と温度</title>
		
		<style>
		    body, html{
			padding:0;
			margin:0;
		    }
		    table{
			margin:auto auto;
		    }
		    table, th, td {
		      border: 1px solid black;
		      border-collapse: collapse;
		    }
		    th, td {
		      padding: 15px;
		      text-align:center;
		    }
		    a {
			text-decoration:none;
			font-size:30px;
			margin:auto;
			padding:10px;
			text-align:center;
			background-color: orange;
			color:white;
			transition-duration:0.3s;
		    }
		    a:hover{
			    background-color: grey;
		    }
		</style>
		</head>
	<body>	
	<a href="../"> << 戻る</a>　
	<table width="60%">
	<tr>
	    <th>日時</th>
	    <th>温度</th>
	    <th>湿度</th>
	</tr>
	'''
    print(head)
    for row in c.execute(select_sql):
	print("<tr>")
        print("<td>"+row[0]+"</td>")
	print("<td>"+str(row[1])+"</td>")
	print("<td>"+str(row[2])+"</td>")
	print("</tr>")	
    foot = '''
    </table>
    <br>
    
    </body>
	</html>
	'''
    print(foot)
