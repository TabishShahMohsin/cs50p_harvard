import sys
#can't call a file with a number as first letter in its name
#don't need to mention .py, atleast if it is in the same directory
from lOwnLibrary12 import goodbye
if len(sys.argv)==2:
    goodbye(sys.argv[1])