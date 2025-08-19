#%% Create a main.py
# Create a menu

from book_oop import Book
from library import Library
from fastapi import FastAPI
import uvicorn
from api import app

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
            """ 
            title = input("Enter Title (Kitap Başlığını Gir):")
            author = input("Enter Author (Yazarı Gir): ")
            new_book = Book(ISBN= ISBN, title = title, author= author)
            """
            # use try-except to prevent the program from crashing (Program çökmesin diye)
            try:
                library.add_book(ISBN)
                print("✅ Book added successfully (Kitap başarıyla eklendi)")
                library.save_books()
            except Exception as e:
                print(f"❌ Could not add book (Kitap Eklenemedi).The reason is (Sebebi ise): {e}")
        
        # remove a book
        elif choice == "2":
            ISBN = input("Enter the ISBN number of the book you want to delete (Silmek İstediğin Kitabın ISBN Numarasını Gir): ")
            if library.remove_book(ISBN):
                print("✅ Removed (Silindi)")
                library.save_books()
            else:
                print("X Book was not found (Kitap Bulunamadı)")
                
                
                
        # list books
        elif choice == "3":
            library.list_books()
        
        # search for book
        elif choice == "4":
            ISBN = input("Enter the ISBN number of the book you are looking for: ")
            book = library.find_book(ISBN)
            if book:
                print("✅Found (Bulundu):", book)
            else:
                print("❌ Not Found (Bulunamadı)")
        
        
        # quit
        elif choice == "5":
            print("Exit (Çıkış Yapılıyor)")
            break
        
        # else
        else:
            print("Invalid choice. Please try again!!! (Geçersiz seçim, lütfen tekrar deneyin)")
        

# check
if __name__ == "__main__":
    # uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True) you are going to show API, you can use (Web servisinde gormek istersen bunu kullanabilirsin)
      main()  
# %%
