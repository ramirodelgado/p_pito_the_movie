import bpy
import os
import ctypes.wintypes

#################################################
####### SETUP SUBSTANCE PAINTER SETUP FOR INTERNAL RENDER
#################################################
#Busca "Mis Documentos"

CSIDL_PERSONAL= 5       # My Documents
SHGFP_TYPE_CURRENT= 0   # Want current, not default value

buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf)

md=(buf.value)
cts=0



activeObj=bpy.context.active_object
aOMS=activeObj.material_slots

for ms in aOMS:
    print(ms.name)
    
    
    sp_texturefolder=md+'\Substance Painter\export\\'
    #sp_texturefolder=md+'\Substance Painter\export\\'+ms.name+'\\'
 
   
    if os.path.isdir(sp_texturefolder):
        
        print(sp_texturefolder)
        
        
           

        cts=0
        for ts in ms.material.texture_slots:
            if cts>=14:
                print('mayores')
                ms.material.texture_slots.create(cts)
            cts=cts+1
            
            print(ts)
        if bpy.data.images.find(ms.name+'_Base_Color.png')>-1:
            print('ya existe una imagen llamada '+ms.name+'_Base_Color.png')
        else:
            difi=bpy.data.images.load(sp_texturefolder+ms.name+'_Base_Color.png')
            
        if bpy.data.textures.find(ms.name+'_Base_Color')>-1:
            print('ya existe una textura llamada '+ms.name+'_Base_Color')
        else:
            dift=bpy.data.textures.new(ms.name+'_Base_Color','IMAGE')
            
        
        ms.material.texture_slots[17].texture=dift
        ms.material.texture_slots[17].texture.image=difi
        ms.material.texture_slots[17].texture.image.use_alpha=False
        
         #Normal_OpenGL.png
            
        if bpy.data.images.find(ms.name+'_Normal_OpenGL.png')>-1:
            print('ya existe una imagen llamada '+ms.name+'_Normal_OpenGL.png')
        else:
            difi=bpy.data.images.load(sp_texturefolder+ms.name+'_Normal_OpenGL.png')
            
        if bpy.data.textures.find(ms.name+'_Normal')>-1:
            print('ya existe una textura llamada '+ms.name+'_Normal')
        else:
            dift=bpy.data.textures.new(ms.name+'_Normal','IMAGE')
            
        ms.material.texture_slots[16].texture=dift
        ms.material.texture_slots[16].texture.image=difi
        ms.material.texture_slots[16].texture.image.use_alpha=False
        ms.material.texture_slots[16].use_map_normal=True
        ms.material.texture_slots[16].use_map_color_diffuse=False
        ms.material.texture_slots[16].texture.use_normal_map=True
        ms.material.texture_slots[16].texture.image.colorspace_settings.name='Non-Color'
        
        #HeightMap
        
        if bpy.data.images.find(ms.name+'_Height.png')>-1:
            print('ya existe una imagen llamada '+ms.name+'_Height.png')
        else:
            difi=bpy.data.images.load(sp_texturefolder+ms.name+'_Height.png')
            
        if bpy.data.textures.find(ms.name+'_Height')>-1:
            print('ya existe una textura llamada '+ms.name+'_Height')
        else:
            dift=bpy.data.textures.new(ms.name+'_Height','IMAGE')
            
        ms.material.texture_slots[15].texture=dift
        ms.material.texture_slots[15].texture.image=difi
        ms.material.texture_slots[15].texture.image.use_alpha=False
        ms.material.texture_slots[15].use_map_normal=True
        ms.material.texture_slots[15].use_map_color_diffuse=False
        ms.material.texture_slots[15].texture.image.colorspace_settings.name='Non-Color'
        
        #Roughness
        
        if bpy.data.images.find(ms.name+'_Roughness.png')>-1:
            print('ya existe una imagen llamada '+ms.name+'_Roughness.png')
        else:
            difi=bpy.data.images.load(sp_texturefolder+ms.name+'_Roughness.png')
            
        if bpy.data.textures.find(ms.name+'_Roughness')>-1:
            print('ya existe una textura llamada '+ms.name+'_Roughness')
        else:
            dift=bpy.data.textures.new(ms.name+'_Roughness','IMAGE')
            
        ms.material.texture_slots[14].texture=dift
        ms.material.texture_slots[14].texture.image=difi
        ms.material.texture_slots[14].texture.image.use_alpha=False
        ms.material.texture_slots[14].use_map_color_diffuse=False
        ms.material.texture_slots[14].use_map_color_spec=True
        ms.material.texture_slots[14].use_map_specular=True
        ms.material.texture_slots[14].specular_factor=.05
        ms.material.texture_slots[14].texture.image.colorspace_settings.name='Non-Color'
        
        