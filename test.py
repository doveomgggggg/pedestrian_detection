from pyecharts.charts import Line, Page, Grid,Bar
from pyecharts import options as opts
import pymysql
import pandas as pd
import numpy as np
db =pymysql.connect(host="localhost",user="root",
                   password="123456",database="pedestrian_detection",
                   charset="utf8")
cur = db.cursor()
v1=[]
v2=[]
cur.execute("SELECT username from login")
data=cur.fetchall()
for d in data:
    v1.append(d[0])
print(v1)
