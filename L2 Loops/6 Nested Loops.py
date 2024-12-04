r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
for i in range(r):
    for j in range(c):
        print("#", end="")
    print() # could replace this whole indented block with print("#"*c)
# can replace both of i and j with _ at the same time
# as range n is nothing but a list of 0 to n-1