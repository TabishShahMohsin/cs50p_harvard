# Regular expression, or regrexes
# To check the inputed values correspond to out expectations
# To check that the user entered a proper email
email=input("Enter E-Mail Address: ")
if "@" in email:
    print("Valid")
else:
    print("Invalid")