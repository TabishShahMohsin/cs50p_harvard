import sys
if len(sys.argv)<2:
    sys.exit("Too few arguments")
for i in range(1,len(sys.argv)):
    print("Hello,", sys.argv[i])
#When it reaches the bottom it exits the file anyways
#This is just to ensure it exits before reaching the very end
