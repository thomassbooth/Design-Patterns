from abc import ABC, abstractmethod


#we have our observers, these must all have this base class (there can be multiple observers)
class Observer(ABC):

    @abstractmethod
    def update(self, state):
        pass

#this is a concrete observer
class StatisticsDisplay(Observer):
    
    def update(self, state):
        print(f'current stats{state}')

#another concrete observer
class HumidityDisplay(Observer):

    def update(self, state):
        print(f'humidity is displaying: {state.get("humidity")}')


#basic functionality our subjects should have
class Subject():

    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def register(self, observer: Observer):
        self.observers.append(observer)

    def unregister(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, state):
        for observer in self.observers:
            observer.update(state)


class Weather(Subject):

    def __init__(self, location, time, temperature, humidity):
        super().__init__()
        self.location = location
        self.time = time
        self.temperature = temperature
        self.humidity = humidity

    #current state of the system
    def get_state(self):
        return {
            'location': self.location,
            'time': self.time,
            'temperature': self.temperature,
            'humidity': self.humidity
        }
    
    #update the state and notify anything subscribed
    def set_state(self, location, time, temperature, humidity):
        self.location = location
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.notify({
            'location': self.location,
            'time': self.time,
            'temperature': self.temperature,
            'humidity': self.humidity
        })
    



if "__main__" == __name__:
    dubai = Weather('dubai', '10pm', '50deg', '80%')

    dubai_statsDisplay = StatisticsDisplay()
    dubai_humidityDisplay = HumidityDisplay()
    dubai.register(dubai_humidityDisplay)
    dubai.register(dubai_statsDisplay)

    dubai.set_state('dubai', '11pm', '51deg', '82%')
    dubai.set_state('dubai', '12pm', '54deg', '90%')
    dubai.set_state('dubai', '1am', '48deg', '80%')
    