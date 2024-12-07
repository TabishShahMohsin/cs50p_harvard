import sys
# The first element would be the name of the file
# Run the program by python3 6\ Command\ Line\ Arguments.py  Tabish
# The argv[0]=6 Command Line Arguments.py, can be used for debugging
# The argv[1]= Tabish
# docs.python.org/3/library/sys.html
# Giving inputs directly from command line.
#sys.argv(): argument vector
    #somehow simply contains all the words that were typed in the prpompt
    #it returns a list with 1st element being the fist word and so on
if len(sys.argv)==2:
    #as len() in python "EXISTS", u don't get to use argc
    print("Hello, my name is", sys.argv[1])
    #Command-line argumetns are supposed to be for the coders, increasing their productivity but more arcane
else:
    print("Enter a single argument after name of the file.")
#But still can go around this by writing in quotes: "Tabish Shah Mohsin"
#stores the whole name with spaces as first element, we get access to that as well