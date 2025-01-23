class Cat:
    # Again a honor based system: for class variables
    MEOWS=5

    def meow(self):
        for _ in range(self.MEOWS): print("Meow")

cat=Cat()

cat.meow()
