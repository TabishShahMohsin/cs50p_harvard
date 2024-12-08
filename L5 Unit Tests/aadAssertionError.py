from aaa import square
from aaa import square_
# Checking infinity such cases is not our goal
# But to check the probable corner cases, to ensure the code still continues to run as it should
def main():
    test_square()
def test_square():
    try:
        assert square_(2)==4
    except AssertionError:
        # No need but better to write AssertionError, as it might execute the except block with other errors also
        # Like if I had used the wrong name for the function, it would have failed all the tests
        print("2 square was not 4")
    try:
        assert square_(3)==9
    except:
        print("3 square was not 9")
if __name__ == "__main__":
    main()
