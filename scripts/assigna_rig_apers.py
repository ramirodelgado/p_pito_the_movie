import bpy
import re

######################################################
#      Seleccionar primero el personaje despues      #
#      el rig del objeto y darle "Run Script"        #
######################################################

robj=bpy.context.active_object
for so in bpy.context.selected_objects:
    if so.name!=robj.name:
        target=so
for b in robj.pose.bones:
    if re.search('copy',b.name):
        for c in b.constraints:
            c.target=target
    