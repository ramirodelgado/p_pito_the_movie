#!/bin/bash

#echo ' Agregando mnt/y a fstab'
#echo "//10.10.10/40/Pepito_Red /mnt/y cifs guest" | sudo tee -a /etc/fstab

echo ' copiando conf'
sudo mount -a
sudo cp -r /mnt/y/config_server/ /home/render/.config/blender/2.77/config/startup.blend

