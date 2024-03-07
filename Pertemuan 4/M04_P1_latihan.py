print("\033c")

import numpy as np
import matplotlib.pyplot as plt

#Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-12, 12, 10000)
plt.figure(figsize=(12, 12))

#Tentukan persamaan matematika yang diinginkan

y1 = 0 +(25-x**2)**0.5
y2 = 0 -(25-x**2)**0.5

y3 = 5 + (5-(x+5)**2)**0.5
y4 = 5 - (5-(x+5)**2)**0.5

y5 = 5 + (5-(x-5)**2)**0.5
y6 = 5 - (5-(x-5)**2)**0.5


plt.plot(x, y1, '-k', label='Kepala')
plt.plot(x, y2, '-k')
plt.plot(x, y3, '-k', label='Telingan Kiri')
plt.plot(x, y4, '-k')
plt.plot(x, y5, '-k', label='Telinga Kanan')
plt.plot(x, y6, '-k')

plt.fill_between(x, y1, y2, color='black', alpha=1)
plt.fill_between(x, y3, y4, color='black', alpha=1)
plt.fill_between(x, y5, y6, color='black', alpha=1)

plt.legend(loc='upper center')
plt.grid()
plt.show()