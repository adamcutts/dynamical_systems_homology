import delay_embedding as dly
import mutual_information as mtl
import numpy as np
import matplotlib.pyplot as plt
import double_gyre as flow

fig, axs = plt.subplots(7, 7)

# Sample some flowline using double gyre
n, t_max = 1500, 200
x0 = np.random.uniform(0, 2)
y0 = np.random.uniform(0, 1)
x, y, t = flow.simulate_double_gyre(x0, y0, t_max, n)

# Choose 1D-function of the flow
time_series = x

n = len(time_series)
T = int(np.floor((n-1)/150))
T = 1
print('Based on position (', '{:.2f}'.format(x0), ',', '{:.2f}'.format(y0), ') at time t=0')

for i in range(49): #  Tests various delay lengths to find a low mutual information
    my_embedding = dly.takens_embedding(time_series, 2, T*i)
    pos1 = int(i % 7)
    pos2 = int(np.floor(i / 7) % 7)
    axs[pos2, pos1].scatter(my_embedding[0], my_embedding[1], s=0.2, alpha=(1/(t[n-T*i-1])) * t[0:n-T*i]) #  The alpha indicates how far along the timeseries we are
    my_mutual_info = mtl.mutual_info(my_embedding, 8)
    # info_str = 'Mutual Info: ' + '{:.2f}'.format(my_mutual_info)
    # axs[pos2, pos1].set_title(info_str, fontsize=12)

    # Colour background by mutual information for visual help
    p = min(my_mutual_info, 1)
    axs[pos2, pos1].set_facecolor((p, 1 - p, 0, 0.3))

plt.show()
