from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(0,100, (200,2))

x = data.T[0]
y = data.T[1]

def dist(a, b, ax=1):
    return np.linalg.norm(a-b, axis=ax)

k=3
D_x = np.random.randint(0, np.max(data), size=k)
D_y = np.random.randint(0, np.max(data), size=k)
D = np.array(list(zip(D_x, D_y)))

D_old = np.zeros(D.shape)
clusters = np.zeros(len(data))
iteration_flag = dist(D, D_old, 1)
tmp = 1
while iteration_flag.any()!=0 and tmp<20:
    for i in range(len(D)):
        distances = dist(data[i], D, 1)
        clusters[i] = np.argmin(distances)
    D_old = deepcopy(D)
    for i in range(k):
        points = [data[j] for j in range(len(data)) if clusters[j] ==i]
        if len(points)!=0:
            D[i] = np.mean(points, axis=0)
    print('循环第{}次'.format(tmp))
    tmp += 1
    print(iteration_flag)
    iteration_flag = dist(D, D_old, 1)
colors = ['r', 'g', 'b', 'y', 'c', 'm']
plt.scatter(x, y)
plt.show()
