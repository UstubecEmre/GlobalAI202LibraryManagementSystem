#%% Create a library class with its methods
#%% 2. Create a Library Class


from book_oop import Book

class Library():
    def __init__(self):
        self._book_lists = []
        
    def add_book(self, book: Book):
        self._book_lists.append(book)

    def remove_book(self, ISBN):
        pass
    
    def list_books(self):
        pass
    
    def find_book(self, ISBN):
        for book in self._book_lists:
            if book.ISBN == ISBN:
                return book
        return None
                
    
    def load_books(self):
        pass
    
    def save_books(self):
        pass 