import matplotlib.pyplot as plt
import numpy as np

# filename = "h2o.dat"
# filename = "nh3.dat"
# filename = "n2.dat"
filename = "c2.dat"


data = np.loadtxt(filename,skiprows=1)

x = data[:, 0]
y = data[:, 1]
l = data[:, 2]

color_map = {
    1: 'blue',
    2: 'yellow',
    4: 'red',
}

plt.figure(figsize=(6, 5))
sc = plt.scatter(x, y, marker='_', c=[color_map.get(il) for il in l], s=200, edgecolors='none')

plt.ylim(0, 200)
plt.xlabel('Site')
plt.ylabel('Step')

plt.tight_layout()
plt.show()
