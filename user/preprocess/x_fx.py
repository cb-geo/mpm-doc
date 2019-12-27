%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

from pylab import rcParams
rcParams['figure.figsize'] = 10, 10
plt.rcParams.update({'font.size': 22})

fig = plt.figure()
ax = plt.axes()


x = np.array([0.0, 0.5, 1.0, 1.5])
y = np.array([0.0, 1.0, 1.0, 0.0])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

plt.axis([0, 1.5, 0, 1.2]);
ax.plot(x, y,  color='blue');
