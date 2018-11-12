####################################################################
#
#   RAMIRO A. DELGADO CORTES
#   PEPITO LA PELICULA 2018 
#   CORRIGE BLENSHAPES ASIGNANDOLOS AL RIG DE LA VARIABLE RIG
#
####################################################################

import bpy

# Escribe el nombre del rig a asignar

rig = 'Venancio.Facial.rig_final'

shapes = bpy.context.object.data.shape_keys

for i in range (len(shapes.animation_data.drivers)):
    n = len(shapes.animation_data.drivers[i].driver.variables.items())
    for j in range (n) :
        shapes.animation_data.drivers[i].driver.variables[j].targets[0].id=bpy.data.objects[rig]