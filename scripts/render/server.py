#!/usr/bin/python

import MySQLdb
import os
import time
import re

#####################################################################
# DB Data
# base de datos es el nombre de la base de datos a utilizar de mysql
# tabla es el nombre de la tabla de la base de datos desde donde se
# guardaran los jobs.
#####################################################################

host="localhost"
basededatos='render'
tabla='test'

#####################################################################
# jstatus es el status default con el que se generan los jobs y los tasks
# rjob es el status de running_job asignado a jobs y tasks
# done status es el status de finishedjobs
#####################################################################

jstatus='EN_COLA'
rjob='EN_PROCESO'
donestatus='TERMINADO'

#####################################################################
# ESTRUCTURA DE FOLDERS DEL RENDER
#-folder es donde se guardan los temporales de los requests
#-output folder es donde se guardan los Stills
#-working folder es el folder local donde cada maquina graba \
#   sus temporales antes de copiarlos al ouput folder
#####################################################################

folder='/y2/scripts/render/workers'
outputfolder='/x/Renders'
workingfolder='LOCALRENDERFOLDER'
#ruta='/WORKINGFOLDER'

def searchfiles():
    qf=[]

    for qf in os.listdir(folder):
        time.sleep(1)

        #print(qf)
        if qf.endswith('d'):
            #print "endswith(d)_start"
            doneupdate_req(qf)
            #print "endswith(d)_end"
        if qf.endswith('py'):
            1==1
            #print"ignora %s" % qf
        if qf.endswith('php'):
            1==1
        if qf.endswith('r'):
            1==1
        #     print"endswith(r)"
        #     #print('reguest')
        #     #print(qf)
        #     #print time.localtime()
        #     #time.sleep(1)
        #     #print("no available workers")
        if qf.endswith('.swp'):
            1==1
        #     time.sleep(1)
        #     print"endswith(swp)"
        else:
            print(qf[-1])
            isd=qf[-1].isdigit()
            #CHECA si qf acaba en Digitos
            #m=re.search(r'\d+$', qf)
            #if m is not None:
            if isd:
                print(qf)
                print('request del ip'+qf)
                request(qf)
                print"try try_send_render()"
                try_send_render(qf,folder)

def file_exists(path):
    checkfile=str(path)
    return_val=exists(checkfile)
    return return_val

def finished_job(jb_n):
    db = MySQLdb.connect("localhost","root","pepito1234",basededatos)
    cursor = db.cursor()
    print "start_finished_job() "
    print(jb_n)

    sql_finishedjob= "UPDATE %s SET job_status='%s'  WHERE job_n=%d" % (tabla,donestatus,int(jb_n))
    #SET job_status=donestatus en tabla WHERE job_n=
    print(sql_finishedjob)
    cursor.execute(sql_finishedjob)
    print"cursorexecute"
    db.commit()
    print("end_finished_job()")


def request(qf):
    print"start_request(qf)  %s"%qf
    #Lee request file creado por el cliente
    rfile=folder+'/'+qf
    print(rfile)
    rf = open(rfile, 'r')
    print(rf.read().split('|'))
    rf.close()
    print 'terminado leer client request file %s, GENERANDO TASKFILE.' % rfile
    print 'end_request(qf)'
    #Genera taskfile

def doneupdate_req(qf):
    print'start_doneupdate_req()'
    print(qf)
    dfile=folder+'/'+qf
    print(dfile)
    df = open(dfile, 'r')
    originaltask=df.readline()
    print(originaltask)
    donetime=df.readline()
    print(donetime)
    taskjob=df.readline()
    print(taskjob)

    print "dfile %s" % dfile

    print "originaltask %s" % originaltask
    print "donetime %s" % donetime
    df.close()
    print'end_doneupdate_req()'
    print'try_update_task_done()'
    update_task_done(originaltask,donetime,taskjob,dfile)

