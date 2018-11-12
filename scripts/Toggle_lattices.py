import bpy
import re

#######################################
##### HIDES ALL LATTICES FOR EASIER ANIMATION
#######################################

t=True
#t=False
f=False
objs=bpy.data.objects
for obj in objs:
    if obj.type=='LATTICE':
        obj.hide=t
        
    if obj.type=='MESH':
        if re.search('def',obj.name.lower()):
            obj.hide=t
