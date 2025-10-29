import matplotlib.pyplot as plt
import numpy as np

filename = "h2o.dat"
# filename = "nh3.dat"
# filename = "n2.dat"
# filename = "c2.dat"

sweep = []
d1 = []


with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "" or line.startswith("iter"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        sweep.append(float(parts[0]))
        d1.append(float(parts[1]))

sweep = np.array(sweep)
d1 = np.array(d1)


plt.figure(figsize=(7, 5))
plt.plot(sweep, d1, "s-", color="tab:green")


plt.xlabel("Sweep")
plt.ylabel("Max bond dimension")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
