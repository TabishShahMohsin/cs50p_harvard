# You can change meaning of operators
    # Can change the meaning of + and -
    # Like we already use + for catenation
class Vault:
    def __init__(self, gold=0, silver=0, bronze=0):
        self.gold=gold
        self.silver=silver
        self.bronze=bronze
        
    def __str__(self):
        return f"{self.gold} gold, {self.silver} silver and {self.bronze} bronze coins."
    
    def __add__(self, other):
        # However other may be of any type but not here as other.silver.. are used
        return Vault(self.gold+other.gold, self.silver+other.silver, self.bronze+other.bronze)
        
        
    # You can get their sum into a new object or use this to get it directly always
    # docs.python.org/3/reference/datamodel.html#special-method-names
    # object.__add__(self, other)
        
Tabish=Vault(50,60,70)
Aarish=Vault(60,50,100)

family=Tabish+Aarish

print(family)