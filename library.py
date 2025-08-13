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
        self.load_books()
        
    def add_book(self, book: Book):
        self._book_lists.append(book)

    def remove_book(self, ISBN):
        for book in self._book_lists:
            if book.ISBN == ISBN:
                self._book_lists.remove(book)
                return True 
        return False 
    
        # or
        """ 
        O(n) Solving : Burada silinip silinmediğini boyut üzerinden anlar. 
        original_len = len(self._book_lists)
        self._book_lists = [book for book in self._books_lists if book.ISBN != ISBN]
        return len(self._book_lists) < original_len 
        """
    
    def list_books(self):
        if not self._book_lists:
            print("❌ There are no books in the library yet. (Henüz Kitap Yok)")
        else:
            for book in self._book_lists:
                print(f"{book.__str__()}")
            
    
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
        
        with open(self.file_name, "w", encoding= "utf-8") as file:
             #dump() => Convert the Python object to JSON format and write it to a file (Python objesini JSON formatına çevirip dosyaya yazar) 
             # dumps() => returns only a string )(Sadece string döndürür)
                        
            # Use list comp to convert to dictionary structure (Liste üreteçleri kullanarak kitap özelliklerini sözlük yapısına dönüştürelim)
            json.dump([book.__dict__ for book in self._book_lists], file, ensure_ascii=False, indent=4)
                
                