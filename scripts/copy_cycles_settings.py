import bpy

##########################################################################
##### SAVES DICTIONARY WITH CYCLES SETTINGS AND COPIES IT TO OTHER SCENES
##########################################################################

settings = ["progressive","sample_clamp_direct","sample_clamp_indirect","film_exposure","light_sampling_threshold","samples","use_square_samples","diffuse_samples","glossy_samples","transmission_samples","ao_samples","mesh_light_samples","subsurface_samples","volume_samples","max_bounces","min_bounces","diffuse_bounces","glossy_bounces","transmission_bounces","volume_bounces","caustics_reflective","caustics_refractive","blur_glossy","film_exposure"]
settingsr = ["tile_x","tile_y"]
settingscm = ["view_transform","look","exposure","gamma"]
dict = {setc: getattr(bpy.context.scene.cycles, setc) for setc in settings}
dictr = {setr: getattr(bpy.context.scene.render, setr) for setr in settingsr}
dictcm = {setcm : getattr(bpy.context.scene.view_settings, setcm) for setcm in settingscm}
daworld = bpy.context.scene.world
for scene in bpy.data.scenes:
    for setc, val in dict.items():
        setattr(scene.cycles, setc, val)
    for setr, val in dictr.items():
        setattr(scene.render, setr, val)
    for setcm, val in dictcm.items():
        setattr(scene.view_settings, setcm, val)
    scene.world=daworld
