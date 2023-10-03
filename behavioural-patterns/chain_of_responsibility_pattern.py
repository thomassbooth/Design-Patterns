from abc import ABC, abstractmethod

class Handler(ABC): 
    
    @abstractmethod
    def set_next(self): 
        pass

    @abstractmethod
    def process_request(self):
        pass
    


class AbstractHandler(Handler):

    _next_handler: Handler = None

    #setup next in the chain
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        return handler


    @abstractmethod
    def process_request(self, request) -> str:
        #define our next handler for each
        if self._next_handler:
            return self._next_handler.process_request(request)

        return None


class Manager(AbstractHandler):

    def process_request(self, request) -> str:
        print('inside manager')
        if request < 10:
            return f"MANAGER: I have processed {request}"
        else:
            return super().process_request(request)

class Director(AbstractHandler):

    def process_request(self, request) -> str:
        if request < 100:
            return f"DIRECTOR: I have processed {request}"
        else:
            return super().process_request(request)

class VP(AbstractHandler):

    def process_request(self, request) -> str:
        if request < 200:
            return f"VP: I have processed {request}"
        else:
            return super().process_request(request)

class CEO(AbstractHandler):

    def process_request(self, request) -> str:
        if request < 1000:
            return f"CEO: I have processed {request}"
        else:
            #call the next one up in the chain
            return super().process_request(request)


def client_code(handler):

    for money in [20, 99, 201, 301, 1001]:
        print(f"\nClient: Who wants a {money}?")
        result = handler.process_request(money)
        if result:
            print(f"{result}")
        else:
            print(f"{money} was left untouched.", end="")


if __name__ == '__main__' :
    manager = Manager()
    director = Director()
    vp = VP()
    ceo = CEO()

    manager.set_next(director).set_next(vp).set_next(ceo)

    client_code(manager)

