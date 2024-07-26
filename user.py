class User: 
    def __init__(self):
        self.user_list={}

    def add_user(self, library_ID, name):
        if library_ID not in self.user_list:
            self.user_list[library_ID] = {'Name': name.title(), 'Borrowed Books': []}
        else:
            print("User already exists.")
    
    def borrow_book(self, library_ID, book_title):
        self.user_list[library_ID]['Borrowed Books'].append(book_title)

    def return_book(self, library_ID, book_title):
        self.user_list[library_ID]['Borrowed Books'].remove(book_title)

    
    def user_info(self, library_ID):
        if library_ID in self.user_list:
            print(f"User information:\n\tLibrary ID: {library_ID}\n\tName: {self.user_list[library_ID]['Name']}\n\tBorrowed Books: {self.user_list[library_ID]['Borrowed Books']}")
        else:
            print("User not found.")
    def display_users(self):
        for library_ID, account_details in self.user_list.items():
            print (f"User: {library_ID}")
            for name, details in account_details.items():
                print(f"\t{name}: {details}")