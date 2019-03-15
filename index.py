import mysql.connector
from mysql.connector import errorcode

try:
    cnn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='django'
    )
    print("It's Work")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something wrong with username or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database do not exist")
    else:
        print(e)

    cursor = cnn.cursor()

    addName = ("Insert INTO Name(fName, lName) VALUES (%s, %s)")
    fName = "hachim"
    lName = "haggar"
    empName = (fName, lName)

    cursor.execute(addName, empName)

    cnn.commit()
    cursor.close()
    cnn.close()
