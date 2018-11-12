import bpy 

x=bpy.data.images

sin_conectar=[]

for imagen in x:
    if imagen.has_data==False:
        print(imagen.name+" "+str(imagen.size[0])+" "+imagen.filepath)
        sin_conectar+=[imagen]
        #imagen.user_clear()
       
        #bpy.data.images.remove(imagen)

#for n in range(len(sin_conectar),-1,-1):
#    print(sin_conectar[n-1])
    
#C:\Users\Windows\Desktop\pepito\ESQUEMA\..\..\..\..\escenas cambio finales reel esc 0 - 10\E_10\E_10 SETEO\folders Esc_10 parte 2\ESC_PARTE 2_FINALES\E10_PARTE 2_F risas de clase 2 entregado\textures\C.UV.Pantalon.Aclarar.png' not found

     
    
    
    