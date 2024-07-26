from book import Book
from user import User
from author import Author
from genre import Genre

user= User()
book= Book()
author = Author()
genre = Genre()
def opening_menu():
    pass

def book_operations():
    try:
        print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
        option = int(input("Please pick an option to continue: "))             
        if option == 1:
            title = input("What is the title: ").title()
            author_name = input('Enter authors name: ').title()
            bio= input('Enter short biography of the author: ')
            author.add_author(author_name, bio)
            #author = input("Who is the author? ").title()
            ISBN = int(input("What is the ISBN? "))
            genre_input = input("What is the genre? ").title()
            description= input("Describe this genre: ")
            genre.add_genre(genre_input, description)
            publication_date = input("What is the publication date?(DD/MM/YYYY) ")
            book.add_book(title, author_name, ISBN, genre, publication_date)
        elif option == 2:
            ISBN = int(input("Please enter the ISBN of the book you would like to borrow: "))
            library_ID = input("Please submit your login: ")                
            user.borrow_book(library_ID, book.borrow_book(ISBN))
        elif option == 3:
            library_ID= input("Please enter your library ID to return the book: ")
            ISBN = int(input("Please enter the ISBN of the book you would like to return: "))
            user.return_book(library_ID, book.return_book(ISBN))
        elif option == 4:
            
            book.search_book(ISBN=int(input("Please enter the ISBN of the book you are looking for: ")))
        elif option == 5:
            book.display_books()
        else:
            raise ValueError("Invalid option. (1-5)")
    except Exception as e:
        print(e)

def user_operations():
    try:
        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            library_ID= input("Please enter your new library ID: ")
            name = input("Please enter your name: ")
            user.add_user(library_ID, name)
        elif option == 2:
            library_ID = input("Please enter your library ID to get user information: ")
            user.user_info(library_ID)
        elif option == 3:
            user.display_users()
        else:
            raise ValueError("Invalid option. (1-3)")
    except Exception as e:
        print(e)

def author_operations():
    
    try:
        print("\nAuthor Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            new_author=input("Enter author name: ").title()
            biography=input("Enter short author biography: ")
            author.add_author(new_author, biography)    
        elif option == 2:
            author_name = input('Which author are you looking for? ').title()
            author.search_author(author_name)
        elif option == 3:
            author.display_authors()
        else:
            raise ValueError("Invalid option. (1-3)")  
    
    except Exception as e:
        print(e)

def genre_operations():
    try:
        print("\nGenre Operations\n1. Add a new genre\n2. View genre details\n3. Display all genres\n")
        option = int(input("Please pick an option to continue: "))
        if option == 1:
            new_genre=input("Enter genre: ").title()
            description=input("Enter short genre description: ")
            genre.add_genre(new_genre, description)    
        elif option == 2:
            user_genre = input('Which genre are you looking for? ').title()
            genre.search_genre(user_genre)
        elif option == 3:
            genre.display_genres()
        else:
            raise ValueError("Invalid option. (1-3)")  
    
    except Exception as e:
        print(e)