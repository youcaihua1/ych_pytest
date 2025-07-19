# tests/subpackage/conftest.py 文件内容
import pytest


@pytest.fixture(autouse=True)  # autouse=True 表示自动使用该夹具
def mid(order, b_fix):  # 依赖于 order 和 b_fix 夹具
    order.append("mid subpackage")  # 向 order 列表添加字符串
