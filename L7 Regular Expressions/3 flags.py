'''
Such flags include:
re.IGNORECASE to make it case insensitive
re.MULTILINE to make a para apply to these contraints
re.DOTALL
'''
import re

email=input("Enter your E-Mail: ").strip()

if re.search(r"^(\w|\.)+@([\w]+\.)*[\w]+\.com$", email, re.IGNORECASE):

    # tabish@something.gmail.com is also valid
    
    '''
    The actual experssion at google:
    ^[a-zA-Z0-9.!#$%&'*+\/=?^_`|}~-]+@[a-zA-Z0-9](?:[a-zA{ -Z0-9-]{0,61}[a-zA-Z0-9])?( ?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
    Obviously, we should use some lib even to verify email
    '''
    
    print("VAlID")
else:
    print("INVALID")