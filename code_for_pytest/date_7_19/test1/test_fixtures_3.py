import pytest


@pytest.fixture
def order():
    return []  # 记录顺序的列表


# 普通夹具 c1
@pytest.fixture
def c1(order):
    order.append("c1")  # 添加 "c1"


# 普通夹具 c2
@pytest.fixture
def c2(order):
    order.append("c2")  # 添加 "c2"


class TestClassWithAutouse:
    # 类内的自动使用夹具 c3，它请求了 order 和 c2
    @pytest.fixture(autouse=True)
    def c3(self, order, c2):
        order.append("c3")  # 添加 "c3"

    # 测试1：显式请求了 c1
    def test_req(self, order, c1):
        # 验证顺序：c3 自动执行 + 它所依赖的 c2 自动执行 -> "c2", "c3"，然后才是显式请求的 c1 -> "c1"
        assert order == ["c2", "c3", "c1"]

    # 测试2：没有请求任何额外夹具
    def test_no_req(self, order):
        # 验证顺序：仍然只有 c3 自动执行 + 它所依赖的 c2 自动执行 -> "c2", "c3"
        assert order == ["c2", "c3"]


class TestClassWithoutAutouse:
    # 测试3：显式请求了 c1
    def test_req(self, order, c1):
        # 验证顺序：由于本类没有自动夹具触发 c2，只执行了显式请求的 c1 -> "c1"
        assert order == ["c1"]

    # 测试4：没有请求任何夹具
    def test_no_req(self, order):
        # 验证顺序：没有请求任何夹具，order 保持为空
        assert order == []
