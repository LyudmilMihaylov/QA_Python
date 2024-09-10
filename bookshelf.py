from abc import ABC, ABCMeta, abstractmethod
from datetime import datetime, timedelta

class LibraryItemMeta(ABCMeta):
    def __new__(cls, name, bases, attrs):
        if 'get_details' not in attrs or not callable(attrs['get_details']):
            raise TypeError(f"Missing or non-callable 'get_details' method in {name}")
        
        return super().__new__(cls, name, bases, attrs)

class LibraryItem(ABC, metaclass=LibraryItemMeta):
    def __init__(self, title, creation_date, author):
        self.title = title
        self.creation_date = creation_date
        self.author = author

    @abstractmethod
    def get_details(self):
        pass

class ItemAgeMixin:
    def get_age(self):
        return datetime.now() - self.creation_date

class Book(ItemAgeMixin, LibraryItem):
    def __init__(self, title, creation_date, author, series=None, edition=None):
        super().__init__(title, creation_date, author)
        self.series = series
        self.edition = edition

    def get_details(self):
        details = f"Book: {self.title} by {self.author}"
        if self.series:
            details += f", Series: {self.series}"
        if self.edition:
            details += f", Edition: {self.edition}"
        return details

class BookBuilder:
    def __init__(self, title, creation_date, author):
        self.title = title
        self.creation_date = creation_date
        self.author = author
        self.series = None
        self.edition = None

    def with_series(self, series):
        self.series = series
        return self

    def with_edition(self, edition):
        self.edition = edition
        return self

    def build(self):
        return Book(self.title, self.creation_date, self.author, self.series, self.edition)

class Journal(ItemAgeMixin, LibraryItem):
    def __init__(self, title, creation_date, author, frequency=None):
        super().__init__(title, creation_date, author)
        self.frequency = frequency

    def get_details(self):
        details = f"Journal: {self.title} by {self.author}"
        if self.frequency:
            details += f", Frequency: {self.frequency}"
        return details

class JournalBuilder:
    def __init__(self, title, creation_date, author):
        self.title = title
        self.creation_date = creation_date
        self.author = author
        self.frequency = None

    def with_frequency(self, frequency):
        self.frequency = frequency
        return self

    def build(self):
        return Journal(self.title, self.creation_date, self.author, self.frequency)

class LibrarySystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LibrarySystem, cls).__new__(cls)
        return cls._instance

class BookShelf(ItemAgeMixin):
    capacity = 100

    def __init__(self, creation_date):
        self.creation_date = creation_date
        self.items = []

    def add_item(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        for item in self.items:
            print(item.get_details())

class LibraryItemFactory:
    @staticmethod
    def create_item(item_type, title, creation_date, author, **kwargs):
        if item_type == 'book':
            builder = BookBuilder(title, creation_date, author)
            if 'series' in kwargs:
                builder.with_series(kwargs['series'])
            if 'edition' in kwargs:
                builder.with_edition(kwargs['edition'])
            return builder.build()

        elif item_type == 'journal':
            builder = JournalBuilder(title, creation_date, author)
            if 'frequency' in kwargs:
                builder.with_frequency(kwargs['frequency'])
            return builder.build()

        else:
            raise ValueError("Invalid item type")

bookshelf = BookShelf(creation_date=datetime(2022, 1, 1))

book_builder = BookBuilder("The Great Gatsby", datetime(1925, 4, 10), "F. Scott Fitzgerald")
book = book_builder.with_edition("First").with_series("Classics").build()

bookshelf.add_item(book)

journal_builder = JournalBuilder("Nature", datetime(2021, 5, 12), "Various Authors")
journal = journal_builder.with_frequency("Monthly").build()

bookshelf.add_item(journal)

print("\nItems on the bookshelf:")
bookshelf.get_items()

factory_book = LibraryItemFactory.create_item(
    "book", "1984", datetime(1949, 6, 8), "George Orwell", series="Dystopian", edition="Second")

factory_journal = LibraryItemFactory.create_item(
    "journal", "Science", datetime(2022, 7, 1), "Various Authors", frequency="Weekly")

bookshelf.add_item(factory_book)
bookshelf.add_item(factory_journal)

print("\nItems on the bookshelf after adding more items:")
bookshelf.get_items()

print(f"\nAge of 'The Great Gatsby' book: {book.get_age().days} days old")