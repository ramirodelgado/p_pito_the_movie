import bpy
#####################################################
##### IMAGE TYPE CHANGER fROM TIFF TO PNG
#####################################################
x=0
y=0
render=bpy.context.scene.render
xo=render.resolution_x
yo=render.resolution_y
rro=render.resolution_percentage
fo=render.image_settings.file_format
fpo=render.filepath
uoo=render.use_overwrite

#print(str(x)+str('\n')+str(y)+str('\nX Original: ')+str(xo)+str('\nY Original: ')+str(yo))
def log(n):
    print(n)
    texto=bpy.data.texts.new('Imagenes_cambiadas') if not 'Imagenes_cambiadas' in bpy.data.texts else bpy.data.texts['Imagenes_cambiadas']
    texto.write(n+"\n")
    
    
for img in bpy.data.images:
    log('Imagenes')
    
    if img.file_format=='TIFF':
        if hasattr(img.filepath_from_user()):
       
            #cambia resolucion de render settings
            x=img.size[0]
            y=img.size[1]
            render.resolution_x=x
            render.resolution_y=y
            render.resolution_percentage=100
            render.image_settings.file_format='PNG'
            render.filepath=img.filepath_from_user()
            render.antialiasing_samples='16'
            render.use_overwrite=True
            img.name=img.name.replace('tif','png')
            img.save_render(img.filepath_from_user().replace('tif','png'))
            img.filepath=img.filepath.replace('tif','png')
            log('La imagen '+img.name+' en \''+img.filepath +'\' fue cambiada')
        
render.resolution_x=xo
render.resolution_y=yo
render.resolution_percentage=rro
render.image_settings.file_format=fo
render.filepath=fpo
render.use_overwrite=uoo       

bpy.ops.wm.save_mainfile() 
        
        
        
        
