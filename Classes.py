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
        self.Borrowedbooks = []

    def borrowBook(self, book: str, booklist: list):
        if booklist.count(book):
            self.Borrowedbooks.append(book)
            booklist.remove(book)
        else:
            print("We don't have a book with that name, sorry")
    
    def returnBook(self, book: str, booklist: list):
        if self.Borrowedbooks.count(book):
            self.Borrowedbooks.remove(book)
            booklist.append(book)
        else:
            print("Thank you for returning the book")
            booklist.append
