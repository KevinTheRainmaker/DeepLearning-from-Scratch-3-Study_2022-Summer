import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        f = self.creator  # 1
        if f is not None:  # f가 역순 방향 마지막 연산이 아니면
            x = f.input  # 2
            x.grad = f.backward(self.grad)  # 3
            # 하나 앞 변수의 backward 메서드를 재귀적으로 호출한다
            x.backward()


class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        output.set_creator(self)  # 출력 변수에 창조자 설정
        self.input = input
        self.output = output  # 출력 저장
        return output


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


if __name__ == '__main__':
    A = Square()
    B = Exp()
    C = Square()

    # 순전파
    x = Variable(np.array(0.5))
    a = A(x)
    b = B(a)
    y = C(b)

    # 역전파
    y.grad = np.array(1.0)
    y.backward()
    print(x.grad)
