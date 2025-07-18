import pytest


@pytest.fixture
def order():
    return []  # 返回一个空列表


@pytest.fixture
def top(order, innermost):  # 依赖 innermost 夹具
    order.append("top")  # 添加 "top"
