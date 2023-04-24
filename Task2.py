'''Write a class structure that implements a library. Classes:

1) Library - name, books = [], authors = []

2) Book - name, year, author (author must be an instance of Author class)

3) Author - name, country, birthday, books = []

Library class

Methods:

- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

- group_by_author(author: Author) - returns a list of all books grouped by the specified author

- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books'''


class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books


class Book:
    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'"{self.name}" ({self.year}), {self.author.name}'


class Library:
    def __init__(self, name, books=[], authors=[]):
        self.name = name
        self.books = books
        self.authors = authors

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book)
        return book

    def group_by_author(self, author: Author):
        return author.books

    def group_by_year(self, year: int):
        year_list = []
        for book in self.books:
            if book.year == year:
                year_list.append(book)
        return year_list


auth = Author('George Orwell', 'US', '1903')
print(auth.name)
library = Library('Kyiv Lib')
library.new_book('1984', 1948, auth)
print(library.books)
print(library.group_by_author(auth))
print(library.group_by_year(1948))