with open("Sorted.txt") as something:
    for line in sorted(something):
        print(f"Hello, {line.rstrip()} ")
#sorted(iterable, /, *, key=None, reverse=False)