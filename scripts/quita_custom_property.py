import bpy
##########################
## REMOVES INDEX CUSTO PROPERTY
##########################
for obj in bpy.data.objects:
    if obj.get('index') is not None:
        del obj['index']