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

# test add_book_by_ISBN => post endpoint
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
    
    
    
#%% test manuelly add book
# using body
def test_add_book_manually():
    ISBN = "978-605-384-433-4"
    payload = {"ISBN": ISBN}
    
    # act (eylem)
    response = client.post("/books", json = payload)
    
    # assert status_code(dogrula)
    assert response.status_code == status.HTTP_201_CREATED
    
    created_book = response.json()
    book = library_instance.find_book(ISBN)
    
    # assert
    assert created_book["ISBN"] == book["ISBN"]
    assert created_book["title"] == book["title"]
    assert created_book["author"] == book["author"]
     
#%% delete book
def test_delete_book_by_ISBN():
    ISBN = "978-605-384-433-4"
    ISBN = ISBN.replace("-","")
    
    response = client.delete("/books/{ISBN}")
    assert response.status_code == status.HTTP_200_OK
    
    removed_book = response.json()
    
    # should return None (None dönmeli)
    book = library_instance.find_book(ISBN)
    assert book is None
    
    assert removed_book["ISBN"] == book["ISBN"]
    assert removed_book["title"] == book["title"]
    assert removed_book["author"] == book["author"]
    

     