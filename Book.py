
class Book:
    def __init__(self,title,isbn,id,pages,author_name):
        self.title = title
        self.isbn = isbn
        self.id = id
        self.pages = pages
        self.author_name = author_name
        self.borrowed = False
        self.userThatBorrowed = None
        self.list_of_reserved_to = []

    def getStringOfInfoAboutAuthor(self):
        #work with db and return String
        pass

class ManageBook:
    def __init__(self):
        pass

    def getBookByID(self,id):
        #get a book by id
        #return it as type of Book
        #if book oes not exist return None
        pass

    def getBooksByIsbn(self,isbn):
        #bring books by isbn
        #return list
        pass

    def getAllBooks(self):
        #bring all book from db
        #return list
        pass

