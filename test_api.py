#%% import required libraries and classes
import pytest 
from fastapi.testclient import TestClient
from fastapi import status
from api import (app,
                 Book, 
                 add_book_by_ISBN,
                 add_book_manuelly, 
                 delete_book_by_ISBN, 
                 library_instance) 
# %%
#%% Pytest fixture to reset library before each test (Her test oncesinde kutuphaneyi sifirla)
@pytest.fixture(autouse=True)
def clear_library():
    library_instance._book_lists = []
    yield # run codes
    library_instance._book_lists = []



#%% test
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
                            "ISBN" : "9780091935993",
                            "title" : "The Missing",
                            "author" : "Jane Casey"
    })
    
    # assert status_code(dogrula)
    assert response.status_code == status.HTTP_201_CREATED
    
    created_book = response.json()
    
    
    # assert
    assert created_book["ISBN"] == "9780091935993"
    assert created_book["title"] == "The Missing"
    assert created_book["author"] == "Jane Casey"


#%% test missing fields
def test_add_book_manually_missing_fields():
    response = client.post("/books",
                           json = {
                               "ISBN": "1234567891486",
                               "title":"",
                               "author":"Unknown (Bilinmiyor)"
                           })
    # assert title and author
    assert response.status_code == status.HTTP_400_BAD_REQUEST 
    data = response.json() # convert json
    assert "cannot be blank" in data["detail"]
    
#%% delete book
def test_delete_book_by_ISBN():
    ISBN = "978-605-384-433-4"
    ISBN_cleaned = ISBN.replace("-","")
    
    
    book_to_add = Book(ISBN=ISBN_cleaned, title="Delete Test Book", author="Tester Emre")
    library_instance._book_lists.append(book_to_add)
    
    response = client.delete(f"/books/{ISBN_cleaned}")
    assert response.status_code == status.HTTP_200_OK
    
    removed_book = response.json()
    
    # should return None (None dönmeli)
    book = library_instance.find_book(ISBN_cleaned)
    assert book is None
    
    assert removed_book["ISBN"] == ISBN_cleaned
    assert removed_book["title"] == "Delete Test Book"
    assert removed_book["author"] == "Tester Emre"
    

#%% get books
def test_get_books():
    # you can create a null list, if you are not going to pytest.fixture
    # library_instance._book_lists = []
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
    assert books[0]["ISBN"] == book1.ISBN
    assert books[0]["title"] == book1.title
    assert books[0]["author"] == book1.title
    
    assert books[1]["ISBN"] == book2.ISBN #"1234567890124"
    assert books[1]["title"] == book2.title #"Test Book 2"
    assert books[1]["author"] == book2.author # "GlobalAI"


#%% get book by ISBN Number
def test_get_book_by_ISBN():
    ISBN = "9781410444035"
    
    # Add book manually first
    book_to_add = Book(ISBN=ISBN, title="Get Test Book", author="Tester")
    
    library_instance._book_lists.append(book_to_add)
    
    response = client.get(f"/books/{ISBN}")
    
    # Check status code
    assert response.status_code == status.HTTP_200_OK
    
    getted_book = response.json()
    book = library_instance.find_book(ISBN)
    
    # find_book returns Book object (Book nesnesi olusturuyor, bu nedenle . ile ulas)
    assert getted_book["ISBN"] == book.ISBN
    assert getted_book["title"] == book.title
    assert getted_book["author"] == book.author
    
    