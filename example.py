import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analysis(arr):
    print('%.1f +/- %.1f (%.1f %.1f %.1f %.1f %.1f)'
          % (arr.mean(), arr.std(),
          arr.min(),
          np.percentile(arr, 10), np.percentile(arr, 50), np.percentile(arr, 90),
          arr.max()))

df = pd.read_csv('data/pm.csv', delimiter=';')
pm10 = df[(df.sensor == 'PM10')]
pm25 = df[(df.sensor == 'PM25')]

arr_10 = np.array(pm10['value'])
arr_25 = np.array(pm25['value'])
analysis(arr_10)
analysis(arr_25)

plt.figure()
plt.plot(np.array(pm10['value']), color='b')
plt.plot(np.array(pm25['value']), color='r')

times_pm10 = np.array([int(x[1][3].split()[1].split(':')[0]) for x in pm10.iterrows()])
vals_pm10  = np.array([float(x[1][1]) for x in pm10.iterrows()])

times_pm25 = np.array([int(x[1][3].split()[1].split(':')[0]) for x in pm25.iterrows()])
vals_pm25  = np.array([float(x[1][1]) for x in pm25.iterrows()])

plt.figure()
plt.scatter(times_pm10, vals_pm10, color='b')
plt.scatter(times_pm25, vals_pm25, color='r')


from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

pred = {}
for i in range(len(times_pm10)):
    t,v = times_pm10[i], vals_pm10[i]
    if t not in pred:
        pred[t] = []
    pred[t].append(v)

keys = np.array(pred.keys())
vals = []
for k in keys:
    vals.append(np.array(pred[k]).mean())
print keys, vals


keys = keys.reshape((24,1))

model = make_pipeline(PolynomialFeatures(5), Ridge())

model.fit(keys, vals)
prediction_keys = [i/3.0 for i in range(24*3)]
prediction_vals = [model.predict(i/3.0) for i in range(24*3)]
plt.scatter(prediction_keys, prediction_vals, color='g')
plt.show()
