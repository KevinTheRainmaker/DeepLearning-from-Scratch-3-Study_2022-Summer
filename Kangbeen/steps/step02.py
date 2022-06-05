import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x) # 구체적인 계산은 forward에서 진행
        output = Variable(y)
        return output
    
    def forward(self, x):
        raise NotImplementedError()
    
class Square(Function): # Function 클래스 상속
    def forward(self, x):
        return x ** 2
    
x = Variable(np.array(10))
f = Square()
y = f(x)

print(type(y))
print(y.data)