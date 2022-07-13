import numpy as np
from queue import PriorityQueue


class Variable:
    def __init__(self, data):
        if data is not None:
            if not isinstance(data, np.ndarray):
                raise TypeError(f'{type(data)} type is not supported.')

        self.data = data
        self.grad = None
        self.creator = None
        self.generation = 0  # 세대를 기록하는 변수 generation

    def set_creator(self, func):
        self.creator = func
        self.generation = func.generation + 1  # 세대 기록: 부모 세대 +1

    def backward(self):
        if self.grad is None:
            self.grad = np.ones_like(self.data)

        funcs = PriorityQueue()
        seen_set = set()

        def add_func(f):
            if f not in seen_set:
                funcs.put(f)
                seen_set.add(f)

        add_func(self.creator)

        while not funcs.empty():
            f = funcs.get()
            gys = [output.grad for output in f.outputs]
            gxs = f.backward(*gys)
            if not isinstance(gxs, tuple):
                gxs = (gxs,)

            for x, gx in zip(f.inputs, gxs):
                if x.grad is None:
                    x.grad = gx
                else:
                    x.grad = x.grad + gx

                if x.creator is not None:
                    add_func(x.creator)

    def cleargrad(self):
        self.grad = None


def as_array(x):
    if np.isscalar(x):
        return np.array(x)
    return x


class Function:
    def __call__(self, *inputs):
        xs = [x.data for x in inputs]
        ys = self.forward(*xs)
        if not isinstance(ys, tuple):
            ys = (ys,)
        outputs = [Variable(as_array(y)) for y in ys]

        # 입력 변수의 세대 중 더 큰 값을 함수의 세대로 설정
        self.generation = max([x.generation for x in inputs])

        for output in outputs:
            output.set_creator(self)

        self.inputs = inputs
        self.outputs = outputs

        return outputs if len(outputs) > 1 else outputs[0]

    def __lt__(self, other):
        return self.generation > other.generation


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
    a = square(x)
    y = add(square(a), square(a))
    y.backward()

    print(y.data)
    print(x.grad)
