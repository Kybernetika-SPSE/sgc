import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = False 

K = 0.8
U_TH = 2.0

U_GS = np.linspace(0, 10, 300)
I_D = []

for u_gs in U_GS:
    if u_gs <= U_TH:
        I_D.append(0)
    else:
        I_D.append(0.5 * K * (u_gs - U_TH)**2)

plt.figure()

plt.plot(U_GS, I_D, label=r"$I_D = f(U_{GS})$")

plt.title("MOSFET – přenosová charakteristika")

plt.xlabel(r"$U_{GS}$ [V]")
plt.ylabel(r"$I_D$ [A]")

plt.grid(True)
plt.legend()
plt.show()