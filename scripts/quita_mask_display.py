import bpy
import re
##########################################
# FAST TOGGLE FOR ALL EYE MASK MODIFIERS
#######################################

t=True
#t=False
f=False

objs=bpy.data.objects
for obj in objs:
    if obj.type=='MESH':
        if re.search('ojo',obj.name.lower()):
            if hasattr(obj,"modifiers"):
                for mod in obj.modifiers:
                    if mod.type=='MASK':
                        mod.show_render=f
                        mod.show_viewport=t
                    
