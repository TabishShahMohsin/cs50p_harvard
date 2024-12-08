import pytest
from aaa import square
# For it to test atleat one of each type not break at the first failure
def test_positive():
    assert square(1)==1
    assert square(2)==4
    assert square(3)==9
def test_negative():
    assert square(-2)==4
    assert square(-1)==1
def test_zero():
    assert square(0)==0
    
# Can also check for errors to work as expected
def test_str():
    with pytest.raises(TypeError):
        square("Cat")