class Librarian:
    def __init__(self, book_list: list):
        self.booklist = book_list

    def addB(self, book):
        self.booklist.append(book)
    def removeB(self, book):
        self.booklist.remove(book)
    def display(self):
        print(self.booklist)

class User:
    def __init__(self, name: str):
        self.name = name
        self.booksBorrowed = []

    def borrowBook(self, book: str, booklist: list):
        if booklist.count(book):
            self.booksBorrowed.append(book)
            booklist.remove(book)
        else:
            print("We don't have a book with that name, sorry")
    
    def returnBook(self, book: str, booklist: list):
        if self.booksBorrowed.count(book):
            self.booksBorrowed.remove(book)
            booklist.append(book)
        else:
            print("Thank you for returning the book")
            booklist.append
