from abc import ABC, abstractmethod

# Abstract Command class
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

# Concrete Command classes
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_on()


    def undo(self):
        self.light.turn_off()

class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.turn_off()


    def undo(self):
        self.light.turn_on()

# Receiver class (the device being controlled)
class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


# Invoker class
class RemoteController:
    def __init__(self):
        self.history = []
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute(self):
        if self.command:
            self.command.execute()
            self.history.append(self.command)

    def undo(self):
        if self.command:
            self.history.pop().undo()


# Client code
if __name__ == "__main__":
    remote = RemoteController()
    light = Light()

    turn_on_command = TurnOnLightCommand(light)
    turn_off_command = TurnOffLightCommand(light)

    remote.set_command(turn_on_command)
    remote.execute()

    remote.set_command(turn_off_command)
    remote.execute()

    remote.undo()
    remote.set_command(turn_off_command)
    remote.execute()
    remote.set_command(turn_off_command)
    remote.execute()
    remote.undo()