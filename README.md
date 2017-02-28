# datapyence

_datapyence_, sometimes called _pytascience_ is an artform where one takes data
combined with machine learning algorithms, a dash of python, and get niceties.

We showcase `pandas`, `matplotlib`, `numpy`, and `scikit-learn`.

We could also showcase `sqlite` to actually get the cvs.  And that's exactly why
we do it.  Look how ridiculously simple it is!  It's almost an insult.

```python
import sqlite3
import pandas as pd

quer = 'SELECT * FROM samples;'
conn = sqlite3.connect('data/friskby.sql')
df = pd.read_sql(quer,conn)
conn.close()
print(repr(df))
```
