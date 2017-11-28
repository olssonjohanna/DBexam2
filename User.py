#12
class User:
    def __init__(self,name,email,address,password):
        self.name = name
        self.email = email
        self.address = address
        self.password = password
        self.list_of_booked_books = []
        self.list_of_borrowed_books = []

    def reserve(self,isbn):
        #work here on DB and list of booked
        pass

    def leaveBackBook(self,book_id):
        #the book will ne left back if it's really borrowed and to be sure of that you must see the db
        pass

class ManageUsers:
    def __init__(self):
        self.list_of_online_users = []

    def addUser(self,id,name,email,address,password):
        #check that same email does not exists and if exists return false
        #else add user to the db and return true
        pass

    def tryToLogIn(self,email,password):
        #see if email and password are in db
        #if they are, bring all other data and create user
        #then add the user to the list of online users
        #and return true
        #if email and password are not in db return false then
        pass

    def getAllUsers(self):
        #return list of all users
        pass

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