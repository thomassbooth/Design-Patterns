from abc import ABC, abstractmethod

#common interface that all animals will implement
class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

#Our concrete animal classes that implement our Animal interface
class Tiger(Animal):

    def speak(self):
        print('TIGER RAWR')

#Our concrete animal classes that implement our Animal interface
class Bear(Animal):

    def speak(self):
        print('BEAR GRRRR')

#Abstract factory 
class AnimalFactory(ABC):

    @abstractmethod
    def create_animal(self):
        pass

#concrete abstract factory
class TigerFactory(AnimalFactory):

    def create_animal(self):
        return Tiger()
    
#concrete abstract factory
class BearFactory(AnimalFactory):

    def create_animal(self):
        return Bear()


if __name__ == '__main__':
    bear_factory = BearFactory()
    tiger_factory = TigerFactory()

    bear = bear_factory.create_animal()
    tiger = tiger_factory.create_animal()

    print(bear.speak())  # Output: Roar!
    print(tiger.speak())  # Output: Growl!