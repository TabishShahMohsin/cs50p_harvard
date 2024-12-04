#float allows decimal point
#python allows add, remainder, subtract, divide, multiply
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
#using float to avoid catenation
#better to use float here only so that we don't need to covert it again and again.
#By defuault input returns strings
#float() changes the data type forcefully
print(a+b) #one can next functions in python
#documentation of round: round(number[, ndigits])
# this means that  it takes only 1 number as argument
# the n digits part indicate that one more number can be optionally given to tell till which digit.
z=round(a+b, 5)
print(f"{z:.2f}")
print(z)
print(f"{z:,}")# syntax for this line is weired and hence to be seem from documentation
#in python a float value can go upto specific places only