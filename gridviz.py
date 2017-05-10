#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import pylab
import numpy as np
try:
    from ert.ecl import EclGrid
except ImportError:
    from ecl.ecl import EclGrid
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import colors

from matplotlib.collections import PolyCollection



decompositions = [
        [
            [0,1,2],
            [3,2,1],
            [6,2,7],
            [3,7,2],
            [0,2,4],
            [6,4,2],
            [3,1,7],
            [5,7,1],
            [0,4,1],
            [5,1,4],
            [5,4,7],
            [6,7,4]
        ],
        [
            [1,3,0],
            [2,0,3],
            [2,3,6],
            [7,6,3],
            [2,6,0],
            [4,0,6],
            [7,3,5],
            [1,5,3],
            [1,0,5],
            [4,5,0],
            [7,5,6],
            [4,6,5]
        ]]

def cell_dec(ijk):
    global decompositions
    return decompositions[sum(ijk)%2]

def edges(ijk):
    return [(0,1), (0,2), (1,3), (2,3), (4,5), (4,6), (5,7), (6,7), (0,4),
            (1,5), (2,6), (3,7), cell_dec(ijk)[0][1::], cell_dec(ijk)[10][1::]]

def plot_cell(grid, ax, ijk, color='b'):
    corners = [grid.getCellCorner(i, ijk=ijk) for i in range(8)]
    x,y,z = zip(*corners)
    for e1, e2 in edges(ijk):
        ax.plot_wireframe([x[e1], x[e2]],
                          [y[e1], y[e2]],
                          [z[e1], z[e2]], color=color)

def inc_k(ijk, inc=1):
    return ijk[0], ijk[1], ijk[2]+inc

def main(grid, coord):
    px,py,pz = coord
    print('point: %g, %g, %g' % (px,py,pz))

    ijk = grid.find_cell(*coord)
    if ijk is None:
        print('ERROR!  ijk %s not found in grid' % list(coord))
        return

    print("\nCELL (%d, %d, %d)\n" % (ijk[0], ijk[1], ijk[2]))


    fig = pylab.figure('Point %s' % str(coord))
    ax = Axes3D(fig)

    #plot_cell(grid, ax, inc_k(ijk,-1), color='b')
    plot_cell(grid, ax, ijk, color='r')
    #plot_cell(grid, ax, inc_k(ijk), color='g')
    ax.scatter([px], [py], [pz], color='c')

    pyplot.show()

if __name__ == '__main__':
    if len(argv) != 2:
        exit('Usage: gridviz fname.EGRID')
    grid = EclGrid(argv[1])
    pts = [(466316.01, 7336634.27, 2441.64), (466337.07, 7336640.05, 2455.64),
           (466349.26, 7336643.36, 2463.67), (466381.08, 7336651.83, 2484.58),
           (466401.91, 7336657.26, 2498.25), (466417.43, 7336661.30, 2508.44),
           (466444.07, 7336668.35, 2525.87)]
    for pt in pts:
        print('\n\n===== PLOTTING FOR POINT %s ======\n' % list(pt))
        main(grid, pt)
