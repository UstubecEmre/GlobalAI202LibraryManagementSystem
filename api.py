#%% import required libraries
from fastapi import (FastAPI, # for FastAPI instance 
                     Body, # for endpoint
                     Query, 
                     Path, 
                     HTTPException, # for handle exception
                     status # for HTTP status codes
                     
                     
                     
                     )
from pydantic import BaseModel, Field

from library import Library
import asyncio
from contextlib import asynccontextmanager

from typing import List # for response_model

#%% create pydantic Book class

class Book(BaseModel):
    ISBN : str = Field(min_length = 10, max_length = 17, description = "Book ISBN Number")
    title: str = Field(min_length = 1, description = "Book Title")
    author : str = Field(min_length = 1, description = "Book Author")








#%% create lifespan for FastAPI

""" Handle application startup and shutdown events. (Baslatma ve kapatmayi yonetecekti)"""
# use asynccontextmanager decorator
@asynccontextmanager
async def lifespan(app: FastAPI):
    """code that will run when the application starts (Uygulama baslarken calisacak kodlar)"""
    
    # __init__ method already running load_books() method (Zaten load_books() methodunu cagiracak ) 
    print("Application is running")
    
    yield # run (calisacak)
    
    print("This application is shutting down (Uygulama Kapatiliyor)). Books are saving")
    
    # save books
    library_instance.save_books()
    print("Books saved succesfully (Kitaplar Basarili Bir Sekilde Kaydedildi)")
    

 
#%% create an instance
app = FastAPI(
    "title":"Emre Ustubec Basic Library Management System",
    "desciption": "A Basic FastAPI Example",
    "version":"1.0.0",
    "lifespan": lifespan
)

# create an instance from Library
library_instance = Library()

@app.get("/books", response_model = List[Book])
def get_books():
    # if you are not going to use response_model, you can use these codes (Eger response_model yani yanitin nasil olması gerektigini belirleme kullanmayacaksan)
    # books = [book.__dict__ for book in library_instance._book_lists]
    # return {"books":books}
    return library_instance._book_lists

""" 
@app.get("/books/{ISBN}")
def get_book_by_ISBN(ISBN):
    clean_ISBN = ISBN.replace("-","")
    # iterate each book item (Her bir kitap objesi icin don)
    for book in library_instance._book_lists:
        if book.ISBN.replace("-","") == clean_ISBN:
            return book.__dict__
    return {"book":"Not Found (Bulunamadi)"}
""" 


@app.get("/books/{ISBN}", response_model = Book)
def get_book_by_ISBN(ISBN: str):
    book = library_instance.find_book(ISBN.replace("-",""))
    if book:
        # if you are not going to use response_model, you can use this code
        # return {"book":book.__dict__} # convert to JSON object
        return book # response_model
    else:
        raise HTTPException(
            status = status.HTTP_404_NOT_FOUND,
            detail = "No Book Found With That ISBN Number (Bu ISBN Numarasina Ait Kitap Bulunamadi) "
        )
        
    

@app.post("/books/{ISBN}")
def add_book_by_ISBN(ISBN:str):
    # add_book method cleans ISBN ()
    library_instance.add_book(ISBN)
    return {"message":"Added book (if not already exists) (Kitap EKlendi (Daha onceden yoksa))"}


@app.delete("/books/{ISBN}")
def delete_book_by_ISBN(ISBN: str):
    result = library_instance.remove_book(ISBN.replace("-",""))
    if result:
        return {"message":"Book removed successfully (Kitap basarili bir sekilde silindi)"}
    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Book Not Found (Kitap Bulunamadi)"
        )
            


