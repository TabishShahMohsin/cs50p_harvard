import re

name=input("Enter your name: ").strip()


if matches:=re.search(r"^(.+), *(.+)$", name):
    # It returns boolean and assigns as well

    name=matches.group(2)+" "+ matches.group(1)

print(f"Hello, {name}")
    