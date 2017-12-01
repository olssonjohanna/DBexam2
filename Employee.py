import pyodbc
class Employee:
    def __init__(self,name,email,address,password,salary):
        self.name = name
        self.email = email
        self.address = address
        self.salary = salary
        self.password = password
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")

    def borrowBookToAUser(self, book_id, user_email):

        cursor = self.connection.cursor()

        try:
            cursor.execute("INSERT INTO Borrow VALUES ('" + str (self.email) + "','" +  str (book_id) + "','" +  str (user_email) + "','" + str(2017) + "')")

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

        # work with db
        # add to borrwing table and you must be sure that book_id is not borrowed
        # at the time

    def toString(self):
        return self.name

class ManageEmployees:
    def __init__(self):
        self.list_of_online_employees = []
        self.connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=Exam2; Trusted_Connection=yes")


    def addEmployee(self,salary,name,email,address,password):

        #self.connection.cursor()
        cursor = self.connection.cursor()
        try:
            cursor.execute("INSERT INTO Employee VALUES ('" + str (email) + "','" +  str (name) + "'," +  str(salary) + ",'" + str(address) + "','" + str(password) +"');")

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

    def tryToLogIn(self, login, passw):

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Employee WHERE EmployeeEmail = '" + str(login) + "' AND Password ='" + str (passw) + "';")
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
            print (self.list_of_online_employees)

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
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Employee SET Salary = Salary + " + str(increament))

        cursor.close()
        self.connection.commit()
        self.connection.close()
        return True


#TESTA
m = ManageEmployees()
#res = m.addEmployee(210,"ojiij", "kdw", "Kdd 1", "ssdkdkj")
#print (res)

#res1 = m.tryToLogIn("david@gmail.se", "123")
#print (res1)

#res = m.logOut("david@gmail.se")
#print (res)

#def printallt(lista):
 #   for element in lista:
  #      print(element.toString())

#r = m.getAllEmployees()
#printallt(r)

#r = m.getAnOnlineEmployeeByEmail("jens@email.se")
#print (r)

r = m.riseSalaryOfAllEmployees(200)
print (r)

#h = Employee("David", "david@gmail.se","Kungsgatan 12", 20000, "123")
#w = h.borrowBookToAUser("30", "jens@email.se")
#print (w)
