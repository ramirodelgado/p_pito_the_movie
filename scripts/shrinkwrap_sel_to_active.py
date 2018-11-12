import bpy
###################################################################################
#ASSIGNS SHRINKWRAP MODIFIER ON ALL SELECTED OBJECTS TO WRAP AROUND ACTIVE OBJECT
###################################################################################

objs=bpy.context.scene.objects

def is_local(obj):
    if obj.layers_local_view[0]:
        return True
    else:
        return False
print("""""""""""""""""")    

ao=bpy.context.active_object.id_data
print(ao)
print('############')
so=bpy.context.selected_objects
print(so)
print('############')
selo=so.remove(bpy.data.objects[ao.name])

print(selo)
print('############')

    
for obj in so:
    bpy.ops.object.select_all(action='DESELECT')
    if is_local(obj):
        
        if obj.type=='MESH':
            
            obj.select=True
            bpy.context.scene.objects.active=obj
            if obj.data.users==1:
                print(0)
            else:
                obj.data=obj.data.copy()
            bpy.ops.object.modifier_add(type='SHRINKWRAP')
            
            
            if hasattr(obj,"modifiers"):
                for mod in obj.modifiers:
                    if mod.type=='SHRINKWRAP':
                        mod.target=ao
                        mod.offset=0.005
                        bpy.ops.object.modifier_apply(modifier=mod.name)
                
                    
