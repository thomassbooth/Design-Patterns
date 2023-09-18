#basicly groups up a set of classes that requires usage of multiple classes to perform certain actions
#to hide the complexity of those actions


#we create a facade class to hide the complexity of an underlying subsystem
#behind a simple interface, its a trade off between functionality and simplicity
#also ecapsulating it.
class BookCatalog:

    books = set()

    def add_book(self, book):
        self.books.add(book)

    def get_book_details(self, book):
        # Implement book retrieval logic
        pass

    def remove_book(self, book):
        self.books.remove(book)


class MemberManagement:

    def new_member(self, member):
        # Implement member creation logic
        pass

    def update_member(self, member):
        # Implement member update logic
        pass
    
    def check_member_status(self, member):
        # Implement member status checking logic
        pass


class LoanProcessing:

    def new_loan(self, book, member):
        # Implement loan creation logic
        print(f'New loan has been created for {book} by {member}')
        
    def clear_loan(self, book, member):
        # Implement loan clearing logic
        pass
    

#to carry out some options it hides the complexity of each of the subsystems behind this facade!
class LibraryFacade:

    def __init__(self):
        self.loanProcessor = LoanProcessing()
        self.memberManager = MemberManagement()
        self.bookCatalog = BookCatalog()

    def borrow_book(self, book, member):
        self.loanProcessor.new_loan(book, member)
        self.bookCatalog.remove_book(book)


if __name__ == '__main__':
    library = LibraryFacade()
    book = 'The Great Gatsby'
    member = 'John Doe'
    library.borrow_book(book, member)
