# re.match : No need to use the caret symbol
# re.fullmatch: No need to use the carret or the dollar symbol
import re

email=input("Enter your E-Mail: ")

if re.fullmatch(r"[\w]+@[a-z0-9_A-Z]+\.(com|gov|edu|in)", email):
    print("Valid")
else:
    print("Invalid")