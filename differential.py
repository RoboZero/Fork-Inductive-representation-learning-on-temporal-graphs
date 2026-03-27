import numpy as np

m = []
l = [50, 40, 30, 20, 10]
d = [50,0,0,0,0]

m.append(d.copy())
for t in range(4):
    for i in range(1, len(d)):
        d[i] += d[i-1]/2 
    m.append(d.copy())

# np.set_printoptions
np_m = np.array(m)
print(np_m)

# Each part affects another.