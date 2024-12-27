# A lib exits that does all of that for us
import re
#  http://docs.python.org/3/library/re.html
# re.search(pattern, string, flags=0)
# pattern is want you want to search
# Which string you would want to search
# flag: is used to modify the behaviour of the function, but will not be using it
email=input("Enter your email: ").strip()

if re.search(r"^[\w]+@[a-z0-9_A-Z]+\.(com|gov|edu|in)$", email):
    # can use [\w|\s] for accepting spaces
    # You can use /w for alphanumeric and _ or a-z0-9_A-Z
    # Better to use raw string for regular expressinos all the time
    # this argument ".+@.+" will be read from left to right, and then email will be compared to this fromat
        # It would use finite state machine to compare
        # It will first iterate at first .+ then at the occurance of @
            # Then it will shift to the condition after the @ symbol and then perform the rest of the iterations
            # If it arrives at an accept state(final state), then indeed it was a valid email address
    # Can't use .edu directly (A corner case), can be solved using special sequence \. and telling python that it's a raw string
    # You want the data entries to follow strict email rules
        #if not then when u use them your program will break
    # Can also create the notion of plus using ..*, any char+any char*wholeno=any char 1 to natural numbers
    print("Valid")
else: 
    print("Invalid")
    
    

'''
.
any character except a newline

*
O or more repetitions (no or any number of characters)

+
1 or more repetitions (Atleast one character)

?
0 or 1 repetition (Either no or just a single chaaracter)

{m}
m repetitions (m characters)

{m, n}
m to n repetitions (range of m to n characters)

^
matches the start of the string

$
matches the end of the string or  just before the newline at the end of the string

[ ]
set of characters

[^]
complementing the set

\d
decimal digit 

\D
not a decimal digit 

S
whitespace characters 

1S
not a whitespace character 

\w
word character ... as well as numbers and the underscore

\W
not a word character

A B
either A or B

(...)
a group

(?:...)
non-capturing version

\b


'''