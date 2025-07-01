# library = []

library = [
    {"title": "Title 1", "author": "Author 1", "year_of_publication": 1998, "isbn": "ISBN 778-445-111", "available": True},
    {"title": "Title 2", "author": "Author 2", "year_of_publication": 1808, "isbn": "ISBN 628-495-121", "available": False},
]

def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the name of the author of the book: ").strip()
    year_of_publication = int(input("Enter the year of publication of the book: "))
    isbn = input("Enter the ISBN of the book you want to delete: ").strip()
    library.append({"title": title, "author": author, "year_of_publication": year_of_publication, "isbn": isbn, "available": True})
    return f"Book {title} by {author} added successfully"


def view_books():
    for book in library:
        print(f"{book["title"]} by {book["author"]}, published on {book["year_of_publication"]}, ISBN: {book["isbn"]}, Available: {book["available"]}")


def update_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            title = input(f"Enter the title of the book or leave blank to use {book['title']}: ").strip().lower()
            if title:
                book['title'] = title
            author = input(f"Enter the author of the book or leave blank to use {book['author']}: ").strip().lower()
            if author:
                book['author'] = author
            return f"Book has been successfully updated"
    return "Book not in library, do you want to add instead?"


def delete_book(isbn):
    for index, book in enumerate(library):  
        if book["isbn"] == isbn:
            confirm_delete = input(f"Are you sure you want to delete {book['title']} by {book['author']}").lower().strip()
            if confirm_delete == "yes":
                del library[index]
                return "Book deleted successfully"
            return "Returning to main menu"
    return "Book not in library, do you want to add instead?"


def search_book(title):
    """Search for a book by its exact title."""
    for book in library:
        if book["title"].lower() == title.lower():
            return f"'{book['title']}' by {book['author']}, ISBN: {book['isbn']}, Available: {'Yes' if book['available'] else 'No'}"
    return "Book not found in the library."

def borrow_book(isbn):
    # isbn = input("Enter the ISBN of the book you want to borrow: ").strip()
    for book in library:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                return f"{book['title']} has been successfully borrowed."
            return f"{book['title']} is currently unavailable."
    return "Book not found in library."


def return_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            # title = input(f"Enter the title of the book to you want to return: ").strip().lower()
           if not book["available"]:
                book["available"] = True
                return f"'{book['title']}' has been successfully returned."
        return "Book not for library, do you want to add instead?"




menu = """
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit
"""

print("Welcome to SQI Library")

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()
    
    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "3":
        isbn = input("Enter the isbn of the book you want to update: ").strip()
        print(update_book(isbn))
    elif choice == "4":
        isbn = input("Enter the isbn of the book you want to update: ").strip()
        print(delete_book(isbn))
    elif choice == "5":
        title = input("Enter the title of the book you are searching for: ").strip().lower()
        print(search_book(title))
    elif choice == "6":
         isbn = input("Enter the ISBN of the book you want to borrow: ").strip()
         print(borrow_book(isbn))
    elif choice == "7":
        isbn = input("Enter the isbn of the book you want to return: ").strip()
        print(return_book(isbn))
    elif choice == "8":
            print("Thank you for using the SQI library. You are always welcome again")
            break
    else:
            print("Invalid choice. Please select a valid option.")

