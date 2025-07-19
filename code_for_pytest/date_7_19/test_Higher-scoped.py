import pytest


@pytest.fixture(scope="session")
def order():
    return []  # 返回一个空列表，用于记录执行顺序


@pytest.fixture
def func(order):
    order.append("function")  # 向 order 列表添加 "function"


@pytest.fixture(scope="class")
def cls(order):
    order.append("class")  # 向 order 列表添加 "class"


@pytest.fixture(scope="module")
def mod(order):
    order.append("module")  # 向 order 列表添加 "module"


@pytest.fixture(scope="package")
def pack(order):
    order.append("package")  # 向 order 列表添加 "package"


@pytest.fixture(scope="session")
def sess(order):
    order.append("session")  # 向 order 列表添加 "session"


class TestClass:
    def test_order(self, func, cls, mod, pack, sess, order):
        # 测试函数：验证夹具的执行顺序是否按作用域从大到小
        assert order == ["session", "package", "module", "class", "function"]
