import numpy as np


class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError(f'{type(data)} type is not supported.')

        self.data = data
        self.grad = None
        self.creator = None

    def set_creator(self, func):
        self.creator = func

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = [self.creator]
        while funcs:
            f = funcs.pop()
            gys = [output.grad for output in f.outputs]  # 1
            gxs = f.backward(*gys)  # 2
            if not isinstance(gxs, tuple):  # 3
                gxs = (gxs,)

            for x, gx in zip(f.inputs, gxs):  # 4
                x.grad = gx

                if x.creator is not None:
                    funcs.append(x.creator)


def as_array(x):
    if np.array(x):
        return np.array(x)
    return x


class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)  # __call__ 에서 unpack
        if not isinstance(ys, tuple):  # 튜플이 아닌 경우
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        for output in outputs:
            output.set_creator(self)

        self.inputs = inputs
        self.outputs = outputs

        return outputs if len(outputs) > 1 else outputs[0]


class Add(Function):
    def forward(self, x0, x1):
        y = x0 + x1
        return y

    def backward(self, gy):
        return gy, gy


class Square(Function):
    def forward(self, x):
        y = x ** 2
        return y

    def backward(self, gy):
        x = self.inputs[0].data  # 수정 전: x = self.input.data
        gx = 2 * x * gy
        return gx


def add(x0, x1):
    return Add()(x0, x1)


def square(x):
    f = Square()
    return f(x)


if __name__ == '__main__':
    x = Variable(np.array(2.0))
    y = Variable(np.array(3.0))

    z = add(square(x), square(y))
    z.backward()
    print(z.data)  # 2^2 + 3^2 = 13.0
    print(x.grad)  # 2^2 = 4.0
    print(y.grad)  # (y^2)' = 2y / 2 * 3 = 6.0
