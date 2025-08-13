#%% Create a library class with its methods
#%% 2. Create a Library Class

# load required libraries (Gerekli kütüphaneleri import et)
from book_oop import Book
import json 
import os 

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
        if os.path.exists(self.file_name):
                with open(self.file_name, mode= "r", encoding= "utf-8") as file:
                    data = json.load(file)
                    # self._book_lists = [Book(**book_data) for book_data in data]    
                
                # Create a null list, and add new book objects
                self._book_lists = []
                
                
                for book_data in data:
                    book_obj = Book(**book_data) # convert json format
                    self._book_lists.append(book_obj)
        else:
            # return null list (Boş liste döndür)
            self._book_lists = []               
    
    def save_books(self):
        pass 