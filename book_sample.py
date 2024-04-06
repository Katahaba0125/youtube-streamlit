import json
import os

def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=2)

def display_books(books):
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} - {book['author']} ({book['progress']}%)")

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    progress = int(input("Enter progress percentage: "))
    
    book = {
        "title": title,
        "author": author,
        "progress": progress
    }

    books.append(book)
    save_books(books)
    print("Book added successfully.")

def update_progress(books):
    display_books(books)
    index = int(input("Enter the index of the book to update progress: ")) - 1

    if 0 <= index < len(books):
        progress = int(input("Enter new progress percentage: "))
        books[index]["progress"] = progress
        save_books(books)
        print("Progress updated successfully.")
    else:
        print("Invalid index.")

def main():
    books = load_books()

    while True:
        print("\nReading Tracker Menu:")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Update Progress")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            update_progress(books)
        elif choice == "4":
            print("Exiting Reading Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
