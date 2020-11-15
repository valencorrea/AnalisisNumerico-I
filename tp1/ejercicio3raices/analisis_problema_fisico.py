import matplotlib.pyplot as plt
import numpy as np


def v(x):
    return ((np.pi) * x**2) * (12.75 - x) / 3

def derivada(x):
    return (-np.pi * (x**2)) + (2 * 12.75 * np.pi * x / 3)

def derivada_segunda(x):
    return (-2 * np.pi * x) + (2 * 12.75 * np.pi / 3)


