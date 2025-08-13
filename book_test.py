#%% Pytest 
import pytest 
from book_oop import Book

def test_book_creation():
    """Test if a Book object is created with correct attributes. Doğru Özniteliklerle oluşturuldu mu"""
    book = Book("9789750738326","Martin Eden","Jack London") 
    
    
    """Assert (Doğrula)"""
    assert book.ISBN == "9789750738326"   
    assert book.title == "Martin Eden"
    assert book.author == "Jack London"



# %%
