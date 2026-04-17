"""
Program to design a basic library management system.

Provides functionalities to borrow a book, return a book, and search
for a book. Uses OOP concepts to create necessary classes (Book,
Library) and applies OOP features like encapsulation. Stores book
details using file handling along with exception handling.
"""

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower_name = ""
        self.borrower_id = ""


class Library:
    def __init__(self, filename):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                
                i = 0
                while i < len(lines):
                    title = lines[i].strip()
                    author = lines[i + 1].strip()
                    isbn = lines[i + 2].strip()
                    available = lines[i + 3].strip().lower() == "true"
                    borrower_name = lines[i + 4].strip()
                    borrower_id = lines[i + 5].strip()
                    
                    book = Book(title, author, isbn)
                    book.available = available
                    book.borrower_name = borrower_name
                    book.borrower_id = borrower_id
                    self.books.append(book)
                    i += 6
        except Exception:
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.title}\n")
                f.write(f"{book.author}\n")
                f.write(f"{book.isbn}\n")
                f.write(f"{book.available}\n")
                f.write(f"{book.borrower_name}\n")
                f.write(f"{book.borrower_id}\n")

    def add_book(self, book):
        for b in self.books:
            if b.isbn == book.isbn:
                print("\n" + "=" * 45)
                print("  ERROR: Book already exists!")
                print("=" * 45)
                return

        self.books.append(book)
        self.save_books()
        print("\n" + "=" * 45)
        print("  Book added successfully!")
        print("=" * 45)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def view_all_books(self):
        if not self.books:
            print("\n" + "=" * 45)
            print("  No books in library.")
            print("=" * 45)
            return

        print("\n" + "=" * 70)
        print("                    LIBRARY BOOKS")
        print("=" * 70)
        
        for i, book in enumerate(self.books, 1):
            status = "Available" if book.available else "Borrowed"
            print(f"  {i}. {book.title} by {book.author}")
            print(f"     ISBN: {book.isbn} | Status: {status}")
            if not book.available:
                print(f"     Borrowed by: {book.borrower_name} (ID: {book.borrower_id})")
        
        print("=" * 70)
        print(f"  Total Books: {len(self.books)}")
        print("=" * 70)

    def borrow_book(self, title):
        book = self.search_book(title)
        if book:
            if book.available:
                clear_screen()
                print("\n" + "=" * 45)
                print("           BORROW BOOK")
                print("=" * 45)
                borrower_name = input("  Borrower Name : ").strip()
                borrower_id = input("  Borrower ID   : ").strip()
                
                book.available = False
                book.borrower_name = borrower_name
                book.borrower_id = borrower_id
                self.save_books()
                
                print("\n" + "=" * 45)
                print("  Book borrowed successfully!")
                print("=" * 45)
            else:
                print("\n" + "=" * 45)
                print("  ERROR: Book is already borrowed.")
                print("=" * 45)
        else:
            print("\n" + "=" * 45)
            print("  ERROR: Book not found.")
            print("=" * 45)

    def return_book(self, title):
        book = self.search_book(title)
        if book:
            if not book.available:
                clear_screen()
                print("\n" + "=" * 45)
                print("           RETURN BOOK")
                print("=" * 45)
                print("\n  Book Details:")
                print("  " + "-" * 35)
                print(f"  Title        : {book.title}")
                print(f"  Author       : {book.author}")
                print(f"  ISBN         : {book.isbn}")
                print("\n  Borrower Information:")
                print("  " + "-" * 35)
                print(f"  Borrower Name: {book.borrower_name}")
                print(f"  Borrower ID  : {book.borrower_id}")
                print("  " + "-" * 35)
                
                confirm = input("\n  Confirm return? (y/n) : ").strip().lower()
                
                if confirm == "y":
                    book.available = True
                    book.borrower_name = ""
                    book.borrower_id = ""
                    self.save_books()
                    print("\n" + "=" * 45)
                    print("  Book returned successfully!")
                    print("=" * 45)
                else:
                    print("\n" + "=" * 45)
                    print("  Return cancelled.")
                    print("=" * 45)
            else:
                print("\n" + "=" * 45)
                print("  ERROR: Book was not borrowed.")
                print("=" * 45)
        else:
            print("\n" + "=" * 45)
            print("  ERROR: Book not found.")
            print("=" * 45)


def get_book_input():
    print("\n" + "=" * 45)
    print("           ADD NEW BOOK")
    print("=" * 45)
    print("\n  Enter book details:")
    print("  " + "-" * 35)
    title = input("  Title  : ").strip()
    author = input("  Author : ").strip()
    isbn = input("  ISBN   : ").strip()
    return Book(title, author, isbn)


def display_menu():
    clear_screen()
    print("\n" + "=" * 45)
    print("           LIBRARY MENU")
    print("=" * 45)
    print("  1. Add Book")
    print("  2. Search Book")
    print("  3. Borrow Book")
    print("  4. Return Book")
    print("  5. View All Books")
    print("  6. Exit")
    print("=" * 45)


def get_menu_choice():
    return input("  Enter your choice : ").strip()


def process_menu_choice(choice, library):
    if choice == "1":
        library.add_book(get_book_input())

    elif choice == "2":
        clear_screen()
        title = input("  Enter title to search : ").strip()
        book = library.search_book(title)
        if book:
            status = "Available" if book.available else "Borrowed"
            print("\n" + "=" * 45)
            print(f"  Title: {book.title}")
            print(f"  Author: {book.author}")
            print(f"  ISBN: {book.isbn}")
            print(f"  Status: {status}")
            if not book.available:
                print(f"  Borrower: {book.borrower_name} (ID: {book.borrower_id})")
            print("=" * 45)
        else:
            print("\n" + "=" * 45)
            print("  ERROR: Book not found.")
            print("=" * 45)

    elif choice == "3":
        clear_screen()
        title = input("  Enter title to borrow : ").strip()
        library.borrow_book(title)

    elif choice == "4":
        clear_screen()
        title = input("  Enter title to return : ").strip()
        library.return_book(title)

    elif choice == "5":
        clear_screen()
        library.view_all_books()

    elif choice == "6":
        clear_screen()
        print("\n" + "=" * 45)
        print("  Exiting system... Thank you!")
        print("=" * 45)
        return True

    else:
        clear_screen()
        print("\n" + "=" * 45)
        print("  ERROR: Invalid choice!")
        print("=" * 45)
    
    return False


def main():
    clear_screen()
    print("\n" + "=" * 45)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)
    
    library = Library("books.txt")
    if library.books:
        print(f"\n  Loaded {len(library.books)} book(s) from file.")
    
    while True:
        display_menu()
        choice = get_menu_choice()
        if process_menu_choice(choice, library):
            input("\n  Press Enter to exit...")
            break
        input("\n  Press Enter to continue...")


if __name__ == "__main__":
    main()