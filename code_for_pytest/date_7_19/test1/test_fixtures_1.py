import pytest


@pytest.fixture
def order():
    return []  # 记录顺序的列表


@pytest.fixture
def a(order):
    order.append("a")  # 添加 "a"


@pytest.fixture
def b(a, order):  # 请求 a
    order.append("b")  # 添加 "b"


@pytest.fixture(autouse=True)  # 关键变化：c 是自动使用的！
def c(b, order):  # 请求 b
    order.append("c")  # 添加 "c"


@pytest.fixture
def d(b, order):  # 请求 b (不再请求 c)
    order.append("d")  # 添加 "d"


@pytest.fixture
def e(d, order):  # 请求 d
    order.append("e")  # 添加 "e"


@pytest.fixture
def f(e, order):  # 请求 e
    order.append("f")  # 添加 "f"


@pytest.fixture
def g(f, c, order):  # 请求 f 和 c
    order.append("g")  # 添加 "g"


def test_order_and_g(g, order):
    # 测试函数：验证执行顺序
    assert order == ["a", "b", "c", "d", "e", "f", "g"]  # 现在顺序可确定
