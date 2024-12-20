import re
# What if there is a common mistake in the data
# We can automate its correction
# Like asking for name, Americans: Shah, Tabish
name=input("Enter your name: ")
matches=re.search(r'^(.+), *(.+)$', name)
# What ever is in the () will get returned as return value
if matches:
    last, first=matches.groups()
    name=first+" "+last
    # Can shorted the above 2 lines by using name=mathes.group(2)+" "+matches.group(1)
    # groups(0) has already something in it

print(f"Hello, {name}")