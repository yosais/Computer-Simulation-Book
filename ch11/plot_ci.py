import numpy as np
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7]
y = [17, 7, 14, 18, 12, 22, 13]
plt.figure()
plt.plot([0, 7], [15, 15], 'k-', lw=2)  # Population Mean = 15
plt.errorbar(x, y, yerr=4, fmt='.')
plt.xlabel("Confidence Intervals")
plt.ylabel("Sample Means")
plt.show()