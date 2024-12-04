#chaining comparison operators
marks=int(input("Enter Your Marks: "))
if marks>90:
    grade="A"
elif marks>80:
    grade="B"
elif marks>70:
    grade="C"
elif marks>60:
    grade="D"
else:
    grade="F"
print(f"Your Grade is: {grade}")