#%% Create a main.py
# Create a menu

from book_oop import Book
from library import Library

def main():
    library = Library()
    # create aninfinite loop
    while True:
        print("\n:)Welcome USTUBEC Library Management System")
        print("1. Add a Book (Bir Kitap Ekle)")
        print("2. Remove a Book (Bir Kitap Sil)")
        print("3. List Books (Kitapları Listele)")
        print("4. Search for Book (Kitapları Ara)")
        print("5. Quit (Çıkış Yapın)")
        
        choice = input("Please, Make Your Choice (Seçimini Yapın):\n")
        # add a book
       
        