def update_testif_job_done():
    print "start update_job_done()"
    db = MySQLdb.connect(host,"root","pepito1234",basededatos)
    cursor = db.cursor()
    #Busca jobs con status en proceso
    sql_readall = "SELECT * FROM %s WHERE job_status = '%s' " % (tabla,rjob)
    cursor.execute(sql_readall)
    print(sql_readall)
    results = cursor.fetchone()
    db.commit()
    #print(str(results))
    #UPDATE DONEJOBTABLE
    jb_n=str(results[0])
    ujd_jobt="job_%s" % (jb_n)
    print"ujd_jobt %s " % ujd_jobt
    #Regresa todos los jobs de la tabla ujd_jobt en donestatus
    sql_read_ujd= "SELECT * FROM %s" % (ujd_jobt)
    print(sql_read_ujd)
    cursor.execute(sql_read_ujd)
    ujd_results = cursor.fetchall()
    #print"ujdresults fetchall"
    #print str(ujdresults)
    #ujdstats guarda status de todas las tasks en el job
    ujdstats=[]
    #print "start ujdresults"
    for row in ujd_results:
        #print str(row[7])
        ujdstats.append((row[7]))
    #print "end ujdresults"
    #print str(ujdstats)
        #print(str(u[7]))
    #compara si items en ujdstats son iguales
    #print(ujdstats)
    db.commit()
    if all_same(ujdstats):
        print ujdstats[0]
        if ujdstats[0]=='TERMINADO':
            print"todas tasks %s en la tabla %s" % (donestatus,ujd_jobt)
            finished_job(jb_n)
    else:
        print"no todas las tasks estan en el mismo status"
    #print all_same(ujdstats)


    print"end update_job_done()"

# def jobdone(jb_n):
#     db = MySQLdb.connect("localhost","root","pepito1234",basededatos)
#     cursor = db.cursor()
#     jobdone=
#     cursor.execute(jobdone)



def all_same(items):
    print "start all_same()"
    print(items)
    print("end_start_all_same()")
    return all(x == items[0] for x in items)


def update_task_done(originaltask,donetime,taskjob,dfile):

    #ACTUALIZA TASK TERMINADA desde el file ip+d
    db = MySQLdb.connect("localhost","root","pepito1234",basededatos)
    cursor = db.cursor()
    print"###########################DONEUPDATE###########################"
    print"start_update_task_done()"
    uTASKNUM=str(originaltask).split(',')[0].strip('[').rstrip().strip('\'')
    print("originaltask %s" % originaltask)
    uTASKTIME=donetime.rstrip()
    uJOB=taskjob
    ujob_table='job_%s' % uJOB
    uSTATUS=donestatus
    #print uTASKNUM
    #print uJOB
    #print ujob_table

    ## Genera sql task update del job
    done_sql="UPDATE %s SET TASKSTATUS='%s', TASKTIME='%s' WHERE TASKNUMBER=%s" % (ujob_table,uSTATUS,uTASKTIME,uTASKNUM)
    print(done_sql)
    cursor.execute(done_sql)
    #print"Rxecuted done_sql"

    db.commit()
    print"commit"
    print("dfile")
    os.remove(dfile)
    print("borra donefile")
    print"end_update_task_done()"
    print"########################### DONEUPDATE-END ###########################"






def update(job,status,activeframe,ip):

    db = MySQLdb.connect("localhost","root","pepito1234",basededatos)
    cursor = db.cursor()
    ajob='job_'+str(job)
    stamp = time.strftime('%d/%m/%Y/ %H:%M:%S', time.localtime(time.time()))
    print"start update()"
    print ajob
    print status
    print activeframe
    print ip
    print stamp

    queuesql="UPDATE `%s` SET TASKSTATUS='%s', TASKIP='%s',TASKDATE='%s' WHERE TASKFRAME=%s"%(ajob,status,ip,stamp,activeframe)
    print(queuesql)
    cursor.execute(queuesql)
    print"end update()"
    db.commit()

