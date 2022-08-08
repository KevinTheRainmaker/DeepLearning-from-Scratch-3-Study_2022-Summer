if '__file__' in globals():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from dezero import Variable
import numpy as np


x = Variable(np.array(1.0))
print(x)
