import random
print(random.randint(1,10))
#Return random integer in range [a, b), equivalen to choice(range(a,b))
#Can be used in a game for obstacles or spawning random things



l=["Tabish", "Fahad", "Jibraan", "Talha", "Danish"]
something=random.shuffle(l)
#Eg: to shuffle a deck of cards
print(something)
#It's DOCUMENTATION tells us that it returns none, but shuffles the list passed to it.
    # Like most of the functions relating to mutable data-types, like sort(), etc.
for name in l:
    print(name)
    
#can also get the same order
# To prove that you can get the same list
l=[1,2]
original=l.copy()
while True:
    random.shuffle(l)
    print(l)
    if l==original:
        break