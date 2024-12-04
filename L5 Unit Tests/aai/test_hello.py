# To test a whole folder of tests on a function
# Testing aagHello.py with a folder of tests
#mkdir test
#code test/test_hello.py
from aagHello import hello

def test_default():
    hello()=="Hello, World"
def test_argument():
    hello("Tabish")==f"Hello, Tabish"
# Within the test directory we must make a file
# __init__.py
# even if this file is empty, it tells python to treat this folder as a package
# Not just a module but a package
# Package is/are modules organized inside a folder
# Can now run in the main directory: pytest aai