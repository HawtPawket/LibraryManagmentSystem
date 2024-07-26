class Author:
    def __init__(self):
        self.author_list={}

    def add_author(self, name, bio):
        if name not in self.author_list:
            self.author_list[name]={'Biography': bio}
            print('Author added.')
        else: 
            print(f'Author, {name}, already exists.')

    def search_author(self, name):
        author_search = 'not found'
        for author, description in self.author_list.items():
            if author == name:
                author_search = 'found'
                print(f'Author: {name}')
                for key, value in description.items():
                    print(f'\t{key}: {value}')               

        if author_search == 'not found':
            print('Author not found.')

    def display_authors(self):
        print(self.author_list)
        
