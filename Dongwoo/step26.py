import numpy as np
from dezero import as_variable
from dezero import Variable
from dezero.utils import _dot_func
from dezero.utils import _dot_var
x=Variable(np.random.randn(2,3))
x.name='x'
print(_dot_var(x))
print(_dot_var(x, verbose=True))


# In[8]:


x0=Variable(np.array(1.0))
x1=Variable(np.array(1.0))
y=x0+x1
txt=_dot_func(y.creator)
print(txt)

