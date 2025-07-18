# tests/test_top.py 文件内容
import pytest


@pytest.fixture
def innermost(order):  # 定义 innermost 夹具
    order.append("innermost top")  # 添加 "innermost top"


def test_order(order, top):  # 测试函数
    assert order == ["innermost top", "top"]  # 验证顺序
