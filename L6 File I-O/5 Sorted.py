names=[]

with open("Sorted.txt") as something:
    #by defualt it opens in reading mode
    for line in something:
        names.append(line.rstrip())
        # rsrtip removes the new line char

for name in sorted(names):
    print(f"Hello, {name}")
# This is a common practice if, short of something, store them and then perform the operations that you desire