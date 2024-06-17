import pytest

@pytest.fixture
def browser():
    print("do")
    yield
    print("posle")


@pytest.fixture
def main_page(browser):
    pass
def test_first(browser, main_page, user):
    pass