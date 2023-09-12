# Libraries
import numpy as np
import math as math
import matplotlib.pyplot as plt


def control_enzymatic(h):
    """Calculate the enzymatic control of gates r and s. The gates are Potassium Gates.

    :param h: step time
    :return a graph of both potassium gates r and s"""
    # Initial Values: -------------------
    v = np.arange(-80, 40, h)  # mV
    pv = len(v)
    r = np.zeros(pv)
    s = np.zeros(pv)
    it = np.zeros(pv)
    gts = 7.5
    ek = -84  # mV
    r[0] = 0.0010678
    s[0] = 0.949
    it = gts * s[0] * r[0] * (v - ek)

    # Michael's-Menten Equations --------------
    for i in np.arange(0, pv - 1):
        tr = 0.0035 * math.exp(-((v[i]) / 30.0) ** 2) + 0.0015
        ts = 0.4812 * math.exp(-((v[i] + 52.45) / 14.97) ** 2) + 0.1414
        rm = 1.0 / (1.0 + math.exp((v[i] - 1.0) / -11.0))
        rs = 1.0 / (1.0 + math.exp((v[i] + 40.5) / 11.5))
        s[i + 1] = s[i] + h * ((rs - s[i]) / ts)
        r[i + 1] = r[i] + h * ((rm - r[i]) / tr)
        it[i + 1] = gts * r[i] * s[i] * (v[i] - ek)

    # Graphs--------------------------------------------
    figure, axis = plt.subplots(1, 2, figsize=(14, 5))
    axis[0].plot(v, s)
    axis[0].plot(v, r)
    plt.legend(["Gate r", "Gate s"], loc="best")
    axis[0].set_title("Graph Gates")
    axis[1].plot(v, it)
    axis[1].set_title("Potassium Current")
    plt.show()


control_enzymatic(0.001)
