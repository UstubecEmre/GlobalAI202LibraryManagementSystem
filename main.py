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
        if choice == "1":
            ISBN = input("Enter ISBN (ISBN Gir):")
            title = input("Enter Title (Kitap Başlığını Gir):")
            author = input("Enter Author (Yazarı Gir): ")
            new_book = Book(ISBN= ISBN, title = title, author= author)
            library.add_book(new_book)
        
        # remove a book
        elif choice == "2":
            ISBN = input("Enter the ISBN number of the book you want to delete (Silmek İstediğin Kitabın ISBN Numarasını Gir): ")
            library.remove_book(ISBN)
        
        # list books
        elif choice == "3":
            library.list_books()
        
        
        