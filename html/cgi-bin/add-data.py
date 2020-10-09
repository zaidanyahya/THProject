#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi

import time
import smbus
import sqlite3
from contextlib import closing

"""
def tempChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)                                           
    return  (-45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1))         
    
def humidChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)
    return (100 * int(str(mlsb), 10) / (pow(2, 16) - 1))
    
i2c = smbus.SMBus(1)
i2c_addr = 0x45                                                         

i2c.write_byte_data(i2c_addr, 0x21, 0x30)                               
time.sleep(0.5)

i2c.write_byte_data(i2c_addr, 0xE0, 0x00)                               
data = i2c.read_i2c_block_data(i2c_addr, 0x00, 6)                       


temp = tempChanger(data[0], data[1])
humid = humidChanger(data[3], data[4])
"""

import random
temp = random.randrange(20, 38)
humid = random.randrange(50, 80)

dbname = '../database.db'


print("Content-Type: text/html")

css = '''
<style>
body, html{
    padding:0;
    margin:0;
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
h2{
    text-align:center;
}
</style>
'''
print()
htmlText = '''
<!DOCTYPE html>
<html>
    <head><meta charset="utf-8" />
    <title>温度と湿度</title>
    %s
    </head>
<body>
    <a href="../"> << 戻る</a>　
    <h2>温度:%s  湿度:%s  のデータがデータベースに追加した！</h2>
</body>
</html>
'''%(css,str('{:.4g}'.format(temp))+ "&#176;C", str('{:.4g}'.format(humid))+ "%" )


with closing(sqlite3.connect(dbname)) as conn:
    c = conn.cursor()
    insert_sql = 'insert into data values(?,?,?)'
    c.execute(insert_sql,(time.strftime("%a %Y/%m/%d  %H:%M:%S", time.localtime()), temp, humid))
    conn.commit()
    conn.close()
    print(htmlText)

