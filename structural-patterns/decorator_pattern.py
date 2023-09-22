from abc import ABC, abstractmethod

# Abstract base class representing the Pizza interface
class Pizza(ABC):

    @abstractmethod
    def getDescription(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# Concrete implementation of the Pizza interface
class ConcretePizza(Pizza):

    def __init__(self) -> None:
        self.description = 'Base Pizza'
        self.priceOfPizza = '£20'

    def getDescription(self):
        print(self.description)

    def cost(self):
        print(self.priceOfPizza)

# Abstract decorator class that inherits from Pizza
class ToppingDecorator(Pizza):

    _pizza: Pizza = None

    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza

    def getDescription(self):
        print('Inside abstract decorator')
        self._pizza.getDescription()

    def cost(self):
        print('Inside abstract decorator')
        self._pizza.cost()

# Concrete decorator class for adding cheese
class CheeseToppingDecorator(ToppingDecorator):

    def __init__(self, pizza: Pizza) -> None:
        super().__init__(pizza)

    def getDescription(self):
        print('Inside cheese topping decorator')
        return super().getDescription()
    
    def cost(self):
        print('Inside cheese topping decorator')
        return super().cost()

if __name__ == '__main__':
    # Create a base pizza object
    basePizza = ConcretePizza()
    
    # Decorate the base pizza with cheese topping
    cheesyPizza = CheeseToppingDecorator(basePizza)
    
    # Get and display the description of the decorated pizza
    cheesyPizza.getDescription()
    
    # Get and display the cost of the decorated pizza
    cheesyPizza.cost()
