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
    ISBN : str = Field(..., pattern = r"^\d{10,17}$", description = "Book ISBN Number") # Field(#min_length = 10, max_length = 17, description = "Book ISBN Number")
    title: str = Field(min_length = 1, description = "Book Title")
    author : str = Field(min_length = 1, description = "Book Author")



class BookRequest(BaseModel):
    ISBN: str
    title: str
    author: str 
    

""" regex regex="^\d{10,17}$" )=> 
^ => starts with (baslasin)
\d{10-17} => Returns a match where the string contains digits (numbers from 10-17) (10-17 arasi degerleri iceren eslesmeleri dondurur)
$ => ends with (bitsin)

"""




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
    title = "Emre Ustubec Basic Library Management System",
    description = "A Basic FastAPI Example",
    version = "1.0.0",
    lifespan =  lifespan
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
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "No Book Found With That ISBN Number (Bu ISBN Numarasina Ait Kitap Bulunamadi) "
        )
        
# old version (eski versiyonum, ISBN numarasina gore kitap ekler, govdeyi dahil etmez)

@app.post("/books/{ISBN}", status_code = status.HTTP_201_CREATED)
def add_book_by_ISBN(ISBN:str):
    # add_book method cleans ISBN ()
    book = library_instance.add_book(ISBN)
    if book:
        return book
    else:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Book couldn't be added (Kitap Eklenemedi)"
        )


# add_book manuelly 
@app.post("/books", status_code = status.HTTP_201_CREATED, response_model = Book)
def add_book_manuelly(request: BookRequest):
    try:
        book = library_instance.add_book(
            ISBN = request.ISBN,
            title = request.title,
            author = request.author
        )
        return book
    except Exception as e :
        raise HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = str(e)
    )

    

@app.delete("/books/{ISBN}")
def delete_book_by_ISBN(ISBN: str):
    book = library_instance.remove_book(ISBN.replace("-",""))
    if book:
        return book # show deleted book
    else:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Book Not Found (Kitap Bulunamadi)"
        )
            


