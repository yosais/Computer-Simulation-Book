import random as rnd
import pandas
from pandas.tools.plotting import lag_plot
import matplotlib.pyplot as plt
s = pandas.Series([rnd.random() for i in range(10000)])
plt.figure()
lag_plot(s, marker='o', color='grey')
plt.xlabel('Random Number - s[i]')
plt.ylabel('Lag1(Random Number) - s[i+1]')
plt.show()