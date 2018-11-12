import bpy

###########################################
#
#Escribe el nombre del grupo a borrar
#
###########################################

GrupoaBorrar='Group'
myGroup=GrupoaBorrar

for tg in bpy.data.groups:
    if tg.name==myGroup:
        print('SE BORRO '+tg.name)
        for myO in tg.objects:
            print(myO.name)

        bpy.data.groups.remove(tg)