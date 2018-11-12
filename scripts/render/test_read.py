#!/usr/bin/python

import MySQLdb

###############################################

basededatos='render'
tabla='test'

###############################################

# Open database connection
db = MySQLdb.connect("localhost","root","pepito1234",basededatos)

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM %s" %tabla
#print sql

try:

   # Execute the SQL command
   cursor.execute(sql)
   #print"execute"
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   #print"fetchall"
   for row in results:
       holder=1
       print(row)
# BUSCA ultimo job para agregar el nuevo
  

except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
