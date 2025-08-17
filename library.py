#%% Create a library class with its methods
#%% 2. Create a Library Class

# load required libraries (Gerekli kütüphaneleri import et)
from book_oop import Book
import json 
import os 
import httpx 


OPEN_LIBRARY_URL = "https://openlibrary.org/isbn/"


class Library():
    def __init__(self, file_name = "library.json"):
        self.file_name = file_name
        self._book_lists = []
        self.load_books()
        
    # add book 
    def add_book(self, ISBN):
        # api_url = f"{OPEN_LIBRARY_URL}{ISBN}.json" => get an error 302 status code
        
        # replace "-" to ""
        clean_ISBN = ISBN.replace("-","")
        # use correct Endpoint
        api_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{clean_ISBN}&format=json&jscmd=data"

        try:
            #print(f"An API call is being made. (API Cagrisi Yapiliyor) {api_url}")
            response = httpx.get(api_url)

            # raise for status 4xx or 5xx (Status code için hata fırlat)
            response.raise_for_status()
            
            # convert to python dict 
            book_data = response.json()
            
            # use GET and get book_info by ISBN
            book_info = book_data.get(f"ISBN:{clean_ISBN}", {})
            # for debug
           # print(f"API Response: {book_data}")
            
            # GET title 
            title = book_info.get("title","Unknown (Bilinmiyor)")
            
            # GET authors
            authors = book_info.get("authors","Unknown (Bilinmiyor)")
            
           # use list comp to get author names
           
           # unfortunately, ı got an error message. 
           
           # check data types of author_names objects => str' object has no attribute 'get'
            author_names = []
            
            # is authors object  a list instance 
            if isinstance(authors, list):
                for author in authors:
                    if isinstance(author, dict):
                        name = author.get("name", "Unknown (Bilinmiyor)")
                        author_names.append(name)
                        
            # author_names = [author.get("key","Unknown (Bilinmiyor)") for author in authors] 
            # api does not this way,
            
            author = ",".join(author_names) if author_names else "Unknown (Bilinmiyor)"
             
            # add a new book
            
            new_book = Book(ISBN= clean_ISBN, title = title, author= author)
            # check, has already exists
            if clean_ISBN in [book.ISBN for book in self._book_lists]:
                print("This book has already exists")
            else:    
                self._book_lists.append(new_book)
            # add main menu
            #print(f"Book added (Kitap Eklendi) {title} - {author}")
        except httpx.HTTPStatusError as e:
            print(f"Error! Result of API: {e.response.status_code} - Error Information: {e.response.text}") 
            
        except httpx.RequestError as e:
            print(f"Request Error (İstek Hatası): {e}")
    
    
    #add book manually
    def add_book_manually(self, ISBN: str, title: str, author:str):
        if not ISBN or not title or not author:
            raise ValueError("ISBN, title, and author cannot be blank")
           
        book = Book(ISBN = ISBN, title = title, author= author)
        self._book_lists.append(book)
        return book
        
        

    # remove book by ISBN
    def remove_book(self, ISBN):
        for book in self._book_lists:
            if book.ISBN == ISBN:
                self._book_lists.remove(book)
                return book 
        return None 
    
        # or
        """ 
        O(n) Solving : Burada silinip silinmediğini boyut üzerinden anlar. 
        original_len = len(self._book_lists)
        self._book_lists = [book for book in self._book_lists if book.ISBN != ISBN]
        return len(self._book_lists) < original_len 
        """
    
    # list books in the book_lists
    def list_books(self):
        if not self._book_lists:
            print("❌ There are no books in the library yet. (Henüz Kitap Yok)")
        else:
            for book in self._book_lists:
                print(book) #print(f"{book.__str__()}")
            
    
    # find book by ISBN
    def find_book(self, ISBN):
        for book in self._book_lists:
            if book.ISBN == ISBN:
                return book
        return None
                
    # load books
    def load_books(self):
        self._book_lists = []
        if os.path.exists(self.file_name):
                with open(self.file_name, mode= "r", encoding= "utf-8") as file:
                    try:
                        data = json.load(file)
                    # self._book_lists = [Book(**book_data) for book_data in data]    
                
                # Create a null list, and add new book objects
                        for book_data in data:
                            book_obj = Book(**book_data) # convert json format
                            self._book_lists.append(book_obj)
                    except (json.JSONDecodeError, TypeError):
            # return null list (Boş liste döndür)
                        self._book_lists = []               

    def save_books(self):
        
        with open(self.file_name, "w", encoding= "utf-8") as file:
             #dump() => Convert the Python object to JSON format and write it to a file (Python objesini JSON formatına çevirip dosyaya yazar) 
             # dumps() => returns only a string )(Sadece string döndürür)
                        
            # Use list comp to convert to dictionary structure (Liste üreteçleri kullanarak kitap özelliklerini sözlük yapısına dönüştürelim)
            json.dump([book.__dict__ for book in self._book_lists], file, ensure_ascii=False, indent=4)
                
                