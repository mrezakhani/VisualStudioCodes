import json
import os
LIBRARY_FILE = "library.txt"

# Initialize library file if not exist
def initialize_library():
    if not os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "w") as file:
            json.dump([], file)

# Load Library data
def load_library():
    with open(LIBRARY_FILE, "r") as file:
        return json.load(file)

# Save Library Data
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent = 4)

# Add a new book
def add_a_book_to_library(library):
    title = input("Enter the book title:").strip()
    auther = input("Enter the book auther:").strip()
    while True:
        try:
            year = int(input("Enter the publication year:"))
            break
        except ValueError:
            print("Please enter a valid value for puplication.")
    book = {"title": title, "auther": auther, "year": year, "status": "available"}
    library.append(book)
    print(f"book '{title}' by auther '{auther}' and publication year '{year}' added successfully!")


# List all books
def list_books(library):
    if not library:
        print("The library is empty")
        return
    print("\n=== List of books in your Library")
    for index, book in enumerate(library, start=0):
        status = "Available" if book["status"] == "available" else "Borrowed"
        print(f"{index + 1}. {book['title']} by {book['auther']} ({book['year']}) - ({status})")


# Search for books
def seach_books(library):
    if not library:
        print("The Library is empty.")
        return
    query = input("Enter title or auther or year to search: ").strip().lower()
    resault = [book for book in library if query in book["title"].lower() or query in book["auther"].lower()];
    if not resault:
        print("Sorry, no book found.")
    for book in resault:
        print("")
        status = "Available" if book["status"] == "available" else "Borrowed"
        print(f"- {book['title']} by {book['auther']} ({book['year']}) - ({status})")


# Borrow or return a book
def borrow_return_book(library):
    list_books(library)
    if not library:
        return
    try:
        book_index = int(input("Enter the number of book, that you want to borrow or return: ")) -1
        if book_index < 0:
            print("Invalid selection")
        else:
            book = library[book_index]
            if book["status"] == "available":
                book["status"] = "borowed"
                print(f"Yow borrowed {book['title']}")
            else:
                book["status"] = "available"
                print(f"You returned {book['title']}")
    except ValueError:
        print("Invalid Input. Please enter a valid number.")    

def main_menu():
    initialize_library()
    library = load_library()
    while True:
        print("\n ===== Library Manager")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Books")
        print("4. Borrow/Return Book")
        print("5. Save and Exit")
        choice = int(input("\nPlease select an operation: "))
        if choice == 1:
            add_a_book_to_library(library)
        elif choice == 2: 
            list_books(library)
        elif choice == 3: 
            seach_books(library)
        elif choice == 4:
            borrow_return_book(library)
        elif choice == 5: 
            save_library(library)
            print("Library data saved. Goodbye!")
            break
        else:
            print("Invalid Choice, Please enter a number between 1 to 5")

if __name__ == "__main__":
    main_menu()
    