#!/bin/bash

 
#echo 'instalando mc'

#sudo apt-get install mc
#echo 'listo'
#echo 'borrando blender instalado'
#sudo apt-get purge blender
#echo 'listo'
echo 'borrando blender de opt'
sudo rm -rf /opt/blender
echo 'listo'
#echo 'borrando blender de /usr/bin'
#sudo rm -rf /usr/bin/blender
echo 'listo'
echo 'copiando nuevo blender a /opt'
sudo cp -rf /mnt/y/blender/ /opt
echo 'listo'

sudo ln -f -s /opt/blender/blender /usr/bin/blender
