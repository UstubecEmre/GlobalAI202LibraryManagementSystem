#%% import required libraries
from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel, Field
from library import Library

#%% create pydantic Book class

class Book(BaseModel):
    ISBN : str = Field(min_length = 10, max_length = 17, description = "Book ISBN Number")
    title: str = Field(min_length = 1, description = "Book Title")
    author : str = Field(min_length = 1, description = "Book Author")




#%% create an instance
app = FastAPI()

# create an instance from Library
library_instance = Library()

@app.get("/books")
def get_books():
    books = [book.__dict__ for book in library_instance._book_lists]
    return {"books":books}

""" 
@app.get("/books/{ISBN}")
def get_books_by_ISBN(ISBN):
    clean_ISBN = ISBN.replace("-","")
    # iterate each book item (Her bir kitap objesi icin don)
    for book in library_instance._book_lists:
        if book.ISBN.replace("-","") == clean_ISBN:
            return book.__dict__
    return {"book":"Not Found (Bulunamadi)"}
""" 


@app.get("/books/{ISBN}")
def get_books_by_ISBN(ISBN: str):
    book = library_instance.find_book(ISBN.replace("-",""))
    if book:
        return {"book":book.__dict__} # convert to JSON object
    else:
        return {"book":"Not Found(Bulunamadi)"}
    

