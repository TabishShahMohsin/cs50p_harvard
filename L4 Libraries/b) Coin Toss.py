import random
l=["Heads", "Tails"]
#This is a list of strings
coin=random.choice(l)
#This returns the elements with equal probabilities
print(coin)
#If we did it infinity times, we would get it to be 50-50.

# Proof of concept that on large scale random will apporximate probabilities
g=10000000
h=0
for i in range(g):
    coin=random.choice(l)
    if coin=="Heads":
        h+=1
print(f"h: {h/g}, t: {(g-h)/g}")