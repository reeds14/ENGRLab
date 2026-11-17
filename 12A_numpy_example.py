# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:49:35 2026

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

# Create matrices A, B, and C
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)

# Print matrices
print("A =", A)
print()
print("B =", B)
print()
print("C =", C)
print()

# Calculate matrix product D = ABC
D = A @ B @ C

print("D =", D)
print()

# Print transpose of D
print("D^T =", D.T)
print()

# Calculate E = square root of D divided by 2
E = np.sqrt(D) / 2

print("E =", E)