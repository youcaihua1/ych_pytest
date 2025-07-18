import time
import random


def test_with_delay():
    # 测试前暂停
    time.sleep(random.uniform(1, 2))

    # 断言后暂停
    assert (1, 2, 3) == (1, 2, 3)
