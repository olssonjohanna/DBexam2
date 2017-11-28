import pyodbc

class Item:
    def __init__(self, id, color, name):
        self.id = id
        self.color = color
        self.name = name

    def toString(self):
        str_to_return = "id: " + str(self.id) + " || color: " + self.color + " || name: " + self.name
        return str_to_return


connection = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server}; Server=localhost; Database=BlackFidaySales; Trusted_Connection=yes")


def getItemByID(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Item;")
    row = cursor.fetchone()
    while row:
        if len(row) == 0:
            break

        if row[0] == id:
            item = Item(row[0], row[1].rstrip(), row[2].rstrip())
            break

    cursor.close()
    connection.commit()
    connection.close()
    return item


def getItemByIDVersion2(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Item where id = '" + str(id) + "';")
    row = cursor.fetchone()
    while row:
        item = Item(row[0], row[1].rstrip(), row[2].rstrip())
        break

    cursor.close()
    connection.commit()
    connection.close()
    return item

item = getItemByID(1)
print(item.toString())
item = getItemByIDVersion2(1)
print(item.toString())