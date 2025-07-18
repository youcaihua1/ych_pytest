# tests/subpackage/test_subpackage.py 文件内容
import pytest


@pytest.fixture
def innermost(order, mid):  # 覆盖定义 innermost 夹具，依赖 mid
    order.append("innermost subpackage")  # 添加 "innermost subpackage"


def test_order(order, top):  # 测试函数
    assert order == ["mid subpackage", "innermost subpackage", "top"]  # 验证顺序
