# To prevent adding these many try and except
# Unit tests means to test units of your code meaning funcitons in it
from aaa import square
def test_square():
    # Must use test_square function
    # Can't use square_test()
    assert square(1)==1
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-1)==1
    assert square(0)==0
    # pytest will run the test for me and also tell which of the process failed on the screen
    # no main no try and error and no print no if
# Pytest give . for pass and F for fail
    