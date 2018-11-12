import bpy
so=bpy.context.selected_objects
for o in so:
    for ms in range(len(o.material_slots)):
        print(ms)
        if o.material_slots[ms].material:
            if o.material_slots[ms].material.name.lower().find('skin')>=0:
                bpy.context.object.active_material_index=ms
                print(o.material_slots[ms].name)
                m=o.material_slots[ms].material
                bpy.data.materials.remove(m,do_unlink=True)
                #break