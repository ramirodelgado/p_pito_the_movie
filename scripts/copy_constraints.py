import bpy
import time
import shutil
import sys
import os
############################################################################
# COPY CONSTRAINT FROM ACTIVE BONE TO SELECTED OBJECT BONE WITH SAME NAME
############################################################################

from os.path import exists

print('=======================\n')
print('\n'+time.ctime()+'\n')
print('=======================\n')
fpl=bpy.data.filepath.split('\\')
fpl.pop(len(fpl)-1)

x='\\'
folder=x.join(fpl)+'\\'
print(folder)
path=folder


pb=bpy.context.active_pose_bone
ao=bpy.context.active_object
so=bpy.context.selected_objects

so.remove(ao)
print(pb)

nb=so[0].pose.bones[pb.name]
print (nb.id_data)

nonmod=['__doc__', '__module__', '__slots__','bl_rna','rna_type','error_location','error_rotation','is_valid']
notwritable=['type']
#nonmod=[]

c_data={}


for constraint in pb.constraints:
    #tipo=constraint.type
    for cs in dir(constraint):
        if cs not in nonmod:
            #print(cs)
            #print(getattr(constraint,cs))
            c_data [cs] = getattr(constraint,cs)

print(c_data)

print('copiar a ')
print(nb)
newconstraint=nb.constraints.new(c_data['type'])

for setting in c_data:
    print(setting)
    print(c_data[setting])
    
    if setting in notwritable:
        print('notwritable')
        
    else:
    
        setattr(newconstraint,setting,c_data[setting])

if not os.path.exists(path):
    print('no existe o no se puede leer el path %s'%path)
else:
    rpath=path+'copy_contraint_tmp'
    fh = open(rpath, 'w')
    fh.write(str(c_data))
    fh.close()