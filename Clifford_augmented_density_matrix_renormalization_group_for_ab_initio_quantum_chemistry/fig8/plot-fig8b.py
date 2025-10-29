import matplotlib.pyplot as plt
import numpy as np

filename = "NH3-neq-gates.dat"


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

plt.ylim(0, 141)
plt.xlabel('Site')
plt.ylabel('Step')

plt.tight_layout()
plt.show()
