from abc import ABC, abstractmethod


class ChatMediator(ABC):

    @abstractmethod
    def send_message(self):
        pass

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def remove_user(self):
        pass


class Colleague(ABC):

    @abstractmethod
    def send(self, message):
        pass


class ConcreteChatMediator(ChatMediator):

    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, message, user):
        for u in self.users:
            if u != user:
                u.receive(message)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)


class User(Colleague):

    def __init__(self, mediator, name):
        self.mediator = mediator
        self.name = name

    def send(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message):
        print(f"{self.name} receives: {message}")


if __name__ == "__main__":
    mediator = ConcreteChatMediator()
    user1 = User(mediator, "User1")
    user2 = User(mediator, "User2")

    mediator.add_user(user1)
    mediator.add_user(user2)

    user1.send("Hello, User2!")
    user2.send("Hi, User1!")

    mediator.remove_user(user1)

    user2.send("Are you there, User1?")  # User1 has been removed from the chat.