import mysql.connector
import os

def insertin(cursor,line):
    query = "UPDATE cet4 SET word = %s WHERE word = '' LIMIT 1"
    cursor.execute(query,(line,))


mytext = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="qweaz123",
  database="words"
)

mycursor=mytext.cursor()

file_path = '/Users/lucifior/Documents/CET4_edited01.txt'

with open(file_path,'r',encoding='utf-8')as file:
    lines = file.read().splitlines()
    for i, line in enumerate(lines):
        if line.strip():
            insertin(mycursor,line.strip())


mytext.commit()

mycursor.close()
mytext.close()