import pytest


@pytest.fixture(scope="class")  # 类级别夹具
def order():
    return []  # 记录顺序的列表


@pytest.fixture(scope="class", autouse=True)  # 类级别自动使用夹具
def c1(order):
    order.append("c1")  # 自动添加 "c1"


@pytest.fixture(scope="class")
def c2(order):
    order.append("c2")  # 添加 "c2"


@pytest.fixture(scope="class")
def c3(order, c1):  # 显式请求自动夹具 c1
    order.append("c3")  # 添加 "c3"


class TestClassWithC1Request:
    def test_order(self, order, c1, c3):  # 显式请求 c1, c3
        # 测试顺序：包含显式请求的自动夹具 c1 和被它触发执行的 c3
        assert order == ["c1", "c3"]


class TestClassWithoutC1Request:
    def test_order(self, order, c2):  # 只请求 c2，没有请求 c1
        # 即使没有请求 c1，它也会被自动执行！
        assert order == ["c1", "c2"]  # 断言包含 c1
