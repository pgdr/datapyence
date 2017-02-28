import sqlite3
import pandas as pd

quer = 'SELECT * FROM samples;'
conn = sqlite3.connect('data/friskby.sql')
df = pd.read_sql(quer,conn)
conn.close()
print(repr(df))
