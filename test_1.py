import pytest
from app1 import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 4) == -4
    assert sub(-1, -1) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(-1, 3) == -3
    assert mul(0, 5) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-6, 3) == -2
    assert div(5, 2) == 2.5

    # Check division by zero
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
