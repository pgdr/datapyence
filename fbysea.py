#!/usr/bin/env python

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import sqlite3

quer = 'SELECT * FROM samples;'
conn = sqlite3.connect('data/friskby.sql')
df = pd.read_sql(quer,conn)
conn.close()
pm25 = df[(df.sensor == 'PM25')]

sns.tsplot(pm25.value)
plt.show()
