# test_9.py
import pytest


@pytest.fixture
def database():
    print("\nCreating database...")  # setup
    yield
    print("\nClosing database...")  # teardown


@pytest.fixture
def user(database):  # 依赖 database fixture
    return {"name": "Alice", "id": 1}


def test_user_info(user):
    assert user["name"] == "Alice"
