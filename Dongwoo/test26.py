import numpy as np
from dezero import Variable
from dezero.utils import plot_dot_graph, _dot_func

x0=Variable(np.array(1.0))
x1=Variable(np.array(1.0))
y=x0+x1
txt=_dot_func(y.creator)
print(txt)
