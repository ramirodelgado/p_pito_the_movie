import bpy
##### VIEW/RENDER HAIR/PARTICLES #####
override=False
# OVERRIDE VALLUES IF OVERRIDE==TRUE #

renderval=True
viewval=False

######################################

selo=bpy.context.selected_objects
for obj in selo:
    if obj.type=='MESH':
        if hasattr(obj,"modifiers"):
            for mod in obj.modifiers:
                if mod.type=='PARTICLE_SYSTEM':
                    if mod.show_render==True:
                        mod.name='HAIRTOGGLE'
                    if mod.name=='HAIRTOGGLE':
                        if override:
                            mod.show_render=renderval
                            mod.show_viewport=viewval
                        else:    
                            mod.show_render=not mod.show_render
                            mod.show_viewport=mod.show_render