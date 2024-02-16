class Library:
    def __init__(self): # Created the constructor method
        self.file = open("books.txt", "a+")

    def __del__(self): # Created the destructor method
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        book_lines = self.file.read().splitlines()
        for line in book_lines:
            book_info = line.split(',')
            print(f"Book: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        book_lines = self.file.read().splitlines()

        updated_book_lines = [line for line in book_lines if title_to_remove not in line]

        self.file.seek(0)
        self.file.truncate()
        self.file.writelines('\n'.join(updated_book_lines))
        print(f"Book '{title_to_remove}' removed successfully.")

# Created an object named "lib" with "Library" class
lib = Library()

# Created a menu to interact with the "lib" object
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("Q) Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "Q":
        print("Exiting the Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again with the choices 1, 2, 3, or Q.")