import bpy
################################################################
####### FIXES IMAGE FILEPATHS FOR INTERNAL BLENDER  (( OLD))
################################################################
def log(x):
    print(x)
    texto=bpy.data.texts.new('Imagenes') if not 'Imagenes' in bpy.data.texts else bpy.data.texts['Imagenes']
    texto.write(x+"\n")
for obj in bpy.data.objects:
   # x=None
    count=0
    for ms in obj.material_slots:
        count+=1
        if ms.name=="":
            #log(obj.name+"notienemat")
            #print(" ------"+obj.name+"no tiene material")
            1==1
        else:
            if ms.material.name!="":
                if hasattr(ms.material.node_tree,"nodes"):
                    #print("tiene nodos el material")
                    for nodo in ms.material.node_tree.nodes:
                        if nodo.type=='MATERIAL_EXT':
                            if hasattr(nodo.material,"texture_slots"):
                                for tsn in nodo.material.texture_slots:
                                    if tsn!=None:
                                        if tsn.name!="":
                                            if tsn.texture.type=='IMAGE':
                                                if tsn.texture.image!=None:
                                                    log("Nombre Obj:    "+str(obj.name)+" --   Nombre Nodo: "+str(nodo.name)+" --   Nombre Material Nodo: "+nodo.material.name+"  --  Nombre Textura: "+tsn.name+" --  Nombre Imagen:" +tsn.texture.image.name+" --  Path imagen: "+tsn.texture.image.filepath)
                elif hasattr(ms.material,"texture_slots"):
                    
                    for ts in ms.material.texture_slots:
                        if ts!=None:
                            if ts==None:
                                print("p22")
                            else:
                                if ms.material.name!="":
                                    if ts.name!="":
                                        if ts.texture.type=='IMAGE':
                                            if ts.texture.image!=None:
                                                if ts.texture.image.name!=None:
                                                    log("Nombre Obj:    "+str(obj.name)+" --   Nombre Material: "+str(ms.material.name)+"  --  Nombre Textura: "+str(ts.name)+" --  Nombre Imagen:" +str(ts.texture.image.name)+" --  Path imagen: "+str(ts.texture.image.filepath))
                                                
                        
                    #log(obj.name+ms.name+" **** no tiene nodos")
print('==================\n\n')                           
#                for ts in ms.material.texture_slots:
#                    if ts!="":
#                        if ts.texture !="":
#                            if ts.texture.type=='IMAGE':
#                                if ts.texture.image!=0:
#                                    log(ts.texture.image)   
#        
        #x="NOTIENEMAT" if ms is None else x is None
#    log(obj.name+"  "+str(count)+"  ")
#        if ms=="":
#            log("no tiene material")
#        if ms.material!="" or ms.material.name!="" or ms is not "":
#            if ms.material.texture_slots!="":
#                for ts in ms.material.texture_slots:
#                    if ts!="":
#                        if ts.texture!="":
#                            if ts.texture.type=='IMAGE':
#                                if ts.texture.image!=0:
#                                    log(ts.texture.image)
#                
#             