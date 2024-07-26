class Genre:
    def __init__(self):
        self.genre_list={}

    def add_genre(self, genre, description):
        if genre not in self.genre_list:
            self.genre_list[genre]={'Description': description}
            print('Genre added.')
        else: 
            print(f'Genre, {genre}, already exists.')

    def search_genre(self, genre):
        genre_search = 'not found'
        for genres, description in self.genre_list.items():
            if genres == genre:
                genre_search = 'found'
                print(f'Genre: {genre}')
                for key, value in description.items():
                    print(f'\t{key}: {value}')               

        if genre_search == 'not found':
            print('Genre not found.')

    def display_genres(self):
        print(self.genre_list)