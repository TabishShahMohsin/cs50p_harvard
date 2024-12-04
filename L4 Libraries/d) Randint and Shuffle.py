import random
print(random.randint(1,10))
l=["Tabish", "Fahad", "Jibraan", "Talha", "Danish"]
#Return random integer in range [a, b], including both end points.
#Can be used in a game for obstacles or spawning random things
#Eg: to shuffle a deck of cards
#It's DOCUMENTATION tells us that it returns none, but shuffles the list passed to it.
random.shuffle(l)
#can also get the same order
for name in l:
    print(name)