import matplotlib.pyplot as plt
import numpy as np

filename = "h2o.dat"
# filename = "nh3.dat"
# filename = "n2.dat"
# filename = "c2.dat"

sweep = []
d1 = []
d2 = []


with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "" or line.startswith("E(") or line.startswith("sweep"):
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        sweep.append(float(parts[0]))
        d1_val = parts[1]
        d2_val = parts[2]
        d1.append(float(d1_val) if d1_val != "--" else np.nan)
        d2.append(float(d2_val) if d2_val != "--" else np.nan)

sweep = np.array(sweep)
d1 = np.array(d1)
d2 = np.array(d2)


plt.figure(figsize=(7, 5))
plt.plot(sweep, d1, "o-", label="CA-DMRG", color="tab:red")
plt.plot(sweep, d2, "s-", label="DMRG", color="tab:blue")

plt.yscale("log")
from matplotlib.ticker import LogLocator
plt.gca().yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.array([2.5,5.0,7.5])*0.1))
plt.xlabel("Sweep")
plt.ylabel("Error [Hartree]")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.tight_layout()
plt.show()
