from aaa import square
# Checking infinity such cases is not our goal
# But to check the probable corner cases, to ensure the code still continues to run as it should
def main():
    test_square()
def test_square():
    try:
        assert square(2)==4
    except:
        print("2 square was not 4")
    try:
        assert square(3)==9
    except:
        print("3 square was not 9")
if __name__ == "__main__":
    main()
