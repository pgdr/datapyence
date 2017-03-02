from ert.ecl import EclFile, EclGrid
from ert.ecl import Ecl3DKW

from os.path import abspath, expanduser, join

norne = abspath(expanduser('~/opm/opm-data/norne/opm-simulation-reference'))

print('Using Norne location %s' % norne)

rst = EclFile(join(norne, 'NORNE_ATW2013.UNRST'))
grd = EclGrid(join(norne, 'NORNE_ATW2013.EGRID'))

x = 10 # x in [0, grd.getNX())
y = 10 # y in [0, grd.getNY())

print(grd)
print('Plotting SGAS, SOIL, SWAT for x,y pillar (%d, %d)' % (x,y))

swat = rst.iget_named_kw('SWAT', 0)
sgas = rst.iget_named_kw('SGAS', 0)

swat3d = Ecl3DKW.castFromKW(swat, grd, default_value=0)
f_swat = lambda k: swat3d[x,y,k]

sgas3d = Ecl3DKW.castFromKW(sgas, grd, default_value=0)
f_sgas = lambda k: sgas3d[x,y,k]

f_soil = lambda k: max(0, 1 - (f_sgas(k) + f_swat(k)))

nz = grd.getNZ()

sgas = [f_sgas(k) for k in range(nz)]
soil = [f_soil(k) for k in range(nz)]
swat = [f_swat(k) for k in range(nz)]

import matplotlib.pyplot as plt
plt.plot(sgas, color='r', label='SGAS')
plt.plot(soil, color='g', label='SOIL')
plt.plot(swat, color='b', label='SWAT')
plt.legend(loc='upper right')
plt.show()
