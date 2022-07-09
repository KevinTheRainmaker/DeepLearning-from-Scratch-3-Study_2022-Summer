from step03 import *


def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)  # f(x-h)
    y1 = f(x1)  # f(x+h)
    return (y1.data - y0.data) / (2*eps)


def complex_f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))


if __name__ == '__main__':
    f = Square()
    x = Variable(np.array(2.0))
    dy = numerical_diff(f, x)
    print(dy)

    x = Variable(np.array(0.5))
    dy = numerical_diff(complex_f, x)
    print(dy)
