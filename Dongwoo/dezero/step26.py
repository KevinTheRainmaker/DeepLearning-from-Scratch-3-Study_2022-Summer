import numpy as np
from dezero import Variable
from dezero.utils import get_dot_graph, plot_dot_graph


x0= Variable(np.array(1.0))
x1= Variable(np.array(1.0))
y=x0+x1

x0.name='x0'
x1.name='x1'
y.name='y'

txt=get_dot_graph(y, verbose=False)
print(txt)

#save as dot file
with open('sample.dot','w') as o:
    o.write(txt)


