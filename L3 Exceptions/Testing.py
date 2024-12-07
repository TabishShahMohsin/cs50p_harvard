import random
d={"Head":0, "Tails":0}
l=["T", "H"]
for i in range(1000000):
    if random.choice(l)=="T":
        d["Tails"]=d["Tails"]+1
    else:
        d["Head"]=d["Head"]+1
print(d)