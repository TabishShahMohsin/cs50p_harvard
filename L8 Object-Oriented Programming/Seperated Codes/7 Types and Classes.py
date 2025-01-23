'''https://docs.python.org/3/library/functions.html#int
actually int is a class
    Constructor call for int: class int(x, base=10)
    
similarly for other things:
    class str(object='') : returns an object of type str
        str.lower uses str an object of type str and uses a method lower to convert all in lowercase
        even .strip is a method

    Acutally even errors are made up of classes
    
    lists:
        https://docs.python.org/3/tutorial/datastructures.html
        a method called append
        
        
    dict:
        That's why we manier times call dict as objects
        docs.python.org/3/library/stdtypes.html#dict
    '''
print(type(ValueError),type(AssertionError), type(50), type("tabsih"), type([1,2,3]), type({1:2,3:4}), type({1,2,3,4}))
