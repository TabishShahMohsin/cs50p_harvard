i=j=0
#computer scientists count from 0
#ctrl/cmd +c will block the infinite loop
while i<3:
    print("meaow")
    i=i+1
    #or i+=1
    #but can't use i++
    #this is not comparing as = is the assignment operator
for _ in range(0,3):
    #could use j instead of _
    #_ can be used to show that the variable had be to created just to use here and we don't need it afterward
    # range is a pre-defined function
    #if one argument only range(n)=[0,1,2,...n-1]
    #if 2 arguments range(4,n)=[4,5,6,,,,n-1]
    #if 3 arguemnts range(4,n,2)=[4,6,8,10,12,,,,even no just before n]
    
    print("Meaow")
print("MEAOW\n"*3, end="") # This is more or a pythonic approach
# end="" is used to prevent the extra \n after print statement is executed
