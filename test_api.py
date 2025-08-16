#%% import required libraries and classes
from fastapi.testclient import TestClient
from fastapi import status
from api import (app, 
                 add_book_by_ISBN,
                 add_book_manuelly, 
                 delete_book_by_ISBN, 
                 library_instance) 
# %% test

client = TestClient(app)

def test_add_book_by_ISBN():
    ISBN = "978-605-384-535-5"
    response = client.post(f"/books/{ISBN}")
    
    # check status code
    assert response.status_code == status.HTTP_201_CREATED
    
    created_book = response.json()
    
    book = library_instance.find_book(ISBN)
    
    assert created_book["ISBN"] == book["ISBN"]
    assert created_book["title"] == book["title"]
    assert created_book["author"] == book["author"]
    
    
    
