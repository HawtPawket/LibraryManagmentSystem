class Book:
    def __init__ (self):
        
        self.library={}

    def add_book(self, title, author, ISBN, genre, publication_date):
        if ISBN not in self.library:
            self.library[ISBN]={}
            self.library[ISBN]['Title']=title
            self.library[ISBN]['Author']=author
            self.library[ISBN]['Genre']=genre
            self.library[ISBN]['Publication Date']=publication_date
            self.library[ISBN]['Availability']= 'Available'
        else:
            print("Book already exists.")
    
    def borrow_book(self, ISBN):
        if self.library[ISBN]['Availability'] == 'Available':
            print("Book has been borrowed")
            self.library[ISBN]['Availability'] = 'Borrowed'
            return self.library[ISBN]['Title']
        else: 
            print("Book is not available.")
    def return_book(self, ISBN):
        if self.library[ISBN]['Availability'] == 'Available':
            print("Book was not borrowed")
        else:
            self.library[ISBN]['Availability']= 'Available'
            return self.library[ISBN]['Title']
    def search_book(self, ISBN):
        if ISBN in self.library:
            print(f"{ISBN}:")
            for label, info in self.library[ISBN].items():
                print(f"\t{label}: {info}")
        else:
            print("Book not found.")
    def display_books(self):
        if self.library:
            for ISBN, information in self.library.items():
                print(f"ISBN {ISBN}: ")
                for label, info in information.items():
                    print(f"\t{label}: {info}")
        else:
            print("No books found.")

