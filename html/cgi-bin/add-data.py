#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi

import time
import smbus
import sqlite3
from contextlib import closing

def tempChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)                                             # P1
    return  (-45 + 175 * int(str(mlsb), 10) / (pow(2, 16) - 1))            # P2
    
def humidChanger(msb, lsb):
    mlsb = ((msb << 8) | lsb)
    return (100 * int(str(mlsb), 10) / (pow(2, 16) - 1))
    
i2c = smbus.SMBus(1)
i2c_addr = 0x45                                                           # P3

i2c.write_byte_data(i2c_addr, 0x21, 0x30)                                 # P4
time.sleep(0.5)

i2c.write_byte_data(i2c_addr, 0xE0, 0x00)                             # P5
data = i2c.read_i2c_block_data(i2c_addr, 0x00, 6)                     # P6


temp = tempChanger(data[0], data[1])
humid = humidChanger(data[3], data[4])

dbname = 'database.db'


print("Content-Type: text/html")
print()
htmlText = '''
<!DOCTYPE html>
<html>
    <head><meta charset="utf-8" />
    <title>温度</title>
    </head>
<body>
    <h1>温度　%s</h1>
    <h1>湿度　%s</h1>
    <p>のデータがデータベースに追加した！</p>
    <a href="../">戻る</a>　
</body>
</html>
'''%(str('{:.4g}'.format(temp))+ "&#176;C", str('{:.4g}'.format(humid))+ "%" )
print(htmlText)

