

class Singleton:

    #this will hold the single instance of the class
    _uniqueInstance = None

    #when creating a new instance of a class, called before __init__
    def __new__(cls, *args, **kwargs):
        #cannot write this inside __init__ as __new__ is called before __init__
        if not cls._uniqueInstance:
            print('I have no instance')
        else:
            print('I have an instance')

        if cls._uniqueInstance is None:
            #as ive overwritten the __new__ in this class, we call pythons base class object using
            #super() then we have the __new__(cls) to create the class!
            cls._uniqueInstance = super().__new__(cls)
        return cls._uniqueInstance


class Singleton_lazy:

    _uniqueInstance = None

    def __init__(self) -> None:
        if not Singleton_lazy._uniqueInstance:
            print('i have no instance')
        else:
            print('i have an instance')

    #here we access the actual class itself, not the instanciated object properties
    @classmethod
    def newInstance(cls):
        if (cls._uniqueInstance == None):
            cls._uniqueInstance = super().__new__(cls)

        return cls._uniqueInstance
        
    
class test(Singleton):

    def __init__(self):
        print('hello')

        

if __name__ == '__main__':

    s1 = Singleton()
    s2 = Singleton()

    sl1 = Singleton_lazy().newInstance()
    sl2 = Singleton_lazy().newInstance()

    
    if id(sl1) == id(sl2):
        print('singleton lazy works')
    else: 
        print('singleton lazy doesnt work')

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")