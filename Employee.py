import pyodbc
class Employee:
    def __init__(self,name,email,address,password,salary):
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary
        self.password = password

    def borrowBookToAUser(self,book_id,user_email,):
        # work with db
        # add to borrwing table and you must be sure that book_id is not borrowed
        # at the time

        pass
class ManageEmployees:
    def __init__(self):
        self.list_of_online_employees = []
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

    def addEmployee(self,salary,name,email,address,password): #Klar Måste testas


        #self.connection.cursor()
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Employee VALUES('"+str(email)+ str(name) + str(salary)+  str(address) + str(password)+ "');")
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

    def tryToLogIn(self,email,password): #Klar, måste testas

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


    def getAllEmployees(self): #KLAR
        #return list of all employees
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


    def logOut(self,email): #KLAR ej testad
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


    def getAnOnlineEmployeeByEmail(self,email): #Klar Måste testas
        for i in range(len(self.list_of_online_employees)):
            if self.list_of_online_employees[i].email == email:
                return self.list_of_online_employees[i]

            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Employee WHERE EmployeeEmail='"+ str(email)+"';")
            cursor.fetchone()

            cursor.close()
            self.connection.commit()
            self.connection.close()
        else:

            return None

    def riseSalaryOfAllEmployees(self,increament): # KLAR måste testas
        #change some values in DB
        #connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Employee SET Salary = Salary" + str(increament))
        cursor.fetchone()
        self.connection.commit()
        self.connection.close()