from aagHello import hello
def test_argument():
    for i in ["Tabish", "Aarish", "Noman"]:
        assert hello(i)==f"Hello, {i}"
    # assert functions are made to test by arguments into fucntions and return values (Pure Functions)
    # They aren't made to test side effects
    # Better to write small tests, bcz don't want them to be the error
def test_default():
    assert hello()=="Hello, World"
    # Better to seperate potentially different cases, to get more ideas of errors