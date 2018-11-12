import bpy
t=True
f=False
objs=bpy.context.scene.objects
#objs=bpy.context.selected_objects
for obj in objs:
    if obj.type=='MESH':
        if hasattr(obj,"modifiers"):
            for mod in obj.modifiers:
                if mod.type=='PARTICLE_SYSTEM':
                    if mod.show_render==t:
                        mod.show_viewport=f
                    
