import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
a = 65539
M = math.pow(2, 31)
seed = 123456
X = []
Y = []
Z = []
for i in range(10000):
    num1 = math.fmod(a * seed, M)
    num2 = math.fmod(a * num1, M)
    num3 = math.fmod(a * num2, M)
    seed = num2
    X.append(num1)
    Y.append(num2)
    Z.append(num3)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c='b', marker='o')
# Remove axis ticks for readability
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([]) 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()