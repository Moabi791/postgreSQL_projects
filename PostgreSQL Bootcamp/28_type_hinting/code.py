#01 Example
from typing import List # , Turple, Set, etc...

class Book:
	pass


class BookShelf:
	def __init__(self, book:List[Book]):
		self.books = BookShelf

	def __str__(self) -> str:
		return f"Bookshelf with {len(self.books)} books"


#02 Example
class Book: 
	TYPES = ("hardcover", "paperback")

	def __init__(self, name:str, book_type: str, weight:int):
		self.name = name
		self.book_type = book_type
		self.weight = weight

	def __repr__(self) -> str:
		return f"<Book {self.name}, {self.book_type} weighing {self.weight}g>"

	@classmethod
	def hardcover(cls, name: str, page_weight: int) ->"Book":
		return cls(name, cls.TYPES[0], page_weight + 100)

	@classmethod
	def paperback(cls, name: str, page_weight: int) ->"Book":
		return cls(name, cls.TYPES[1], page_weight)