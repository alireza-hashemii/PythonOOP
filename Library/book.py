import datetime

id = 0

class Book:
    def __init__(self,name: str,genre: str):
        self.name = name 
        self.date = datetime.datetime.now()
        self.genre = genre
        global id
        id += 1
        self.id = id

    def find(self,name:str):
        return name in self.name 
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nDate: {self.date}\nGenre: {self.genre}"

