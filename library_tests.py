# import pytest
import pytest
import json
import httpx
from unittest.mock import patch, Mock
from library import Library
from book_oop import Book

def create_library_sample():
    library = Library(file_name= "test_library.json")
    library._book_lists = [] # set null list
    # create a new Book instance
    test_book = Book("12345679123","Test Book", "Test Author")
    
    # append book_lists
    library._book_lists.append(test_book)
    
    return library 

    
def test_book_add(monkeypatch):
    library = Library(file_name= "test_library.json")
    
    # Mock => Bu, istediğimiz metot ve özellikleri taklit edebileceğimiz boş bir sahte nesne.
    mock_response = Mock()
    
    # raise for status 
    mock_response.raise_for_status = Mock()
    
    # create a dict
    mock_response.json = Mock(
        # The return_value parameter specifies the value that this method will return.
        # => return_value parametresi bu metodun döndüreceği değeri belirliyor.
        
        return_value={
            "title": "Efficient Library Management System",
            "authors": [{"key":"Emre Üstübeç"}]
        
        }
    )
    
    
    """ 
    # monkeypatch: 
    monkeypatch.setattr temporarily modifies the httpx.get function. ( monkeypatch.setattr ile httpx.get fonksiyonunun gecici olarak degistirilmesini saglar.)

    Now, when the code httpx.get(...) is called, mock_response will be returned instead of the actual HTTP request.
    (Artik kod httpx.get(...) cagirildiginda gercek HTTP istegi yerine  mock_response donecektir)
    
    """ 
    monkeypatch.setattr("httpx.get", lambda url: mock_response)
    
    library.add_book("1234567891230")
    
    # check length of book list
    assert len(library._book_lists) == 1
    
    # select first item
    book = library._book_lists[0]
    
    # assert title and author
    assert book.title == "Efficient Library Management System"
    assert book.author == "Emre Üstübeç" 

def test_remove_book():
    # create an instance
    library = create_library_sample()
    print(f"Starting Book List (Baslangic Kitap Listesi): {library._book_lists}")
    
    # enter ısbn no
    removed = library.remove_book("12345679123")
    print(f"Was the Book (ISBN: 12345679123) deleted (Silindi mi?): {removed}")
    
    
    # returns True if the book is removed, (kitap silinirse True döndür)
    assert removed is True 
  
    assert len(library._book_lists) == 0
    
    
    # Removing non-existing book (ISBN numarası kütüphanede yoksa)
    not_removed = library.remove_book("147258369214")
    
    print(f"Was the book (ISBN:147258369214 ) deleted (Silindi mi?)")
    
    # assert 
    assert not_removed is False
    
    print("✅ Test passed successfully. Final list: (Test Basarili, Nihali Liste: )", library._book_lists)
    
def test_list_books():
    pass

def test_find_book():
    pass


def test_load_books():
    pass

def test_save_books():
    pass 
