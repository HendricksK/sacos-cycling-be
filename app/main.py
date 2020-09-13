from flask import Flask 

import psycopg2

app = Flask(__name__) 

@app.route("/") 
def home_view(): 
	try:
	   connection = psycopg2.connect(user="#",
	                                  password="#",
	                                  host="#",
	                                  port="#",
	                                  database="#")
	   cursor = connection.cursor()
	   postgreSQL_select_Query = "select * from article"

	   cursor.execute(postgreSQL_select_Query)
	   print("Selecting rows from mobile table using cursor.fetchall")
	   mobile_records = cursor.fetchall() 
	   
	   print("Print each row and it's columns values")
	   for row in mobile_records:
	       print("Id = ", row[0], )
	       print("Name = ", row[1])
	       print("Article Data  = ", row[2])
	       print("Article Url  = ", row[3], "\n")

	except (Exception, psycopg2.Error) as error:
		print ("Error while fetching data from PostgreSQL", error)

	finally:
	    #closing database connection.
	    if(connection):
	        cursor.close()
	        connection.close()
	        print("PostgreSQL connection is closed")

	return "<h1>Welcome to Geeks for Geeks...123</h1>"
