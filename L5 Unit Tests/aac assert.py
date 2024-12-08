from aaa import square
from aaa import square_
def main():
    test_square()
def test_square():
    assert square(2)==4
    assert square(3)==9
    assert square_(2)==4
    assert square_(3)==9
    # Will show AssertionError for the last one
main()