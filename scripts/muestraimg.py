import bpy
image=bpy.data.images
print('\n\n\n\n\n\n\n')
#############################################################
#                                                           #
#  Muestra nombre de imagenes buscando palabras de la ruta  #
#                                                           #
#############################################################
Buscar='home'

for i in image:
	n=i.filepath_from_user().lower().find(Buscar.lower())
	if n!=-1:
		print(i.name)