import bpy
t=True
#t=False
f=False
objs=bpy.data.objects
for obj in objs:
    if obj.type=='MESH':
        if hasattr(obj,"modifiers"):
            for mod in obj.modifiers:
                if mod.type=='PARTICLE_SYSTEM':
                    mod.show_render=t
                    mod.show_viewport=f
                    
