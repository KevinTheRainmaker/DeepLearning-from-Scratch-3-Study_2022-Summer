import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

if __name__ == '__main__':
    # 변수 인스턴스에 데이터 대입    
    data = np.array(1.0)
    x = Variable(data)
    print(x.data)

    # 다른 데이터로 변수 내용 덮어쓰기
    x.data = np.array(2.0)
    print(x.data)