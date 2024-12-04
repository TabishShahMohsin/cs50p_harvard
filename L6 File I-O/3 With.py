# More pythonic version is with
# Don't need to close
# Prevents currupted files
name=input("Enter name: ")
with open("With.txt", "w") as Something:
    Something.write(f"Hello, {name}\n")
    # After this indent is executed, the file is saved