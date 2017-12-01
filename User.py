import pyodbc

class User:
    def __init__(self,email,name,address,password):
        self.email = email
        self.name = name
        self.address = address
        self.password = password
        self.list_of_booked_books = []
        self.list_of_borrowed_books = []
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

    def reserve(self, isbn):
        # work here on DB and list of booked

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Book where ISBN = '" + str (isbn) +"';")
        data = cursor.fetchall()
        self.list_of_booked_books.append(data)

        cursor.close()
        self.connection.commit()
        self.connection.close()
        return self.list_of_booked_books

    def leaveBackBook(self, bookID):
        # the book will ne left back if it's really borrowed and to be sure of that you must see the db
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Borrow WHERE BookID = '" + str (bookID) +"';")
        data = cursor.fetchall()

        if data == 0:
            return False

        if data:
            cursor.execute("DELETE FROM Borrow WHERE BookID = '" + str (bookID) +"';")

            cursor.close()
            self.connection.commit()
            self.connection.close()
            return True

        else:
            cursor.close()
            self.connection.commit()
            self.connection.close()
            return None

    def toString(self):
        return_string = "|Name: " + str(self.name) + " |Email: " + str(self.email) + " |Address: " + str(self.address) + " |Password: " + str(self.password)
        return return_string

class ManageUsers:
    def __init__(self):
        self.list_of_online_users = []
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        self.list = []


    def addUser(self,email,name,address,password):
        # check that same email does not exists and if exists return false
        # else add user to the db and return true

        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        #self.connection.cursor()
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Users VALUES ('" + str (email) + "','" +  str (name) + "','" +  str (address) + "','" +  str (password) + "')")

            cursor.close()
            self.connection.commit()
            self.connection.close()

            return True

        except Exception as e:
            print (e)
            cursor.close()
            self.connection.commit()
            self.connection.close()
            return False

    def tryToLogIn(self,email,password):
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users WHERE UserEmail = '" + str(email) + "' AND Password = '"+ str(password)+"';")

        data = cursor.fetchone()

        if data == 0:
            return False

        else:
            new_user = User(data[0], data[1], data[2], data[3])
            self.list_of_online_users.append(new_user)

            cursor.close()
            self.connection.commit()
            self.connection.close()
            return True

    def getAllUsers(self): #printar obj
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Users;")
        data = cursor.fetchall()

        while data:
            if len(data) == 0:
                break

            else:
                new_user = User(data[0], data[1], data[2], data[3])
                self.list.append(new_user)

                print(self.list)
            return self.list

        cursor.close()
        self.connection.commit()
        self.connection.close()

    def logOut(self,email):  #returnerar None
        print(self.list_of_online_users)
        for i in range(len(self.list_of_online_users)):
            if self.list_of_online_users[i].email == email:

                userToBeOutLogged = self.list_of_online_users.pop(i)


                #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

                cursor = self.connection.cursor()
                try:
                    cursor.execute("UPDATE Users SET Name = '"+userToBeOutLogged.name+"'WHERE UserEmail= ' " +str(email)+"', Adress ='"+userToBeOutLogged.address+"'WHERE UserEmail = '"+ str(email)+"',Password='"+userToBeOutLogged.Password+"'WHERE UserEmail = '" + str(email)+ "';")

                    cursor.close()
                    self.connection.commit()
                    self.connection.close()
                    return True
                    #save changes of user to DB
                except:
                    cursor.close()
                    self.connection.commit()
                    self.connection.close()
                    return False

    def getAnOnlineUserByEmail(self,email):
        def getAnOnlineUserByEmail(self, email):
            for i in range(len(self.list_of_online_users)):
                if self.list_of_online_users[i].email == email:
                    return self.list_of_online_users[i]

            return None

#TESTAR
var = ManageUsers()

name = "swdgjjsg"
email = "krghjddddergkldl@email.se"
passw = "stol4"
address = "Kssss 12"
password = "dkfk"
bookid = "5"

var2 = User(name, email, address, password)

#r = var2.leaveBackBook("20")
#print (r)

#result = var.addUser(email,name,address,password)
#print(result)

result = var.tryToLogIn(email, password)
print(result)

res = var.logOut(email)
print (res)

#resulst = var.getAllUsers()
#print (resulst)

#res = var.getAnOnlineUserByEmail(email)
#print (res)

#t = var2.reserve(1)
#print(t[0])
