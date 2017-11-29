import pyodbc

class User:
    def __init__(self,name,email,address,password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.list_of_booked_books = []
        self.list_of_borrowed_books = []
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

    def reserve(self,isbn):
        # work here on DB and list of booked


        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Book where isbn = '" + str(isbn) + "';")
        data = cursor.fetchone

        self.list_of_booked_books.append(data)

        cursor.close()
        self.connection.commit()
        self.connection.close()

    def leaveBackBook(self,book_id):  #FUNKAR
        # the book will ne left back if it's really borrowed and to be sure of that you must see the db
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Borrow WHERE BookID = '" + str(book_id) + "';")
        data = cursor.fetchone

        if data == 0:
            return False

        elif data == book_id:
            ("DELETE * FROM Borrow WHERE bookID = '" + str(book_id) + "';")
            cursor.close()
            self.connection.commit()
            self.connection.close()
            return True

        else:
            cursor.close()
            self.connection.commit()
            self.connection.close()
            return False




    def toString(self):
        return_string = "|Name: " + str(self.name) + " |Email: " + str(self.email) + " |Address: " + str(self.address) + " |Password: " + str(self.password)
        return return_string

class ManageUsers:
    def __init__(self):
        self.list_of_online_users = []
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")


    def addUser(self,email,name,address,password): #KLAR måste testas
        # check that same email does not exists and if exists return false
        # else add user to the db and return true

        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        #self.connection.cursor()
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Users VALUES('"+str(email)+ str(name) +str(address)+str(password)+"');")
            cursor.fetchone()

            cursor.close()
            self.connection.commit()
            self.connection.close()

            return True

        except:
            cursor.close()
            self.connection.commit()
            self.connection.close()
            return False

    def tryToLogIn(self,email,password): #FUNKAR!
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserEmail = '" + str(email) + "' AND Password = '"+str(password)+"';")

        data = cursor.fetchone()

        if data == 0:
            return False

        else:
            new_user = User(data[1], data[0], data[2], data[3])
            self.list_of_online_users.append(new_user)


            cursor.close()
            self.connection.commit()
            self.connection.close()
            return True



    def getAllUsers(self):  #FUNKAR måste testas igen
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users;")
        data = cursor.fetchone()

        list = []

        while data:
            if len(data) == 0:
                break

            else:
                new_user = User(data.Name, data.UserEmail, data.Adress, data.Password)
                list.append(new_user)
                data = cursor.fetchone()


            return list

        cursor.close()
        self.connection.commit()
        self.connection.close()

    def logOut(self,email): #KLAR måste testas
        for i in range(len(self.list_of_online_users)):
            if self.list_of_online_users[i].email == email:
                userToBeOutLogged = self.list_of_online_users.pop(i)

                #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

                cursor = self.connection.cursor()
                cursor.execute("UPDATE Users SET Name = '"+userToBeOutLogged.name+"'WHERE UserEmail= ' " +str(email)+"', Adress ='"+userToBeOutLogged.address+"'WHERE UserEmail = '"+ str(email)+"',Password='"+userToBeOutLogged.Password+"'WHERE UserEmail = '" + str(email)+ "';")
                cursor.fetchone()

                cursor.close()
                self.connection.commit()
                self.connection.close()

                #save changes of user to DB
                break

    def getAnOnlineUserByEmail(self,email): #måste testas
        for i in range(len(self.list_of_online_users)):
            if self.list_of_online_users[i].email == email:
                return self.list_of_online_users[i]
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Users WHERE UserEmail = ' "+ str(email)+ "';")

            cursor.close()
            self.connection.commit()
            self.connection.close()
        else:
            return None



#TESTAR
var = ManageUsers()

name = "Ulf"
email = "jens@email.se"
passw = "stol4"
address = "K 12"
password = "11aa"
bookid = "5"


var2 = User(name, email, address, password)

result = var.addUser(email,name,address,password)
print(result)
