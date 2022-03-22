import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-11, 11, 1)
a = 2
b = 3
c = 4
d = 9
y = a*(x**3) + b*(x**2) + c*x + d 
 
print('Values of x: ', x)
print('Values of y: ', y)
 
plt.plot(x, y)
 
plt.title("Cubic Function")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()
