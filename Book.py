import pyodbc
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
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=DBexam2; Trusted_Connection=yes")

        #get a book by id
        #return it as type of Book
        #if book oes not exist return None
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Book;")
        row = cursor.fechone()
        while row:
            if len(row)==0:
                break
            if row[0] == id:
                book = Book(row.title,row.isbn,row.id,row.pages,row.author_name)
                break

        cursor.close()
        connection.commit()
        connection.close()
        return book

    def getBooksByIsbn(self,isbn):
        #bring books by isbn
        #return list
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=DBexam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Book;")
        row = cursor.fechone()
        while row:
            if len(row) == 0:
                break
            if row == isbn:
                book2=Book(row.title,row.isbn,row.id,row.pages,row.author_name)
                break

        cursor.close()
        connection.commit()
        connection.close()
        return book2
    def getAllBooks(self):
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=DBexam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Book; ")
        row = cursor.fechone()
        while row:
            if len(row) == 0:
                break
            else:
                self.list_of_Books = []
                new_book = Book(row.title,row.isb,row.id,row.pages,row.author_name)
                self.list_of_Books.append(new_book)

        cursor.close()
        connection.commit()
        connection.close()
        return self.list_of_Books


        #bring all book from db
        #return list