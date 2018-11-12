import bpy
import time
print('\n\n###########  START SCRIPT CLEAN EMPTY  ###########\n\n')

context=bpy.context.scene.objects
hide=['LATTICE','ARMATURE','EMPTY','CAMERA']
print('\n\n# OBJ SCANNING PHASE ###########\n\n')
mats=[]
on=0
for obj in context:
    if obj.type=='MESH':
        #print (on)
        k=0
        rms=[]
        for mat in obj.material_slots.keys():
            
            if mat=='':
                print('plop')
                print(obj.name+'_'+str(on)+'_ '+str(k))
                rms.append(k)
            k=k+1
        if len(rms)!=0:
            print('REMOVE'+str(rms))
            
            for r in range(len(rms)):
                bpy.context.scene.objects.active=obj
                obj.active_material_index=rms[r]
                time.sleep(.5)
                bpy.ops.object.material_slot_remove()
                time.sleep(.5)
    on=on+1
print("######## FINISHED CLEANING MATSLOTS ##########")