# Library Management System

This project implements a simple Library Management System using object-oriented programming techniques. The program utilizes a text file, `books.txt`, as a database to store information about books, including book name, author, release date, and number of pages. The system provides functionality to list books, add new books, and remove existing books from the library.

## Table of Contents
- [Library Class](#library-class)
- [Methods](#methods)
  - [List Books](#list-books)
  - [Add Book](#add-book)
  - [Remove Book](#remove-book)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Menu](#menu)

## Library Class

### Constructor and Destructor
- The `Library` class has a constructor method that opens the `books.txt` file in append and read mode (`"a+"`). If the file does not exist, it will be created.
- The destructor method is responsible for closing the file when the program terminates.

## Methods

### List Books
- This method reads the contents of the `books.txt` file and prints the book names and authors.

### Add Book
- This method prompts the user for input to add a new book to the `books.txt` file. It appends the information to the file.

### Remove Book
- This method removes a book with the given title from the `books.txt` file. It prompts the user for input, reads the file contents, removes the specified book, and updates the file.

## Getting Started

To get started with the Library Management System, follow these steps:

1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the program using `python library_management_system.py`.

## Usage

After running the program, you can interact with the Library Management System using the provided menu.

## Menu

```
*** MENU ***
1) List Books
2) Add Book
3) Remove Book
Q) Exit
```

- Enter the corresponding value (1, 2, 3, or Q) to perform the desired action.
- The program will prompt you for further input based on your selection.

Happy coding!
