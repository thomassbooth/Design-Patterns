from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, gender, hp, name):
        self.gender = gender
        self.hp = hp
        self.name = name

    def get_gender(self):
        print(self.gender)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    @abstractmethod
    def get_battlecry(self):
        pass


class MaleMage(Character):

    def get_battlecry(self):
        print('GRRRRR male')
    

class FemaleMage(Character):

    def get_battlecry(self):
        print('grrr female')


class CharacterFactory(ABC):

    @abstractmethod
    def create_male(self):
        pass

    @abstractmethod
    def create_female(self):
        pass


class MageFactory(CharacterFactory):

    def create_male(self, name):
        return MaleMage('male', 50, name)
    
    def create_female(self, name):
        return FemaleMage('female', 40, name)
    



if __name__ == '__main__':

    mage_factory = MageFactory()

    male = mage_factory.create_male('tom')
    female = mage_factory.create_female('nuni')

    print(male.get_battlecry())
    print(male.get_name())
    print(female.get_battlecry())
    print(female.get_name())