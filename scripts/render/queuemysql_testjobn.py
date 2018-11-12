#!/usr/bin/python

import MySQLdb

jscene='E13'
jblend='E13_T01-T03_AF_noiseTest3000cd.blend'
fi=0
ff=677
jfolder='/mnt/z/_FOTO/E13'
jpriority=3

###############################################

basededatos='render'
tabla='test'
jstatus='EN_COLA'

###############################################
jobframes=ff-fi+1

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
   holder=0
   for row in results:
       holder=holder+1
       #print(row)
# BUSCA ultimo job para agregar el nuevo
   if 1==1:
       print"1==1"
       #lastjob=row[0]
       lastjob=holder
       newjob=lastjob-1
       print(newjob)
except:
    print"woops"
