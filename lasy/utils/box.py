import numpy as np


class Box:
    """
    Contain metadata on index and physical space for an array,
    as well as handy methods.
    """

    def __init__(self, dim, lo, hi, npoints):
        """
        Initialize a Box object

        Parameters
        ----------
        dim : string
            Dimensionality of the box, 'xyz' or 'rz'

        lo, hi : list of scalars
            Lower and higher end of the physical domain of the box.
            One element per direction (2 for dim='rz', 3 for dim='xyz')

        npoints : tuple of int
            Number of points in each direction.
            One element per direction (2 for dim='rz', 3 for dim='xyz')
            For the moment, the lower end is assumed to be (0,0) in rz and (0,0,0) in xyz
        """
        self.dim = dim
        self.ndims = 2 if dim == 'rz' else 3
        self.lo = list(lo)
        self.hi = list(hi)
        self.npoints = npoints
        self.axes = []
        self.dx = []
        for i in range(self.ndims):
            self.axes.append(np.linspace(lo[i], hi[i], npoints[i]))
            self.dx.append(self.axes[i][1] - self.axes[i][0])