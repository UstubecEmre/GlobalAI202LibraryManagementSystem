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
    test_book = Book("1234567912345","Test Book", "Test Author")
    
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
    removed = library.remove_book("1234567912345")
    print(f"Was the Book (ISBN: 1234567912345) deleted (Silindi mi?): {removed}")
    
    
    # returns True if the book is removed, (kitap silinirse True döndür)
    assert removed is True 
  
    assert len(library._book_lists) == 0
    
    
    # Removing non-existing book (ISBN numarası kütüphanede yoksa)
    not_removed = library.remove_book("1472583692149")
    
    print(f"Was the book (ISBN:1472583692149) deleted (Silindi mi?)")
    
    # assert 
    assert not_removed is False
    
    print("✅ Test passed successfully. Final list: (Test Basarili, Nihali Liste: )", library._book_lists)


def test_list_books(capsys):
    """ 
    capsys
    Pytest'in yerlesik fixture'idir. 
    
    Ekrana (stdout) veya hatalara (stderr) yazilan tum ciktilari yakalar. 
    
    Böylece print() ile yazilan metinleri test etmemize olanak saglar.
    
    """
    # call the create_library_sample
    library = create_library_sample()
    
    # list books (Kitaplari listele)
    library.list_books()
    
    
    # readouterr() => 
    """
    capsys.readouterr() ile yakalanan tum standart cikti ve hata mesajlarini almamizi saglayan fonsiyondur.

    Donen deger bir namedtuple idir:

    captured.out → stdout (ekrana yazilan normal mesajlari ifade eder)

    captured.err → stderr (ekrana yazilan hata mesajlarini ifade eder)
    
    """
    
    captured = capsys.readouterr() 
    assert "Test Book" in captured.out 
    assert "Succesfully Viewed (Basariyla Goruntulendi)" in captured.out
    

def test_find_book():
    #call the create library sample
    library = create_library_sample()
    
    # enter test book  ISBN
    found = library.find_book("1234567912345")
    # return True
    assert found is not None
    
    # valid the title (Basligi dogrula) 
    assert found.title =="Test Book"
   
   # if enter the wrong ISBN number
    not_found = library.find_book("1472589635400")
    
    # assert not_found
    assert not_found is None

def test_load_books():
    pass

def test_save_books():
    pass 
