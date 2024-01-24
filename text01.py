import mysql.connector

mytext = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="qweaz123",
        database = "words"
    )

mycursor = mytext.cursor()

mycursor.execute("""
        CREATE TABLE cet4 (
            word VARCHAR(50),
            means varchar(50),
            sound longblob
        )
    """)