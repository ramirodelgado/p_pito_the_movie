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
   for row in results:
       holder=holder+1
       #print(row)
# BUSCA ultimo job para agregar el nuevo
   if 1==1:
       print"start 1==1()"
       lastjob=holder
       newjob=lastjob-1
       print(newjob)
       # lastjob=row[0]
       # newjob=lastjob+1
       #AGREGA NEW JOB
       #sql= """ INSERT INTO """+tabla+""" """"+
       sql = """INSERT INTO """+tabla+""" """+"(job_n, job_blend,job_scene, job_status, job_frame_i, job_frame_f, job_folder, job_priority) VALUES ('%d','%s', '%s','%s', '%d', '%d', '%s', '%d' )" % (newjob,jblend,jscene,jstatus,fi,ff,jfolder,jpriority)

       try:
          # Execute the SQL command
          print(sql)
          cursor.execute(sql)

          #print(sql)
          # Commit your changes in the database
          #db.commit()
          #print("########\nADDED: Job %d table \n ('%d','%s', '%s', '%d', '%d', '%s' )  " % (newjob,newjob,jblend,jstatus,fi,ff,jfolder))
          jobtable="""job_"""+str(newjob)

          #GENERA TABLA PARA EL NUEVO JOB
          newjob_sql = """CREATE TABLE """+jobtable+""" (TASKNUMBER  INT(8),TASKDATE  CHAR(22),TASKSCENE CHAR(55),TASKFRAME INT(22),TASKDIR CHAR(33),TASKBLEND CHAR(55),TASKTIME TIME(2),TASKSTATUS CHAR(22),TASKIP CHAR(22))"""
          #print(newjob_sql)
          cursor.execute(newjob_sql)
         # db.commit()

          #CREA ESTRUCTURA DE LA BASE DE DATOS
          print(jobframes)
          #AGREGA TASKS utilizando la variable tasksql A LA TABLA DEL JOB GENERADO POR newjob_sql.
          for n in range(jobframes):
              #print(n)
              tasksql="""INSERT INTO """+jobtable+""" """+"(TASKNUMBER,TASKDATE,TASKSCENE,TASKFRAME,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP) VALUES ('%d','%s', '%s', '%d', '%s','%s','%d', '%s', '%s' )" % (n,0,jscene,n+fi,jfolder,jblend,0,jstatus,0)
              #print(tasksql)
              cursor.execute(tasksql)

          db.commit()
          print("AGREGADOS %s frames (%s-%s) como %s del archivo '%s' en carpeta %s de la escena %s." % (str(jobframes),fi,ff,jobtable,jblend,jfolder,jscene))
          #print('TABLA DEL JOB CREADA')

       except:
           print"Error al insertar %s en %s" % (sql,tabla)
           db.rollback()

       # disconnect from server
       #db.close()

except:
   print "Error: unable to fetch data"

# disconnect from server
db.close()
