#!/usr/bin/python

"""
A simple render client
"""

import socket
import fcntl
import struct
import sys
import os
import subprocess
import time
import datetime
import shutil
import re
import commands
from os.path import exists

root_ofolder='/x/Renders'
folder='/mnt/z/scripts/render/workers/'
workingfolder='LOCALRENDERFOLDER'


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def done_job(dj,x,msg,jobtable):
    print"start done_job()"
    print(dj)

    y=time.mktime(time.localtime())

    TM=datetime.timedelta(seconds=y-x)
    print(TM)
    donejob=open(dj,'w')
    donejob.write(str(msg)+'\n')
    donejob.write(str(TM)+'\n')
    print(jobtable)
    donejob.write(str(jobtable))
    donejob.close()
    time.sleep(5)
    print"end done_job()"

def request(ip):
    path=folder
    #print "start request(ip)"
    #print(path)
    if not os.path.exists(path):
        print('no existe o no se puede leer el path %s'%path)
    else:
        #Genera request de task
        #print('PIDIENDO TASK')
        stamp = time.strftime('%d/%m/%Y/ %H:%M:%S', time.localtime(time.time()))
        rpath=path+'/'+ip
        #print("request path %s" %rpath)
        print "Buscando task en %s" % path
        fh = open(rpath, 'w')
        fh.write("%s|%s" % (stamp,ip))
        fh.close()
        time.sleep(5)
        #print("ESCRITO REQUEST %s" % rpath)
    #print "end request(ip)"

def render(ip,rj):

        #print"start render()"
        #print rj
        readjob=open(rj,'r')
        #print(str(readjob.read()))
        x=time.mktime(time.localtime())
        print(x)
        cmd=readjob.readline()
        cmdfolder=readjob.readline()
        orig=readjob.readline()
        jobtable=readjob.readline()
        print(jobtable)

        #Eecuta bash del comando
        exec_cmd = subprocess.call(cmd, shell=True)
        print"############## render terminado  #################"
        ###################
        # COPIA FILES del working folder al
        try:
            results=orig.split('|')
            print(results)
            print"cmd folder %s" % cmdfolder
            print"orig %s " % orig
            print"jobtable %s" % jobtable
            #for r in results:
            #    print(r)
            TASKNUMBER=results[0]
            TASKDATE=results[1]
            #TASKHOUR=results[2]
            TASKSCENE=results[2]
            TASKFRAME=results[3]
            TASKDIR=results[4]
            TASKBLEND=results[5]
            TASKTIME=results[6]
            TASKSTATUS=results[7]
            TASKIP=results[8]
            tf=TASKBLEND.split('.')[0]
            print("TERMINADO TASKSTUFF")
            #CONVIERTE FRAME A 4 DIGITOS
            print"TASKFRAME %s" % TASKFRAME
            TFRAME="%04i" % int(TASKFRAME)
            print(TFRAME)
            #print(workingfolder)
            #print(TASKSCENE)
            print(tf)
            taskdata=[]
            for n in results:
                taskdata.append(n)
            #TASK LOCAL FOLDER
            TFOLDER=cmdfolder[:-1]
            print(TFOLDER)
            #LOCAL HOME FOLDER
            #localroot=os.environ['HOME']
            #data='%s/%s/%s/%s_%s.exr' % (localroot,workingfolder,str(TASKSCENE),str(tf),str(TFRAME))
            data='%s/%s/%s_%s.exr' % (workingfolder,str(TASKSCENE),str(tf),str(TFRAME))

            #data=str(workingfolder)+str(TASKSCENE)+str(tf)+'_'+str(FRAME)+'.exr'
            #print("CORTE")
            #output="%s/%s/%s_%s.exr" % (root_ofolder,TFOLDER,str(tf),str(TFRAME))
            output="%s/%s/%s_%s.exr" % (root_ofolder,TASKSCENE,str(tf),str(TFRAME))
            outputf="%s/%s/" % (root_ofolder,TASKSCENE)


            #print("CORTE")
            print "#############################################################################"
            print('START COPIA %s' % data)
            print('A %s' % output)
            print "#############################################################################"
            #print(nombre)
            #print(nombre2)
            #BUSCA SI EXISTE EL PATH DE OUTPUT EN LA CARPETA SI NO LA CREA
            if not os.path.exists(outputf):
                print"creando el path %s" % outputf
                os.mkdir(outputf)
            else:
                print"si existe el path %s" % outputf
            #INTENTA COPIAR RENDER DE workingfolder a root_ofolder si no existe en el directorio
            shutil.copy(data, outputf)
	    print "#shutil copy"

	    os.remove(data)
            print "#os.remove(data)"

            print"Borrado el file %s" % data
            #print("--$--SENT--$--")

        except EnvironmentError, e:
           print "\n\n#############################################"
           print "\n\n --- FILE NOT SENT TO SERVER: %s\n\n" % e
           print "#############################################"
           sys.exit()
        else:
           print "#############################################"
           print "\n\n --- FILE : %s SENT TO SERVER \n\n" % data
           print "#############################################"
           print "Files sent to server successfully"
           os.remove(rj)
           print "#############################################################################"
           print('END COPIA %s' % data)
           print('A %s' % output)
           print "#############################################################################"

           print "BORRADO DIRECTORIO %s" % workingfolder
           shutil.rmtree(workingfolder)
           #LIMPIA TEMPS SCRIPT DE ROSS
           #print"start clean tmp()"
           path = "/tmp"

           tmpFiles = sorted(os.listdir( path ))
           images = []

           exts = ['.exr', '.jpg', '.png']

           for f in tmpFiles:
              basename=os.path.basename(f)
              fileName, fileExtension = os.path.splitext(basename)
              if fileExtension in exts:
                 images.append(path+"/"+f)

           for img in images:
               print "Removing temporary file: %s" % img
               os.remove(img)
        print("CLEANING TMP FILES tmp()")
        dj=folder+'/'+ip+'d'
        print(dj)
        #print(dj+'##'+str(x)+'##'+str(taskdata))
        #BORRA TASKJOB GENERADO POR SERVER ip+r

        print(jobtable)
        #print("end render(ip)")
        done_job(dj,x,taskdata,jobtable)
        ######################

def file_exists(path):
    checkfile=str(path)
    return_val=exists(checkfile)
    return return_val

def cola():
    rawip=str(commands.getoutput("hostname -I")).split(' ')[0].strip()

    ip=str(rawip).strip()

    trystamp = time.strftime('%d/%m/%Y|%H:%M:%S', time.localtime(time.time()))
    print "\n###########################  %s  ###########################"% ip
    print "######################## %s #########################\n"% trystamp
    #ip=get_ip_address('enp2s0')
    rj=folder+'/'+ip+'r'
    j=folder+'/'+ip
    #print('start cola()')
    try:
        #print'try render'
        #print'Buscando task pendiente'
        if file_exists(rj):
            #SI HAY RENDERTASK
            time.sleep(1)
            print "SI HAY RENDERTASK %s " % rj
            file=render(ip,rj)


    #
        if file_exists(j):
            print'Ya hay un request de task'
            time.sleep(1)
            #print"try request"
        else:
            time.sleep(1)
            file=request(ip)
            print "No Tasks pendientes"
    except:
        print('end cola()')

while 1==1:
    try:
        cola()
        time.sleep(1)
    except:
        print("Esperando al server o no hay mas jobs pendientes.")
