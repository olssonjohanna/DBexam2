
class Employee:
    def __init__(self,name,email,address,password,salary):
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary
        self.password = password

    def borrowBookToAUser(self,book_id,user_email):
        #work with db
        #think that before this book will be borrowed you should check
        #that no one else in queue to reserve the book
        #or this user is actually first in the queue
        pass

class ManageEmployees:
    def __init__(self):
        self.list_of_online_employees = []

    def addEmployee(self,id,name,email,address,password):
        #check that same email does not exists and if exists return false
        #else add employee to the db and return true
        pass

    def tryToLogIn(self,email,password):
        #see if email and password are in db
        #if they are, bring all other data and create employee
        #then add the employee to the list of online employees
        #and return true
        #if email and password are not in db return false then
        pass

    def getAllEmployees(self):
        #return list of all employees
        pass

    def logOut(self,email):
        for i in range(len(self.list_of_online_employees)):
            if self.list_of_online_employees[i].email == email:
                employeeToBeOutLogged = self.list_of_online_employees.pop(i)
                #save changes of employee to DB
                break

    def getAnOnlineEmployeeByEmail(self,email):
        for i in range(len(self.list_of_online_employees)):
            if self.list_of_online_employees[i].email == email:
                return self.list_of_online_employees[i]

        return None

    def riseSalaryOfAllEmployees(self,increament):
        #change some values in DB
        pass