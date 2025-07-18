import pytest


@pytest.fixture
def order():
    return []  # 创建一个空列表


@pytest.fixture
def append_first(order):
    order.append(1)  # 向列表添加 1 （假设这里可能出错）


@pytest.fixture
def append_second(order, append_first):  # 依赖 append_first
    order.extend([2])  # 向列表添加 2


@pytest.fixture(autouse=True)  # 自动使用，无需在测试函数中声明
def append_third(order, append_second):  # 依赖 append_second
    order += [3]  # 向列表添加 3


def test_order(order):
    assert order == [1, 2, 3]  # 验证列表最终是 [1, 2, 3]
