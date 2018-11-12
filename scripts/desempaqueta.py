import bpy
import os
print('\n\n\n\n\n\n\n\n\n\n\n')

################################################
# REMOVES AUTOPACK
################################################

#PARA LAS IMAGENES:
for img in bpy.data.images:
    #SI ESTAN EMPAQUETADAS:
    if img.packed_file:
        #Y SU PATH YA EXISTE:
        if os.path.exists(img.filepath):
            print(img.name  +" ya existe en"+img.filepath+" se utilizara ese archivo.")
            img.unpack(method='USE_ORIGINAL')
        #SI NO EXISTE, CREA LA LOCACION ORIGINAL    
        else:
            print("NO SE ENCONTRO "+img.name+" en "+img.filepath+" se escribira en el directorio.")
            img.unpack(method='WRITE_ORIGINAL')
    else:
        print(img.name+" en "+img.filepath+" no esta empaquetado.")
