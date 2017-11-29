import pyodbc
class Employee:
    def __init__(self,name,email,address,password,salary):
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary
        self.password = password

    def borrowBookToAUser(self,book_id,user_email,):
        #work with db
        #think that before this book will be borrowed you should check
        #that no one else in queue to reserve the book
        #or this user is actually first in the queue

        pass

class ManageEmployees:
    def __init__(self):
        self.list_of_online_employees = []

    def addEmployee(self,salary,name,email,address,password):

        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Employee")
        data = cursor.fetchone()

        if email == data[1]:
            return False

            cursor.close()
            connection.commit()
            connection.close()
        else:
            connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
            new_Employee = Employee(salary,name,email,address,password)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Employee VALUES'"+str(new_Employee)+"';" )
            cursor.fetchone()

            return True

            cursor.close()
            connection.commit()
            connection.close()


    def tryToLogIn(self,email,password):

        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Employee WHERE EmployeeEmail ='"+ str(email)+ "'AND Password ='"+ str(password)+ "';")
        data = cursor.fetchone()
        if data:
            new_employee = Employee(data[0],data[1],data[2],data[3], data[4])
            self.list_of_online_employees.append(new_employee)
            return True
        else:
            return False

        cursor.close()
        connection.commit()
        connection.close()

    def getAllEmployees(self):
        #return list of all employees
        connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM EMployee;")
        data = cursor.fetchone()
        list_of_Employee =[]
        while data:
            if len(data) == 0:
                break
            else:
                new_Employee = Employee(data[0],data[1],data[2],data[3],data[4])
                list_of_Employee.append(new_Employee)
            return list_of_Employee
        cursor.close()
        connection.commit()
        connection.close()


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