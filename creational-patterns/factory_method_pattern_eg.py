from abc import ABC, abstractmethod


'''Problem Scenario: Online Game Character Creation'''

#interface class
class Character(ABC):

    def __init__(self, hp, attackdmg):
        self.hp = hp
        self.attackdmg = attackdmg
        
    @abstractmethod
    def attack(self):
        pass

    def heal(self):
        print(f"{self.__class__.__name__} healed for {self.hp} HP.")

#concrete class
class Warrior(Character):

    def attack(self):
        print(self.attackdmg)

#concrete class
class Mage(Character):

    def attack(self):
        print(self.attackdmg)

#abstract factory
class CharacterFactory(ABC):

    @abstractmethod
    def create_character(self):
        pass

    @abstractmethod
    def name_character(self):
        pass

#concrete factory
class WarriorFactory(CharacterFactory):

    def create_character(self):
        return Warrior(30, 45)
    
    def name_character(self, name):
        self.name = name

#concrete factory
class MageFactory(CharacterFactory):

    def create_character(self):
        return Mage(20, 10)
    
    def name_character(self, name):
        self.name = name
    

if __name__ == '__main__':
    
    mage_factory = MageFactory()
    warrior_Factory = WarriorFactory()

    warr1 = warrior_Factory.create_character()
    mage1 = mage_factory.create_character()

    warr1.attack()
    mage1.attack()