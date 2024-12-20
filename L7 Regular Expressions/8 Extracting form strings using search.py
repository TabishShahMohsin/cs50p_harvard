import re
url=input("Enter URL: ")
# To make twitter.com mandatory
# google.com should not accepted as an input
if matches:=re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
    
'''
Can try:
re. split(pattern, string, maxsplit=0, flags=0): used to split a string
re. findall(pattern, string, flags=0): to find multiple copies of a string



'''