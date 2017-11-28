import pyodbc

class User:
    def __init__(self,name,email,address,password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.list_of_booked_books = []
        self.list_of_borrowed_books = []

    def reserve(self,isbn):
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Book where isbn = '" + str(isbn) + "';")
        data = cursor.fetchone



        cursor.close()
        connection.commit()
        connection.close()

        #work here on DB and list of booked
        pass

    def leaveBackBook(self,book_id):
        # the book will ne left back if it's really borrowed and to be sure of that you must see the db
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * from Borrow where book_id = '" + str(book_id) + "';")
        data = cursor.fetchone

        if data == 0:
            return False

        else:
            book_id.delete()
            return True

        cursor.close()
        connection.commit()
        connection.close()

        pass

    def toString(self):
        return_string = "|Name: " + str(self.name) + " |Email: " + str(self.email) + " |Address: " + str(self.address) + " |Password: " + str(self.password)
        return return_string

class ManageUsers:
    def __init__(self):
        self.list_of_online_users = []

    def addUser(self,id,name,email,address,password):
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User")
        data = cursor.fetchone

        if email == data.email:
            return False

            cursor.close()
            connection.commit()
            connection.close()

        else:
            new_user = (id, name, email, address, password)

            cursor = connection.cursor()
            cursor.execute("INSERT " + str(new_user) + " TO User")
            data = cursor.fetchone

            return True

            cursor.close()
            connection.commit()
            connection.close()

        pass

    def tryToLogIn(self,email,password):
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM User where email = " + str(email) + " and where password = " + str(password) + "")
        data = cursor.fetchone

        if data == 0:
            return False

        else:
            new_user = User(data.name, data.email, data.address, data.password)
            self.list_of_online_users.append(new_user)
            return True

        cursor.close()
        connection.commit()
        connection.close()

        pass

    def getAllUsers(self):  #FUNKAR
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
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
        connection.commit()
        connection.close()

    def logOut(self,email):
        for i in range(len(self.list_of_online_users)):
            if self.list_of_online_users[i].email == email:
                userToBeOutLogged = self.list_of_online_users.pop(i)

                #save changes of user to DB
                break

    def getAnOnlineUserByEmail(self,email):
        for i in range(len(self.list_of_online_users)):
            if self.list_of_online_users[i].email == email:
                return self.list_of_online_users[i]

        return None

var = ManageUsers()
result = ManageUsers.tryToLogIn = lambda: ("jens@email.se", "stol4")
print(result)

for user in result:
    print(user.email)

