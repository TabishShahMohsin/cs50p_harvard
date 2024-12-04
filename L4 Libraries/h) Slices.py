import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")
for name in sys.argv[1:]:
    #[1:] slicing from the element of index 1 till the end of the list
    #negative number counts from the other end starting from -1 not from 0
    print("Hello,", name)