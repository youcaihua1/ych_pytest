import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple") # 返回一个名为"apple"的Fruit对象


@pytest.fixture
def fruit_basket(my_fruit):  # 这个夹具使用了上面定义的my_fruit夹具
    return [Fruit("banana"), my_fruit]  # 返回一个包含"banana"和上面my_fruit的水果篮


def test_my_fruit_in_basket(my_fruit, fruit_basket):  # 测试函数依赖两个夹具
    assert my_fruit in fruit_basket  # 断言my_fruit在fruit_basket中
