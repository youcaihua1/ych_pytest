# tests/subpackage/conftest.py 文件内容
import pytest


@pytest.fixture
def mid(order):  # 定义 mid 夹具
    order.append("mid subpackage")  # 添加 "mid subpackage"
