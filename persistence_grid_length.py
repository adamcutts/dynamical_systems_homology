import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
import delay_embedding as dly
import double_gyre as flow


# Rescales data for RGB plotting
def sigmoid(z):
    result = (1+np.exp(z))**(-1)
    return result


# Sorts the H1 intervals from largest to smallest length
def barcode_sorter(barcode):
    result = sorted(barcode, key=lambda bar: bar[1] - bar[0], reverse=True)
    return result


# Works with a 2m x m grid of test points
m = int(input('Resolution: '))

n, t_max = 200, 520

x_points = np.linspace((2*m + 1)**(-1), 2 - (2*m + 1)**(-1), 2*m)
y_points = np.linspace(1 - (m + 1)**(-1), (m + 1)**(-1), m)  # Reversed since subplots goes down in rows

values_array = np.zeros((m, 2*m))

for i in range(m):
    for j in range(2*m):
        print(f'Iterate ({i},{j}) of ({m},{2*m})')
        x, y, t = flow.simulate_double_gyre(x_points[j], y_points[i], t_max, n)
        data = dly.takens_embedding(x, 4, 5).T
        diagrams = ripser(data)['dgms']
        H1_barcode = barcode_sorter(diagrams[1])
        longest_bar = H1_barcode[0][1] - H1_barcode[0][0]  # Returns length of longest bar in H1 barcode
        values_array[i][j] = longest_bar
        # if len(H1_barcode) == 1:
        #     values_array[i][j] = longest_bar
        # else:
        #     second_bar = H1_barcode[1][1] - H1_barcode[1][0]
        #     values_array[i][j] = longest_bar - second_bar

heatmap = plt.imshow(values_array, extent=(0, 2, 0, 1), interpolation='nearest')
# plt.colorbar(heatmap)
plt.show()
