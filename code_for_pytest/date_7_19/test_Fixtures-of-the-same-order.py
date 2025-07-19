import pytest


@pytest.fixture
def order():
    return []  # 返回空列表用于记录顺序


@pytest.fixture
def a(order):
    order.append("a")  # 添加 "a"


@pytest.fixture
def b(a, order):  # 请求 a
    order.append("b")  # 添加 "b"


@pytest.fixture
def c(b, order):  # 请求 b
    order.append("c")  # 添加 "c"


@pytest.fixture
def d(c, b, order):  # 请求 c 和 b
    order.append("d")  # 添加 "d"


@pytest.fixture
def e(d, b, order):  # 请求 d 和 b
    order.append("e")  # 添加 "e"


@pytest.fixture
def f(e, order):  # 请求 e
    order.append("f")  # 添加 "f"


@pytest.fixture
def g(f, c, order):  # 请求 f 和 c
    order.append("g")  # 添加 "g"


def test_order(g, order):
    # 测试函数：验证夹具是否严格按依赖关系顺序执行
    assert order == ["a", "b", "c", "d", "e", "f", "g"]
