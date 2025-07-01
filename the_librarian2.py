# the_librarian.py

# Sample library data
library = [
    {"title": "Title 1", "author": "Author 1", "year_of_publication": 1998, "isbn": "ISBN 778-445-111", "available": True},
    {"title": "Title 2", "author": "Author 2", "year_of_publication": 1808, "isbn": "ISBN 628-495-121", "available": False},
]

def add_book():
    """Add a new book to the library."""
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the name of the author: ").strip()
    year_of_publication = int(input("Enter the year of publication: "))
    isbn = input("Enter the ISBN: ").strip()
    library.append({"title": title, "author": author, "year_of_publication": year_of_publication, "isbn": isbn, "available": True})
    print(f"Book '{title}' by {author} added successfully.")

def view_books():
    """Display all books in the library."""
    if not library:
        print("No books available in the library.")
        return
    for idx, book in enumerate(library, start=1):
        print(f"{idx}. {book['title']} by {book['author']}, "
              f"Published: {book['year_of_publication']}, ISBN: {book['isbn']}, "
              f"Available: {'Yes' if book['available'] else 'No'}")

def update_book(isbn):
    """Update the information of a book given its ISBN."""
    for book in library:
        if book["isbn"] == isbn:
            print(f"Updating details for '{book['title']}' by {book['author']}...")
            title = input(f"Enter the title of the book or leave blank to keep '{book['title']}': ").strip()
            if title:
                book['title'] = title
            author = input(f"Enter the author of the book or leave blank to keep '{book['author']}': ").strip()
            if author:
                book['author'] = author
            return f"Book '{book['title']}' updated successfully."
    return "Book not found in the library."

def delete_book(isbn):
    """Remove a book from the library using its ISBN."""
    for index, book in enumerate(library):
        if book["isbn"] == isbn:
            confirm_delete = input(f"Are you sure you want to delete '{book['title']}' by {book['author']}? (yes/no): ").strip().lower()
            if confirm_delete == "yes":
                del library[index]
                return f"Book '{book['title']}' deleted successfully."
            return "Deletion cancelled."
    return "Book not found in the library."

def search_book(title):
    """Search for a book by its exact title."""
    for book in library:
        if book["title"].lower() == title.lower():
            return f"'{book['title']}' by {book['author']}, ISBN: {book['isbn']}, Available: {'Yes' if book['available'] else 'No'}"
    return "Book not found in the library."

def borrow_book(isbn):
    """Mark a book as borrowed (not available)."""
    for book in library:
        if book["isbn"] == isbn:
            if book["available"]:
                book["available"] = False
                return f"'{book['title']}' has been successfully borrowed."
            return f"'{book['title']}' is currently unavailable."
    return "Book not found in the library."

def return_book(isbn):
    """Mark a book as returned (available)."""
    for book in library:
        if book["isbn"] == isbn:
            if not book["available"]:
                book["available"] = True
                return f"'{book['title']}' has been successfully returned."
            return f"'{book['title']}' was not borrowed."
    return "Book not found in the library."

def main():
    """Main menu loop for the library management system."""
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
    while True:
        print(menu)
        choice = input("Choose an option from the menu above: ").strip()
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            isbn = input("Enter the ISBN of the book you want to update: ").strip()
            print(update_book(isbn))
        elif choice == "4":
            isbn = input("Enter the ISBN of the book you want to delete: ").strip()
            print(delete_book(isbn))
        elif choice == "5":
            title = input("Enter the title of the book you are searching for: ").strip()
            print(search_book(title))
        elif choice == "6":
            isbn = input("Enter the ISBN of the book you want to borrow: ").strip()
            print(borrow_book(isbn))
        elif choice == "7":
            isbn = input("Enter the ISBN of the book you want to return: ").strip()
            print(return_book(isbn))
        elif choice == "8":
            print("Thank you for using the library management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
