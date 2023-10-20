from abc import ABC, abstractmethod


class ChatMediator(ABC):

    @abstractmethod
    def sendMessage(self):
        pass

    @abstractmethod
    def addUser(self):
        pass

    @abstractmethod
    def removeUser(self):
        pass


if __name__ == "__main__":
