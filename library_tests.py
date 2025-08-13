# import pytest
import pytest
import json
import httpx
from unittest.mock import patch, Mock
from library import Library
from book_oop import Book

def create_library_sample():
    library = Library(file_name= "library.json")
    library._book_lists = [] # set null list
    # create a new Book instance
    test_book = Book("12345679123","Test Book", "Test Author")
    
    # append book_lists
    library._book_lists.append(test_book)
    
    return library 

    
def test_book_add():
    pass 

def test_remove_book():
    pass 

def test_list_books():
    pass

def test_find_book():
    pass


def test_load_books():
    pass

def test_save_books():
    pass 
