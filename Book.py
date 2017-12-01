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

    def getStringOfInfoAboutAuthor(self, author):
        #work with db and return String

        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Author WHERE Email = '" + str (author) +"';")
        allInfo = cursor.fetchall()

        cursor.close()
        connection.commit()
        connection.close()

        return allInfo

        pass

class ManageBook:
    def __init__(self):
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

    def getBookByID(self,id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ISBNBook where ISBN in (select ISBN from Book where bookID = "+str(id)+");")
        row = cursor.fetchone()
        book = None
        while row:
            if len(row)==0:
                break

            book = Book(row[1],row[0],id,row[2],"")
            break

        cursor.close()
        self.connection.commit()
        self.connection.close()

        return book

    def getBooksByIsbn(self,isbn):
#        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM ISBNBook where ISBN in (select ISBN from Book where ISBN = " + str(isbn) + ");")
        row = cursor.fetchone()
        book = None

        while row:
            if len(row) == 0:
                break

            book = Book(row[1], row[0], row[2], isbn, "")
            break

        cursor.close()


        self.connection.commit()
        self.connection.close()

        return book

    def getAllBooks(self):
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT ISBNBook.Title, ISBNBook.Pages, ISBNBook.ISBN, Author.Name, bookID from ISBNBook join Book on ISBNBook.ISBN = Book.ISBN join Relation on Relation.ISBN = ISBNBook.ISBN join Author on Author.Email = Relation.Email")
        row = cursor.fetchone()

        list_of_Books = []

        while row:
            if len(row) == 0:
                break

            else:
                new_book = Book(row[0], row[1], row[2], row[3], "")
                list_of_Books.append(new_book)
                row = cursor.fetchone()

        cursor.close()
        self.connection.commit()
        self.connection.close()

        return list_of_Books

#var = ManageBook()
#result = var.getAllBooks()
#print(result)

#for each in result:
#   print(each.title)



h = Book("f", "1", 10, "5200", "hh")
v = "b@email.se"
r = h.getStringOfInfoAboutAuthor(v)
print (r)
