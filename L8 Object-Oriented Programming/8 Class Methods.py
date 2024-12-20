import random
# Common for all the objects
# Another decorators  @classmethod
    # No access to self, but will be in the indented black of a class

class Dice:
    number=["one", "two", "three", "four", "five", "six"]
        
    @classmethod
    # A method is by defualt an instant method, untill classmethod is mentioned
    def NUM(cls, name):
        # we write cls as class is a keyword
        print(name, "should play", random.choice(cls.number), "move(s).")
        
#something=Dice()
#something1=Dice()
# We don't need this fucntionality, so we don't use __init__

Dice.NUM("Tabish Shah Mohisn")
