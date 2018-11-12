import bpy
image=bpy.data.images
print('\n\n\n\n\n\n\n')

#################################################################
#  FIXES IMAGE FILEPATHS FOR SERVER CHANGE
#################################################################
ruta_mala='Y:\\ESQUEMA\\iluminacion_link\\2 - E_46 (1-58) -SET\\'
ruta_buena='Y:\\ESQUEMA\\'



for i in range(len(bpy.data.images)-1,-1,-1):
    if image[i].filepath_from_user().startswith(ruta_mala):
        froute=image[i].filepath_from_user().replace(ruta_mala,ruta_buena)
        image[i].filepath=froute
        #print(image[i].name, image[i].source,image[i].filepath_from_user())
        print(image[i].name+' //  ' +image[i].filepath_raw)
        #print(image[i].filepath_from_user())
        
        #image[i].user_clear()
        #bpy.data.images.remove(bpy.data.images[i])