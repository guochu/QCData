import matplotlib.pyplot as plt
import numpy as np

filename = "n2-eos.dat"

#which_to_plot = 'energies'
which_to_plot = 'errors'


x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []


with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "" or line.startswith("a/a0"):
            continue
        parts = line.split()
        if len(parts) < 11:
            continue
        x.append(float(parts[0]))
        if which_to_plot == 'energies':
            y1.append(float(parts[1]))
            y2.append(float(parts[2]))
            y3.append(float(parts[3]))
            y4.append(float(parts[4]))
            y5.append(float(parts[9]))
            y6.append(float(parts[10]))
        elif which_to_plot == 'errors':
            y1_val = parts[5]
            y2_val = parts[6]
            y3_val = parts[7]
            y4_val = parts[8]
            y1.append(float(y1_val) if y1_val != "--" else np.nan)
            y2.append(float(y2_val) if y2_val != "--" else np.nan)
            y3.append(float(y3_val) if y3_val != "--" else np.nan)
            y4.append(float(y4_val) if y4_val != "--" else np.nan)

        

x = np.array(x)
y1 = np.array(y1)
y2 = np.array(y2)
y3 = np.array(y3)
y4 = np.array(y4)
y5 = np.array(y5)
y6 = np.array(y6)

if which_to_plot == 'energies':
    plt.figure(figsize=(7, 5))
    plt.plot(x, y1, "s", label="DMRG (d=60)", color="tab:blue")
    plt.plot(x, y2, "^", label="DMRG (d=80)", color="tab:blue")
    plt.plot(x, y3, "s", label="CA-DMRG (d=60)", color="tab:red")
    plt.plot(x, y4, "^", label="CA-DMRG (d=80)", color="tab:red")
    plt.plot(x, y5, "-", label="FCI", color="tab:grey")
    plt.plot(x, y6, "--", label="RHF", color="tab:orange")
    plt.xlabel("Nuclear separation [Angstrom]")
    plt.ylabel("Energy [Hartree]")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
elif which_to_plot == 'errors':
    plt.figure(figsize=(7, 5))
    plt.plot(x, y1, "s", label="DMRG (d=60)", color="tab:blue")
    plt.plot(x, y2, "^", label="DMRG (d=80)", color="tab:blue")
    plt.plot(x, y3, "s", label="CA-DMRG (d=60)", color="tab:red")
    plt.plot(x, y4, "^", label="CA-DMRG (d=80)", color="tab:red")

    plt.yscale("log")
    from matplotlib.ticker import LogLocator
    plt.gca().yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.array([2.5,5.0,7.5])*0.1))
    plt.xlabel("Nuclear separation [Angstrom]")
    plt.ylabel("Error [Hartree]")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()