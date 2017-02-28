import pandas as pd, matplotlib.pyplot as plt, sklearn, numpy as np

df = pd.read_csv('data/pm.csv', delimiter=';')
vals = df['value']
arr = np.array(vals)

arr.mean()
arr.min()
arr.max()
np.percentile(arr, 10)
np.percentile(arr, 90)

pm10 = df[(df.sensor == 'PM10')]
pm25 = df[(df.sensor == 'PM25')]

plt.figure()
plt.plot(np.array(pm10['value']))
plt.figure()
plt.plot(np.array(pm25['value']))

#mtx = np.array([(int(x[1][3].split()[1].split(':')[0]), float(x[1][1]))
#                   for x in pm10.iterrows()])

times_pm10 = np.array([int(x[1][3].split()[1].split(':')[0]) for x in pm10.iterrows()])
vals_pm10  = np.array([float(x[1][1]) for x in pm10.iterrows()])


plt.figure()
plt.scatter(times_pm10, vals_pm10)



times_pm25 = np.array([int(x[1][3].split()[1].split(':')[0]) for x in pm25.iterrows()])
vals_pm25  = np.array([float(x[1][1]) for x in pm25.iterrows()])


plt.figure()
plt.scatter(times_pm25, vals_pm25)
plt.show()
