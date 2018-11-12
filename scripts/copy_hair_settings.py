import bpy
#############################################################################
# COPIES PARTICLE SETTINGS FOR ALL SELECTED OBJECTS FROM THE ACTIVE OBJECT
#############################################################################

ao=bpy.context.active_object

settings = ["child_nbr","rendered_child_count","use_strand_primitive","use_hair_bspline","render_step","draw_step","hair_length","roughness_1","roughness_1_size","roughness_endpoint","roughness_end_shape","roughness_2","roughness_2_size","roughness_2_threshold","clump_factor","clump_shape","material_slot","child_radius"]
rw=ao.particle_systems.active.settings['cycles']['root_width']
dict = {setc: getattr(bpy.context.active_object.particle_systems[0].settings, setc) for setc in settings}
currentmat=ao.data.materials[ao.particle_systems.active.settings.material_slot]
radius=ao.particle_systems.active.settings['cycles']['radius_scale']
for obj in bpy.context.selected_objects:
    print(obj.name)
    for ps in obj.particle_systems:
        print(ps.name)
        ps.settings['cycles']['radius_scale']=radius
        ps.settings['cycles']['root_width']=rw
        obj.data.materials[ps.settings.material-1]=currentmat
        for setc, val in dict.items():
            setattr(ps.settings, setc, val)