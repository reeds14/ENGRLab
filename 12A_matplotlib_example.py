# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:44:06 2026

@author: xfgom
"""

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Reed Scott (UIN: 838002005)
#               Sho Hiroi (UIN: 837008392)
#               Xavier Gomez (UIN: 538001968)
#               Izaac Almeida (UIN: 238008017)
# Section:      553
# Assignment:   Lab 12A
# Date:         17 October 2026

import numpy as np
import matplotlib.pyplot as plt


# Plot 1: Parabolas with different focal lengths

x = np.linspace(-2, 2, 100)

y1 = (1 / (4 * 2)) * x**2
y2 = (1 / (4 * 6)) * x**2

plt.figure()

plt.plot(x, y1, color='red', linewidth=2.0, label='f=2')
plt.plot(x, y2, color='blue', linewidth=6.0, label='f=6')

plt.title('Parabola plots with varying focal length')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()


# Plot 2: Cubic polynomial

x = np.linspace(-4, 4, 25)

y = 2*x**3 + 3*x**2 - 11*x - 6

plt.figure()

plt.plot(x, y, 'y*', markeredgecolor='black')

plt.title('Plot of cubic polynomial')
plt.xlabel('x values')
plt.ylabel('y values')

plt.show()


# Plot 3: Cosine and sine using two subplots

x = np.linspace(-2*np.pi, 2*np.pi, 100)

y1 = np.cos(x)
y2 = np.sin(x)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(x, y1, color='red', label='cos(x)')
plt.title('Plot of cos(x) and sin(x)')
plt.ylabel('y=cos(x)')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x, y2, color='gray', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y=sin(x)')
plt.legend()
plt.grid()

plt.show()