import matplotlib.pyplot as plt
import numpy as np
from sympy import *


def show(func, roots, var):
    x = Symbol(var)
    func = sympify(func)
    maxRoot = max(roots)
    minRoot = min(roots)
    x_in = np.arange(minRoot-0.1, maxRoot + 0.1, 0.01)
    y = []
    for entry in x_in:
        y.append(func.evalf(subs={x: entry}))
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.plot(x_in, y, label="Function")
    plt.scatter(roots, np.zeros((len(roots))), label="Roots", color="red")
    plt.legend(loc=1)
    plt.show()
