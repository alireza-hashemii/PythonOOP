from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self,name:str,genre:str):
        self.books.append(Book(name,genre))
        print("It has added")

    def modify_name(self,id,name):
        for book in self.books:
            if book.id == id:
                book.name = name
            print("Name has changed")

    def modify_genre(self,id,genre):
        for book in self.books:
            if book.id == id:
                book.genre = genre
            print("Genre has changed")

    def search(self,pattern):
        return [book for book in self.books if book.find(pattern)]

