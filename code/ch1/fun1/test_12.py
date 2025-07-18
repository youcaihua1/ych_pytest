import pytest


@pytest.fixture
def order():  # 模块作用域夹具
    return []


@pytest.fixture
def outer(order, inner):  # 模块作用域夹具，请求另一个夹具 inner
    order.append("outer")  # 操作列表


class TestOne:
    @pytest.fixture
    def inner(self, order):  # TestOne 类作用域夹具
        order.append("one")  # 操作列表

    def test_order(self, order, outer):  # TestOne 类内测试
        assert order == ["one", "outer"]  # 验证列表顺序


class TestTwo:
    @pytest.fixture
    def inner(self, order):  # TestTwo 类作用域夹具 (与TestOne中的同名)
        order.append("two")  # 操作列表

    def test_order(self, order, outer):  # TestTwo 类内测试
        assert order == ["two", "outer"]  # 验证列表顺序
