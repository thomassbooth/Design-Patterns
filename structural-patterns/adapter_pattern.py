
from abc import ABC, abstractmethod

class Target:

    'this is our og code, domain specific interface used by the client'

    def request(self):
        return 'default targets behaviour'
    

class Adaptee:

    '''New behaviour thts being introduced, it is incompatible with the existing client code, 
    we need to adapt this before the client code can use it as its expecting target '''

    def specific_request(self):
         return ".eetpadA eht fo roivaheb laicepS"


class AdapteeAdapter(Adaptee):
    'Makes the adaptees interface compatible with the tagets interface via multiple inheritance'

    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")



if __name__ == '__main__':
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = AdapteeAdapter()
    client_code(adapter)