import numpy as np

# 역전파를 저장하는 부분 추가 grad
class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None

# 역전파 확인하는 함수 추가
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input #backward에 활용하기 위해서 작성
        return output

    def forward(self, x):
        raise NotImplementedError()

    def backward(self, gy):
        raise NotImplementedError()


# Square, Exp 쿨래스 추가 구현
class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y

    def backward(self, gy):
        x = self.input.data
        gx = 2 * x * gy
        return gx

class Exp(Function):
    def forward(self, x):
        y = np.exp(x)
        return y

    def backward(self, gy):
        x = self.input.data
        gx = np.exp(x) * gy
        return gx

