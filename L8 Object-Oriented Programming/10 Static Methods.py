# You can desing classes in an hierarchy
    # With classes borrowing(inherriting) attributes from other classes
    # Good for dealing with data redundancy
    # can use same attributes for professors and students hence don't need to repeat them
class Humans:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name")
        self.name=name
        
class Students(Humans):
    # Telling that Students is a subclass of Humans
    def __init__(self, name, house):
        super().__init__(name)
        self.house=house
        
        
class Professor(Humans):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject=subject
        
        
# It turns out the even the exceptions are nothing but subclasses
# docs.python.org/3/library/exceptions.html


'''
Type of Method  Uses self?	Uses cls?	When to Use
Instance Method	Yes	        No	        When you need to access or modify an instance’s data.
Class Method	No	        Yes	        When you need to access or modify class-level data or create new instances.
Static Method	No	        No	        When you don’t need access to instance or class-level data; acts as a standalone utility.

'''
'''

BaseException
+-- KeyboardInterrupt
+-- Exception
    +-- ArithmeticError
        +-- ZeroDivisionError
    +-- AssertionError +-- AttributeError
    +-- EOFError
    +-- ImportError
        +-- ModuleNotFoundError
    +-- LookupError
        +-- KeyError
    +--
    NameError
    +-- SyntaxError
        +-- IndentationError
    +--
    ValueError
    
    hence even if you want to create your own exception, then create it using this hierarchy

'''
        