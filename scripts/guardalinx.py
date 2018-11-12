#########################################
#CHANGES ABSOLUTE PATHS FOR LINUX
#########################################
import bpy
import os

n=bpy.data.filepath.split('/')
ln=len(bpy.data.filepath.split('/'))-1
name=bpy.data.filepath.split('/')[ln]
nn=name.split('.blend')[0]
if os.path.isdir('/mnt/y/ESQUEMA/personajes/'+nn):
    print('ya existe el path, guardando en /mnt/y/ESQUEMA/personajes/'+nn)
    
else:
    os.mkdir('/mnt/y/ESQUEMA/personajes/'+nn)
    
np='/mnt/y/ESQUEMA/personajes/'+nn+'/'+name
print('guardado en '+np)
bpy.ops.wm.save_as_mainfile(filepath=np)

bpy.ops.file.pack_all()
bpy.ops.file.unpack_all(method='WRITE_LOCAL')
bpy.ops.file.autopack_toggle()
bpy.ops.wm.save_as_mainfile(filepath=np)
