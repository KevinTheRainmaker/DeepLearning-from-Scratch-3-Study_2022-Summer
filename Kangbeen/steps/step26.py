import numpy as np

from dezero import Variable
from dezero.utils import plot_dot_graph
from dezero.utils import get_dot_graph

from step24 import goldstein

x = Variable(np.array(1.0))
y = Variable(np.array(1.0))
z = goldstein(x, y)
z.backward()

# print(get_dot_graph(z))

x.name = 'x'
y.name = 'y'
z.name = 'z'
plot_dot_graph(z, verbose=False,
               to_file='./Kangbeen/steps/step26.png')
