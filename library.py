#%% Create a library class with its methods
#%% 2. Create a Library Class


from book_oop import Book

class Library():
    def __init__(self, file_name = "library.json"):
        self._book_lists = []
        self.file_name = file_name
        
    def add_book(self, book: Book):
        self._book_lists.append(book)

    def remove_book(self, ISBN):
        for book in self._book_lists:
            if book.ISBN == ISBN:
                self._book_lists.remove(book)
                return True 
        return False 
    
    def list_books(self):
        for book in self._book_lists:
            print(book)
            
    
    def find_book(self, ISBN):
        for book in self._book_lists:
            if book.ISBN == ISBN:
                return book
        return None
                
    
    def load_books(self):
        pass
    
    def save_books(self):
        pass 