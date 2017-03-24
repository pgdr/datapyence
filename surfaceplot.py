from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import pylab
from ert.ecl import EclGrid

def find_surface_point(memberfn, idx, x, y, init_z=0, epsilon=1e-5):
    """Finds surface of function memberfn for cell idx and given x,y
    coordinate.  Assumes (x,y,init_z) is inside cell.
    """
    if not memberfn(idx, x, y, init_z):
        return None
    z_below = init_z
    z_above = init_z
    while memberfn(idx, x, y, z_above):
        z_above += abs(z_above * 2)
    z_next = z_above
    while abs(z_above - z_below) > epsilon:
        z_next = abs(z_above - z_below)/2.0 + z_below
        if memberfn(idx, x, y, z_next):
            z_below = z_next
        else:
            z_above = z_next
    return z_next

def cell_plane_iter(grid, idx, samples):
    """Iterates through [samples] of cell's x,y with z=z_mean fixed"""
    corners = []
    for i in range(8):
        corners.append(grid.getCellCorner(i, idx))
    xmin = min([c[0] for c in corners])
    xmax = max([c[0] for c in corners])
    ymin = min([c[1] for c in corners])
    ymax = max([c[1] for c in corners])
    zmean = sum([c[2] for c in corners]) / 8.0
    x_range = xmax - xmin
    y_range = ymax - ymin

    xs = []
    ys = []
    zs = []
    for i in range(samples):
        x = xmin + i * x_range/samples
        for j in range(samples):
            y = ymin + j * y_range/samples
            yield x,y,zmean

def find_surface(grid, idx, samples):
    """Finds top surface of cell idx of grid, with samples^2 points"""
    in_cell = lambda idx,x,y,z: grid.cell_contains(x,y,z,global_index=idx)
    xs = []
    ys = []
    zs = []
    for x,y,z in cell_plane_iter(grid, idx, samples):
        z = find_surface_point(in_cell, idx, x, y, init_z=z)
        if z is None:
            continue
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return xs,ys,zs


def main(fname):
    grid = EclGrid.loadFromGrdecl(fname)
    fig = pylab.figure()
    ax = Axes3D(fig)

    xs, ys, zs = find_surface(grid, 0, 20) # global idx, n, scale
    ax.plot_trisurf(xs,ys,zs)
    pyplot.show()


if __name__ == '__main__':
    main('data/markus.grdecl')
