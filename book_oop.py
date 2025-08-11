#%% 1. Create a book class (Kitap Sınıfının Oluşturulması)
class Book:
    # static attibutes (class attributes)
    count_book = 0
    
    def __init__(self, ISBN, title, author):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        
        # increase count_book
        Book.count_book += 1
        
    def __str__(self):
        return f"The ISBN number of this book is {self.ISBN}. The title of this book is: {self.title} and the author of the book is also {self.author}"
        #return f"{self.title} by {self.author} (ISBN: {self.ISBN})"
# %% call the function
first_book = Book(ISBN = "9789754589023", title = "Suç ve Ceza", author= "Fyodor Dostoyevski")

print(first_book.__str__())
print(f"Title of First Book: {first_book.title}")
print(f"Author of First Book: {first_book.author}")
print(f"ISBN Number of First Book: {first_book.ISBN}")

print("total number of objects created: ",first_book.count_book)



 
#%% 2. Create a Library Class
class Library():
    def __init__(self,book_lists = None, file_name = "library.json"):
        # check the book_lists (None olup olmadığını kontrol edelim. None ise boş liste döndürsün)
        self.book_lists = book_lists if self.book_lists is not None else []
        self.file_name = file_name
        
    def add_book(self, book):
        pass

    def remove_book(self, ISBN):
        pass
    
    def list_books(self):
        pass
    
    def find_book(self, ISBN):
        pass
    
    def load_books(self):
        pass
    
    def save_books(self):
        pass 