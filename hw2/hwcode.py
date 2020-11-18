import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 100)
def sigmoidA(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x) + np.exp(-x))

def sigmoid(x):
    return 1/(1+np.exp(-x))

y = [sigmoidA(i) for i in x]
y2 = [sigmoid(i) for i in x]
plt.plot(x, y, label='sigmoid_A')
plt.plot(x, y2, label='sigmoid')
plt.legend()
plt.title('sigmoid_A vs sigmoid distribution')
plt.savefig('sigmoid_A vs sigmoid')
plt.show()