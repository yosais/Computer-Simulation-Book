# The generated random sequence will fill the 2D space in a uniform fashion
import numpy as np
import pandas
from pandas.tools.plotting import lag_plot
import matplotlib.pyplot as plt
s = pandas.Series(0.1 * np.random.rand(1000) + 0.9 * np.sin(np.linspace(-99 * np.pi, 99 * np.pi, num=1000)))
plt.figure()
lag_plot(s, marker='o', color='grey')
plt.xlabel('s[i]')
plt.ylabel('s[i+1]')
plt.show()