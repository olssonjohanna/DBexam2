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
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

    def addEmployee(self,salary,name,email,address,password):


        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Employee")
        data = cursor.fetchone()

        if email == data[0]:
            cursor.close()
            self.connection.commit()
            self.connection.close()
            return False


        else:
            #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
            new_Employee = Employee(salary,name,email,address,password)
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO Employee VALUES'"+str(new_Employee)+"';" )
            cursor.fetchone()

            cursor.close()
            self.connection.commit()
            self.connection.close()

            return True




    def tryToLogIn(self,email,password):

        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Employee WHERE EmployeeEmail ='"+ str(email)+ "'AND Password ='"+ str(password)+ "';")
        data = cursor.fetchone()
        if data:
            new_employee = Employee(data[1],data[0],data[3],data[4], data[2])
            self.list_of_online_employees.append(new_employee)
            cursor.fetchone()


            cursor.close()
            self.connection.commit()
            self.connection.close()

            return True
        else:
            cursor.close()
            self.connection.commit()
            self.connection.close()

            return False


    def getAllEmployees(self):
        #return list of all employees
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Employee;")
        data = cursor.fetchone()
        list_of_Employee =[]
        while data:

            new_Employee = Employee(data[1],data[0],data[3],data[4],data[2])
            list_of_Employee.append(new_Employee)
            data = cursor.fetchone()
        cursor.close()
        self.connection.commit()
        self.connection.close()
        return list_of_Employee


    def logOut(self,email):
        for i in range(len(self.list_of_online_employees)):
            if self.list_of_online_employees[i].email == email:
                employeeToBeOutLogged = self.list_of_online_employees.pop(i)
                #save changes of employee to DB


                cursor = self.connection.cursor()
                cursor.execute("UPDATE Employee SET Name = '"+employeeToBeOutLogged.name+"' WHERE EmployeeEmail = '"+ str(email)+"', Salary = '"+employeeToBeOutLogged.salary+"' WHERE EmployeeEmail = '"+ str(email) + ", Adress = '"+employeeToBeOutLogged.adress+"' WHERE EmployeeEmail = '"+ str(email) + " , Password = '"+employeeToBeOutLogged.password+"' WHERE EmployeeEmail = '" + str(email) + "';" )
                cursor.fetchone()

                cursor.close()
                self.connection.commit()
                self.connection.close()

                break


    def getAnOnlineEmployeeByEmail(self,email):
        for i in range(len(self.list_of_online_employees)):
            if self.list_of_online_employees[i].email == email:
                return self.list_of_online_employees[i]

        return None

    def riseSalaryOfAllEmployees(self,increament):
        #change some values in DB
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Employee SET Salary = Salary" + str(increament))
        cursor.fetchone()
        self.connection.commit()
        self.connection.close()