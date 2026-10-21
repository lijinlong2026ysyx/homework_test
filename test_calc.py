import pytest
from calc import add, div

def test_add():
    assert add(2, 3) == 5

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
