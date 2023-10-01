# An example for making two coffees
from abc import ABC, abstractmethod

# Define an abstract base class (CoffeeTemplate) with a template method and abstract methods
class CoffeeTemplate(ABC):

    # The template method outlining the coffee-making algorithm
    def prepare_coffee(self):
        self.boil_water()
        self.brew_coffee_grounds()
        self.pour_in_cup()
        self.add_condiments()

    # Abstract method for boiling water (to be overridden by subclasses)
    @abstractmethod
    def boil_water(self):
        pass

    # Abstract method for brewing coffee grounds (to be overridden by subclasses)
    @abstractmethod
    def brew_coffee_grounds(self):
        pass

    # Abstract method for pouring coffee into a cup (to be overridden by subclasses)
    @abstractmethod
    def pour_in_cup(self):
        pass

    # Abstract method for adding condiments (to be overridden by subclasses)
    @abstractmethod
    def add_condiments(self):
        pass

# Concrete subclass for Espresso coffee
class EspressoCoffee(CoffeeTemplate):

    # Implementation of boiling water for Espresso
    def boil_water(self):
        print("Boiling small amount of water for espresso")

    # Implementation of brewing coffee grounds for Espresso
    def brew_coffee_grounds(self):
        print("Brewing... espresso...")

    # Implementation of pouring Espresso into a cup
    def pour_in_cup(self):
        print("Pouring into a tiny espresso cup...")

    # Implementation of adding condiments for Espresso
    def add_condiments(self):
        print("Adding some sweeteners...")

# Concrete subclass for Latte coffee
class LatteCoffee(CoffeeTemplate):

    # Implementation of boiling water for Latte
    def boil_water(self):
        print("Boiling a large amount of water for Latte")

    # Implementation of brewing coffee grounds for Latte
    def brew_coffee_grounds(self):
        print("Brewing... Latte... Beans...")

    # Implementation of pouring Latte into a cup
    def pour_in_cup(self):
        print("Pouring into a large coffee cup...")

    # Implementation of adding condiments for Latte
    def add_condiments(self):
        print("Adding some sweeteners... Adding some milk...")

# Main program
if __name__ == "__main__":
    # Create instances of the coffee types
    Latte = LatteCoffee()
    Espresso = EspressoCoffee()

    # Make Latte and Espresso using the template method
    Latte.prepare_coffee()
    Espresso.prepare_coffee()
