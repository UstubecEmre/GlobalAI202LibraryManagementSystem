#%% import required libraries
from fastapi import FastAPI, Body, Query, Path
from pydantic import BaseModel, Field

#%% create pydantic Book class

class Book(BaseModel):
    ISBN : str = Field(min_length = 10, max_length = 13, description = "Book ISBN Number")
    title: str = Field(min_length = 1, description = "Book Title")
    author : str = Field(min_length = 1, description = "Book Author")




#%% create an instance
api = FastAPI()
