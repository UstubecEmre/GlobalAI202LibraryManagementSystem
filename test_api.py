#%% import required libraries and classes
from fastapi.testclient import TestClient
from fastapi import status
from api import (app,
                 Book, 
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
def test_add_book_manually_success():
    
    #payload = {"ISBN": ISBN}
    
    # act (eylem)
    response = client.post("/books",
                           json= {
                            "ISBN" = "9780091935993",
                            "title" = "The Missing",
                            "author" = "Jane Casey"
    })
    
    # assert status_code(dogrula)
    assert response.status_code == status.HTTP_201_CREATED
    
    created_book = response.json()
    
    
    # assert
    assert created_book["ISBN"] == "9780091935993"
    assert created_book["title"] == "The Missing"
    assert created_book["author"] == "Jane Casey"
    
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
    

#%% get books
def test_get_books():
    # create a null list
    library_instance._book_lists = []
    book1 = Book(ISBN = "1234567890123",title ="Test Book 1", author ="Emre Ustubec")
    book2 = Book(ISBN = "1234567890124",title = "Test Book 2",author = "GlobalAI")
    
    library_instance._book_lists.extend([book1, book2])
    
    # make a get request 
    response = client.get("/books")
    # check status code
    assert response.status_code == status.HTTP_200_OK
    
    # convert to json
    books = response.json()
    
    # assert total books in the _books_list
    assert len(books) == 2
    
    # test all params 
    assert book1["ISBN"] == "1234567890123"
    assert book1["title"] == "Test Book 1"
    assert book1["author"] == "Emre Ustubec"
    
    assert book2["ISBN"] == "1234567890124"
    assert book2["title"] == "Test Book 2"
    assert book2["author"] == "GlobalAI"


#%% get book by ISBN Number
def test_get_book_by_ISBN():
    ISBN = "9781410444035"
    response = client.get(f"/books/{ISBN}")
    
    # Check status code
    assert response.status_code == status.HTTP_200_OK
    
    getted_book = response.json()
    book = library_instance.find_book(ISBN)
    
    # find_book returns Book object (Book nesnesi olusturuyor, bu nedenle . ile ulas)
    assert getted_book["ISBN"] == book.ISBN
    assert getted_book["title"] == book.title
    assert getted_book["author"] == book.author
    
    