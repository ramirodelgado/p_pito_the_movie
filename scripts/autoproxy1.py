######################################################################
#CREATES A PROXY RIGGED CHARACTER CLONE OF THE ONE IN THE FIRST LAYER
######################################################################
import bpy 

def log(x):
    print(x)
    texto=bpy.data.texts.new('Log') if not 'Log' in bpy.data.texts else bpy.data.texts['Log']
    texto.write(x+"\n")

name='PAPA'
lm=[] 
layer1=[True]+(19*[False])
layer2=[False,True]+(18*[False])
both=([True]*2)+([False]*18)


#bpy.ops.object.hide_view_clear()    
bpy.ops.object.select_all(action='DESELECT')

log('deseleccionando todo')

#BORRA GRUPOS
log('BORRANDO GRUPOS')

#for g in bpy.data.groups:
#    log(g.name)
#    bpy.data.groups.remove(g)
  
for object in bpy.data.objects:
    if object.type=='ARMATURE':
        log(object.name+' ***  es armature')
        object.layers=both
        object.select=False
        
    elif object.type=='LATTICE':
         log(object.name+' ***  es lattice')
         object.layers=both
         object.select=False
         
    elif object.type=='CURVE':
        log(object.name+' ***  es curva')
        
        object.layers=both
   
        object.select=False
    elif object.name.lower().find('control')>-1:
        object.layers=both
        object.select=False
        
    elif object.name.lower().startswith('wgt'):
         log(object.name+' ***  es widget')
         object.select=False
    elif object.name.lower().startswith('ctrl'):
         log(object.name+' ***  es widget')
         object.select=False
    elif object.name.lower().find('deform')>-1:
         log(object.name+' ***  es Mesh Deform')
         object.layers=both
         object.select=False
    elif object.name.lower().find('cloth')>-1 or object.name.lower().find('caida')>-1  :
        log(object.name+' ***  es Mesh de Cloth')
        object.select=False
         
    else:
        object.select=True
        log(object.name)
 
        
bpy.ops.object.duplicate()
myList=bpy.context.selected_objects
#LOS MUEVE AL LAYER 2
for obj in myList:
    obj.layers=layer2
   
#for obj in bpy.data.objects:
    
    if obj.type=='MESH' and not obj.name.lower().startswith('wgt') and not obj.name.lower().startswith('ctrl') and not obj.name.lower().find('deform')>-1:
        
        if obj.name.lower().find('cabeza')>-1 or obj.name.lower().find('cejas')>-1 :
            log(obj.name+' Encontrada  ****')
            for mod in obj.modifiers:
                if mod.type=='PARTICLE_SYSTEM':
                   log('    *** Encontrado sistema de particulas '+mod.name)
                   obj.modifiers.remove(mod)
                elif mod.type=='SUBSURF':
                    log (obj.name+' Borradas '+mod.type)
                    obj.modifiers.remove(mod)
                   
                    lm.append(mod)
                   
               ### if mod.type=='MASK':
                    ###log('    === Encontrada Mascara '+mod.name)
                    ###Aplica Mascara *** No se uso por que implica un mesh sin shape keys***
            #for n in lm:
            #   log(n)
                    
        else:
            
            bpy.context.scene.objects.active=obj
            print(obj.name)
            if getattr(obj.data,'shape_keys'):
                if getattr(obj.data.shape_keys,'key_blocks'):
                    if len(obj.data.shape_keys.key_blocks)>0:
                        bpy.ops.object.shape_key_add(from_mix=True)
                        new_shape=obj.data.shape_keys.key_blocks.keys()[-1]
                        log('///Mezclando ShapeKeys con valores')
                        
                        while getattr(obj.data,'shape_keys'):
                            if getattr(obj.data.shape_keys,'key_blocks'):
                                bpy.context.active_object.active_shape_key_index=0
                                log('   +++Borrando Shape_key '+bpy.context.active_object.active_shape_key.name)
                                bpy.ops.object.shape_key_remove()
                        
                    
                    
                
            for mod in obj.modifiers:
                
                if mod.type=='COLLISION':
                    log (obj.name+' Borradas '+mod.type)
                    obj.modifiers.remove(mod)
                elif mod.type=='SUBSURF':
                    log (obj.name+' Borradas '+mod.type)
                    obj.modifiers.remove(mod)
               
                elif mod.type=='MASK':
                    bpy.context.scene.objects.active=obj
                    log (obj.name+' Aplicada la '+mod.type)
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
                
                    
            obj.modifiers.new(name='myMod1',type='DECIMATE')
            obj.modifiers.new(name='myMod2',type='DECIMATE')
            obj.modifiers['myMod1'].decimate_type='UNSUBDIV'
            obj.modifiers['myMod1'].iterations=1
            
            obj.modifiers['myMod2'].decimate_type='COLLAPSE'
            obj.modifiers['myMod2'].ratio=.65
            
            
            
           
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier='myMod1')
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier='myMod2')
            
            for mod in obj.modifiers:
                if mod.type=='MESH_DEFORM':
                    mod.precision=6
                    if mod.object.name.lower().find('deform'):
                        bpy.ops.object.meshdeform_bind(modifier=mod.name)
               
            log(obj.name)
            
            
#LISTA DE OBJECTOS DUPLICADOS
            
for nobj in myList:
    bpy.context.scene.objects.active=nobj
    
    print(nobj.name)
    
    #QUITA MATERIALES DEL PROXY
    if len(nobj.material_slots)>0:
        for ms in nobj.material_slots:
            nobj.active_material_index=0
            print('MATERIAL : ***',ms.name)
            bpy.ops.object.material_slot_remove()
    
            
        
bpy.ops.object.select_all(action='DESELECT')

bpy.context.scene.layers=layer1
bpy.ops.object.select_all(action='SELECT')
bpy.ops.group.create(name=name+'_HIGH_POLY')
bpy.ops.object.select_all(action='DESELECT')

bpy.context.scene.layers=layer2
bpy.ops.object.select_all(action='SELECT')
bpy.ops.group.create(name=name+'_LOW_POLY')

        
        
print('\n\n\n\n\n\n')
    