class Students:
    def __init__(self, age, gender):
        self.age=age
        self.gender=gender
    
    @property
    def gender(self):
        print("Property was used(getter)")
        return self._gender
    
    @gender.setter
    def gender(self, gender):
        print("setter was used")
        if gender not in ["M","W"]:
            raise ValueError("Should enter M or W as gender.")
        self._gender=gender
    
    def __str__(self):
        return f"A {self.gender} of {self.age}"
    
t=Students(12,"M")
print(t.age,t._gender, t.gender)