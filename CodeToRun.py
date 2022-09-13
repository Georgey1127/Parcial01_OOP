from Classes import Librarian, User

library = Librarian(["Alex Rider: Stormbreaker","Alex Rider 2: Point Blanc", "Harry Potter and the Sorcerer's Stone"])
Alejandra = User('Alejandra')

print("Hi im Alejandra and I want to borrow a book. What books do yo have available?")
library.display()
Alejandra.borrowBook("Alex Rider 2: Point Blanc", library.booklist)
library.display()

print("A new book has been added to the collection")
library.addB("Cien años de soledad")
library.display()

print("A book has been damaged we will need to remove it")
library.removeB("Harry Potter and the Sorcerer's Stone")
library.display()

Alejandra.returnBook("Alex Rider 2: Point Blanc", library.booklist)
library.display()
