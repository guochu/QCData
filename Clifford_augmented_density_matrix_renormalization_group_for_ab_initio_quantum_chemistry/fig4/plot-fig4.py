import matplotlib.pyplot as plt
import numpy as np

filename = "c2-timing.dat"

chi_inv = []
t1 = []
t2 = []


with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "" or line.startswith("bonddim(chi)"):
            continue
        parts = line.split()
        if len(parts) < 5:
            continue
        chi_inv.append(float(parts[1]))
        t1.append(float(parts[2]))
        t2.append(float(parts[3]))


chi_inv = np.array(chi_inv)
t1 = np.array(t1)
t2 = np.array(t2)
ratio = t1/t2


_,ax = plt.subplots(figsize=(7, 5))
plt.plot(chi_inv, t1, "o-", label="CA-DMRG", color="tab:red")
plt.plot(chi_inv, t2, "s-", label="DMRG", color="tab:blue")

plt.xlabel("1/chi")
plt.ylabel("Time per sweep [s]")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
ax_inset = inset_axes(ax, width="40%", height="40%", loc="upper right")
ax_inset.plot(chi_inv, ratio, "s", color='black')
ax_inset.set_xlabel("1/chi")
ax_inset.set_ylabel("t(CA-DMRG) / t(DMRG)")

plt.tight_layout()
plt.show()
