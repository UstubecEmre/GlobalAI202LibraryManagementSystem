#%% Create a book class (Kitap Sınıfının Oluşturulması)
class Book:
    # static attibutes (class attributes)
    count_book = 0
    
    def __init__(self, ISBN, title, author):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"The ISBN number of this book is {self.ISBN}. The title of this book is{self.title} and the author of the book is also {self.author}"
    
    


