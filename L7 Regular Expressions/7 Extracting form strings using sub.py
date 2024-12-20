# Eg: using twitter url links to find the username
# can use .replace() or .removeprefix() with strings to pop out the rest but still not the best way

import re

URL=input("Enter the URL: ")


username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", URL)
# re. sub(pattern, repl, string, count=0, flags=0)
# Substitute

print(f"Username: {username}")

