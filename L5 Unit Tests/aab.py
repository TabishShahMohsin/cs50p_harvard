from aaa import square
def main():
    test_square()
def test_square():
    d={1:1, 2:4, 3:9, 4:16, 5:25}
    for t in d:
        if square(t)!=d[t]:
            print("ERROR!! square(", t, ") is not", d[t])
        # or assert sqaure(t)==d[t]
if __name__ == "__main__":
    main()