import bpy
############################
## BAKE DYNAMICS SHORTHAIR ##
############################
personaje='papa'

print('\n\nSTART SHORTHAIR DYNAMICS SCRIPT\n\n')
selo=bpy.context.selected_objects

def override(point_cache,object):
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        scene=bpy.context.scene
        blend_sdata=bpy.data

        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'active_object': object,'blend_data':blend_sdata,'scene':scene,'window': window, 'screen': screen, 'area': area,'region':region,'point_cache':point_cache}
                        break
    for o in override:
        print( o+' '+str(override[o]))
    return override

scene=bpy.context.scene

def finder(what,where):
    fw=where.lower()
    if what.lower().find(fw):
        return True
    else:
        return False
papa_meshes=['cpete','cabello.izq','cabello.der']

x=personaje+'_meshes'

for obj in selo:
    if obj.type=='MESH' and obj.name in dict:
        bpy.context.scene.objects.active=obj
        
        ## If object is mesh and has particle systems :
        if len(obj.particle_systems.keys())>0:
            partsystems=len(obj.particle_systems.keys())
            part=obj.particle_systems
            
            ## Looks inside all particle systems in the object
            for ps in range(partsystems):
                print(obj.name+" has part system "+part[ps].name)
                part.active=part[ps]
                print(part.active.point_cache)
                #context={'scene': scene, 'active_object': object,'point_cache':part.active.point_cache}
                #bpy.ops.ptcache.bake(context,bake=True)
                bpy.ops.ptcache.bake(override(part.active.point_cache,obj),bake=True)
                print('baked cache for '+part[ps].name)
                #time.sleep(1)
                #print("point cache done for "+part[ps].name)