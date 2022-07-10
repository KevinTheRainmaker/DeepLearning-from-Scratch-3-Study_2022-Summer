import numpy as np


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


class Variable:
    def __init__(self, data):
        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        funcs = [self.creator]
        while funcs:
            f = funcs.pop()  # 함수를 가져온다
            x, y = f.input, f.output  # 함수의 입출력을 가져온다
            x.grad = f.backward(y.grad)  # backward 메서드 호출

            if x.creator is not None:
                funcs.append(x.creator)  # 이전 함수를 리스트에 추가


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
