# tests/subpackage/test_subpackage.py 文件内容
import pytest


@pytest.fixture
def inner(order, mid, a_fix):  # 依赖于 order, mid 和 a_fix 夹具
    order.append("inner subpackage")  # 向 order 列表添加字符串


def test_order(order, inner):  # 测试函数，依赖于 order 和 inner 夹具
    assert order == ["b_fix", "mid subpackage", "a_fix", "inner subpackage"]  # 断言 order 列表的内容
