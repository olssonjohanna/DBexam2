import pyodbc
connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=BlackFidaySales; Trusted_Connection=yes")
cursor = connection.cursor()

cursor.execute("SELECT * FROM Customer;")
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

cursor.close()
connection.commit()
connection.close()