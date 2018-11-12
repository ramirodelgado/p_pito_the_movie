import bpy
import os
import glob

########################################################
## FIXES NODE CONFIGURATION OFFSET WITH EXR IMAGE SEQUENCES AND SETS RESOLUTION
########################################################

# Selecciona un Nodo de Imagen con un exr cargado y genera un setup basico de frames de acuerdo a la seleccion activa.
imgsi=bpy.context.scene.node_tree.nodes.active.image.size
myExr=[]


nodos=bpy.context.scene.node_tree
for nodo in nodos.nodes:
    nodo.select=False
    
#nodos.nodes['Image'].select=True
#bpy.context.scene.node_tree.nodes.active= bpy.context.scene.node_tree.nodes['Image']
fp=nodos.nodes.active.image.filepath
oname=nodos.nodes.active.image.name


folder=fp.split('\\')[(len(fp.split('\\'))-2)]
ruta=fp.split(oname)[0]

#lee folder y busca exr

x=glob.glob(ruta+'/*.exr')
print('folder ='+folder)
foo=nodos.nodes.active.image.name
print(ruta)
#quita extension y num 
foo = ''.join(foo.split())[:-8]
print(foo)

#Separa exr de la secuencia activa
nodos.nodes.active.image.source='SEQUENCE'
for exr in x:
    if exr[:-8].endswith(foo):
        myExr.append(exr)
        
print(myExr)
#Busca primer y ultimo frame de la secuencia:
Exr_a=sorted(myExr)[0]
Exr_b=sorted(myExr)[(len(myExr)-1)]
#Checa orden del primer y ultimo frame
if Exr_a>=Exr_b:
    primerExr=Exr_b
    ultimoExr=Exr_a
    
else:
    primerExr=Exr_a
    ultimoExr=Exr_b
    
print(primerExr[:-9])

primerframe=int(primerExr[len(primerExr)-8:-4])
ultimoframe=int(ultimoExr[len(ultimoExr)-8:-4])
print(primerframe)
print(ultimoframe)
bpy.context.scene.frame_current=primerframe
bpy.context.scene.frame_start=primerframe
bpy.context.scene.frame_end=ultimoframe
nodos.nodes.active.frame_offset=primerframe-1
nodos.nodes.active.frame_start=primerframe
nodos.nodes.active.frame_duration=(ultimoframe-primerframe)
#if 'Viewer' in bpy.context.scene.node_tree.nodes.keys():
   #print("hay viewer")

print('fin')
print('\n\n\n\n\n\n')

bpy.context.scene.render.resolution_x=imgsi[0]
bpy.context.scene.render.resolution_y=imgsi[1]
bpy.context.scene.render.resolution_percentage=100