def try_send_render(ip,folder):
    print("start_try_send_render()")
    # Open database connection
    db = MySQLdb.connect("localhost","root","pepito1234",basededatos)
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    #sql = "SELECT * FROM %s  WHERE job_status = %s " %(tabla,jstatus)
    #Lee jobs Database

    #" WHERE 'job_status' = 'EN_COLA'"
    try:
        #BUSCA JOBS con job_status  en rjob = 'EN PROCESO'
        sql = "SELECT * FROM %s WHERE job_status = '%s' ORDER BY job_priority DESC " % (tabla,rjob)
        print sql
        cursor.execute(sql)
        results = cursor.fetchone()
        print results
        #print(results[3]+str(results))
        if results==None:
            print("NINGUN JOB EN PROCESO")
            #BUSCA JOBS EN COLA
            try:
                print "try search_cola_sql"
                search_cola_sql = "SELECT * FROM %s WHERE job_status = '%s' ORDER BY job_priority DESC, job_n" % (tabla,jstatus)
                print search_cola_sql
                cursor.execute(search_cola_sql)

               # Fetch all the rows in a list of lists.
                results = cursor.fetchone()
                print("try send_render() busca encola  ."+str(results))

                if results==None:
                    print "Ningun job en cola"
                    try:
                        print"try_update_job_done()"
                        update_testif_job_done()
                        #break
                    except:
                        "no se pudo update_job_done()"
                else:
                    print "SIGUIENTE JOB "+str(results[0])
                    sql= "UPDATE %s set job_status = '%s'  WHERE job_n=%d ORDER BY job_priority DESC, job_n " %(tabla,rjob,results[0])
                    cursor.execute(sql)
                    db.commit()

            except:
               print("ERROR CONECCION CON JOBS")
        else:

           print"Job en proceso "+str(results[0])+" del file "+results[1]
           activejob=results[0]
           #BUSCA PRIMER TASK EN STATUS DE LA VARIABLE jstatus LA LISTA DE LA TABLA DEL JOB ACTIVO
           nj_sql="SELECT * FROM job_%s WHERE TASKSTATUS = '%s' " % (results[0],jstatus)
           print(nj_sql)
           cursor.execute(nj_sql)
           #REGRESA PRIMER TASK
           results = cursor.fetchone()
           print(str(results))
           if results==None:
               print("No mas jobs en_cola.")
               finished_job(activejob)
           print"CONVIRTIENDO TASK A STR"
           #SEPARA DATOS DE LA TASK 'EN_COLA'
           TASKNUMBER=int(str(results[0]))
           #print(TASKNUMBER)
           TASKDATE=results[1]
           TASKSCENE=results[2]
           TASKFRAME=int(str(results[3]))
           TASKDIR=results[4]
           TASKBLEND=results[5]
           TASKTIME=(0)
           TASKSTATUS=results[7]
           TASKIP=results[8]
           activeframe=TASKFRAME
           #print("TASKFRAME")

           #Genera taskfilequeue para el cliente
           #print(folder)
           rqfile=folder+'/'+ip+'r'
           print(rqfile)
           cf = open(rqfile, 'w')
           tf=TASKBLEND.split('.')[0]
           #Genera comando para enviar al file de respuesta
           cmd = "sudo /usr/bin/blender -b --enable-autoexec -P /mnt/z/scripts/Mis_def.py  \"%s/%s\" -P /mnt/z/scripts/rformat.py -o \"%s/%s/%s_\" -F  MULTILAYER -x 1 -f %s  " % (TASKDIR,TASKBLEND,workingfolder,TASKSCENE,tf,TASKFRAME)
           #print cmd

           dbdata=''

           dbdata="%s|%s|%s|%s|%s|%s|%s|%s|%s" % (TASKNUMBER,TASKDATE,TASKSCENE,TASKFRAME,TASKDIR,TASKBLEND,TASKTIME,TASKSTATUS,TASKIP)
           #Guarda taskfile para el cliente
           print(dbdata)
           print(cf)
           cf.write(cmd)
           #print cmd
           cf.write("\n"+TASKDIR.split('/')[-1])
           cf.write("\n"+(dbdata))
           print(activejob)
           cf.write("\n"+str(activejob))
           cf.close()
           #Borra taskfile generado por el cliente
           rfile=rqfile.rstrip('r')
           print(rfile)
           os.remove(rfile)
           print"# BORRADO TASK REQ #"

           #print(cmd)
           #print(activeframe)
           #print(activejob)
           db.commit()
           try:
               #uinfo=[activejob+'EN_PROCESO'+activeframe]
               #print[activejob,activeframe,ip]
               print("try_update()")
               update(activejob,rjob,activeframe,ip)
               db.commit()
               print"done_update()"
           except:
               print"no se pudo actualizar la tabla del job activo a ."
           #afile.readline()
           #read_f.close()




    except:
       print "Error: unable to fecth data"

    # disconnect from server
    db.close()




#ip='10.10.10.3'
#Busca requests para
while 1:
    try:
        #Busca task requests del cliente.py en 'folder'
        searchfiles()
        #time.sleep(1)
    except:
        print("ERROR AL BUSCAR WORKERS EN %s" % folder)
