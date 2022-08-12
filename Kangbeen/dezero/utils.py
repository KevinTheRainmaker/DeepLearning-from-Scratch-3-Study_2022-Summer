import os
import subprocess  # 파이썬 외부 프로세스 입출력 및 실행 제어 라이브러리


def _dot_var(v, verbose=False):  # 로컬에서만 사용할 함수: 외부에서 부를 수 없다
    # 변수 노드 프레임
    dot_var = '{} [label="{}", color=orange, style=filled]\n'

    name = '' if v.name is None else v.name  # name이 None이면 빈 str로 변환하여 포맷을 통일

    if verbose and v.data is not None:
        if v.name is not None:
            name += ': '
        # verbose를 True로 설정 시 name에 shape와 type을 추가
        name += str(v.shape) + ' ' + str(v.dtype)
    return dot_var.format(id(v), name)


def _dot_func(f):
    # 함수 노드 프레임
    dot_func = '{} [label="{}", color=lightblue, style=filled, shape=box]\n'
    txt = dot_func.format(id(f), f.__class__.__name__)  # 계산 함수 클래스명을 노드 name으로

    dot_edge = '{} -> {}\n'
    for x in f.inputs:
        txt += dot_edge.format(id(x), id(f))
    for y in f.outputs:
        txt += dot_edge.format(id(f), id(y()))  # y는 weakref
    return txt


def get_dot_graph(output, verbose=True):
    txt = ''
    funcs = []
    seen_set = set()

    def add_func(f):
        if f not in seen_set:
            funcs.append(f)
            funcs.sort(key=lambda x: x.generation)
            seen_set.add(f)

    add_func(output.creator)
    txt += _dot_var(output, verbose)

    while funcs:
        func = funcs.pop()
        txt += _dot_func(func)
        for x in func.inputs:
            txt += _dot_var(x, verbose)

            if x.creator is not None:
                add_func(x.creator)
    return 'digraph g{\n' + txt + '}'


def plot_dot_graph(output, verbose=True, to_file='graph.png'):
    dot_graph = get_dot_graph(output, verbose)

    # dot 데이터를 파일에 저장
    tmp_dir = os.path.join(os.path.expanduser('~'), '.dezero')
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    graph_path = os.path.join(tmp_dir, 'tmp_graph.dot')

    with open(graph_path, 'w') as f:
        f.write(dot_graph)

    # dot 명령 호출
    extension = os.path.splitext(to_file)[1][1:]  # 확장자
    cmd = f'dot {graph_path} -T {extension} -o {to_file}'
    subprocess.run(cmd, shell=True)
