import mysql.connector

'''
To establish connection with db
'''
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor() # making a cursor object to navigate through database

word=input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

print(results)
if results:
    for result in results:
        print(result[0])
else:
    print("No word found!")