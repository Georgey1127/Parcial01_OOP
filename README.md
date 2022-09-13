# Parcial 01 OOP

In this repository I will be explaining and showing my exam.

App: Library Managment System
* The user can do many things in the Library Management system. The user can borrow a book, return a book and display available books. The Librarian should be able to upload a list of books and modify such list if a book is lost or damaged. You should be able to browse all the available collections or find a book by searching (you only need to think in exact string matching, not approximate)

This is the app I chose to code for the Exam


PlantUML
-

![image](https://user-images.githubusercontent.com/110436992/189922993-92332437-408f-472d-be0f-ab86f9e124b5.png)


Explanation: The class User is created and has an attribute called "name" which is a type string this will function to now the name of the user. The methods of this class User are "borrowBook" and "returnBook" that will help with the functionality of the app when the User trys to return or borrow a book form the Librarian. The Librarian is another class and has an attribute called "book_list" and is a type list which will have the list of books available. The methods of this class Librarian are "addB" and "removeB" which will let the Class Librarian add or remove a book from the list of books.

