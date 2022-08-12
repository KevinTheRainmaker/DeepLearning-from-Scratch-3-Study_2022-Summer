import numpy as np
from dezero import Function, Variable
from dezero.utils import plot_dot_graph

import math


class Sin(Function):
    def forward(self, x):
        y = np.sin(x)
        return y

    def backward(self, gy):
        x = self.inputs[0].data
        gx = gy * np.cos(x)
        return gx


def sin(x):
    return Sin()(x)


def my_sin(x, threshold=0.0001):
    y = 0
    for i in range(100_000):
        c = (-1) ** i / math.factorial(2 * i + 1)
        t = c * x ** (2 * i + 1)
        y = y + t

        if abs(t.data) < threshold:
            break
    return y


if __name__ == '__main__':
    x = Variable(np.array(np.pi/4))
    y = sin(x)
    y.backward()

    print(y.data)
    print(x.grad)

    x = Variable(np.array(np.pi/4))
    y = my_sin(x)
    y.backward()

    print(y.data)
    print(x.grad)

    x.name = 'x'
    y.name = 'y'
    plot_dot_graph(y, verbose=False, to_file='./Kangbeen/steps/step27-1.png')

    y2 = my_sin(x, threshold=1e-150)
    y.backward()

    x.name = 'x'
    y2.name = 'y'
    plot_dot_graph(y2, verbose=False, to_file='./Kangbeen/steps/step27-2.png')
