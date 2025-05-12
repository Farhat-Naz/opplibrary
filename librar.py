class Library:
    def __init__(self, name, location):
        self.lib_name = name
        self.lib_location = location
        self.books=[]
        
class Book:
    def __init__(self, name, author):
        self.book_name = name
        self.book_author = author
     
    def add_book(self, book):
     
        self.books.append(book)  
                
l1 = Library("The Book", "farhat")
print(l1.lib_name, l1.lib_location)


l2 = Book("The Paksitan", "farh")
print(l2.book_name, l2.book_author)     
l1.books.append(l2)

print(f"Books in library: {[book.book_name for book in l1.books]}")
