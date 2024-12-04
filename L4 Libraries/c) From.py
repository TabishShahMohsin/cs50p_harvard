#when we use import we import every-single funciton that is in that module
#using from will import the only-used function.
#if import: must write random.choice(seq)
#if from:   onlly write choice(seq)
#you would choose the prev approach it u were using function with these names
#this approach could tighten the code a little bit
from random import choice
#it loads into the local namespace(local vocabulary)
L=["Heads", "Tails"]
print(choice(L))