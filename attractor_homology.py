import delay_embedding as dly
import mutual_information as mtl
import numpy as np
import matplotlib
import double_gyre as flow
from ripser import Rips
matplotlib.pyplot.rcdefaults()


n, t_max = 900, 100
x0 = float(input('Initial x value: '))
y0 = float(input('Initial y value: '))
x, y, t = flow.simulate_double_gyre(x0, y0, t_max, n)

# Choose 1D-function of the flow
time_series = x

rips = Rips(maxdim=1)
data = dly.takens_embedding(time_series, 4, 20)
data = data.T  # Ripser uses each row as a point in the point cloud
diagrams = rips.fit_transform(data)
rips.plot(diagrams, show=True)
