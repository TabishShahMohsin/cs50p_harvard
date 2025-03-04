# Simply 3rd party-libraries
# Module implemented in a folder and not a file
# Makes python much more powerful
# Can get some in PyPI website
# Python Package Index
# pypi.org can get it through command-line and browser
# Eg: pypi.org/project/cowsay
# Either get it by website, unzip it , get it in right place and use it.
# Or use pip, a package manager, comes with python nowadays.
    # Allows installing packages in your own computer
    #pip3 install cowsay
import sys
import cowsay
if len(sys.argv)==2:
    cowsay.cow("Hello, "+ sys.argv[1])
    #fortunately, using , instaead of + doesn't display the cow