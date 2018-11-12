import bpy

Mscene=bpy.context.scene

Mrender=bpy.context.scene.render

Rend_settings=Mrender.image_settings

print("CAMBIANDO COLOR DEPTH")

bff='OPEN_EXR_MULTILAYER'

Rend_settings.file_format=bff
Mrender.use_stamp=False
Mscene.cycles.sampling_pattern='CORRELATED_MUTI_JITTER'

Rend_settings.color_depth='16'
os=bpy.context.scene.cycles.samples
#Sampling OVERRIDE
#bpy.context.scene.cycles.samples=3500
#ns=bpy.context.scene.cycles.samples
#print ("OVERRIDING SAMPLING de %s a %s samples." % (os,str(ns)))
ro=['__doc__', '__module__', '__slots__', 'bl_rna', 'cycles','freestyle_settings','name','layers','layers_exclude','layers_zmask','light_override','material_override','rna_type','samples','update_render_passes','use']

plano1=['use_sky','use_pass_z','use_surfaces','use_strand','use_solid','use_pass_combined', 'use_pass_color', 'use_pass_combined', 'use_pass_diffuse', 'use_pass_diffuse_color', 'use_pass_diffuse_direct', 'use_pass_diffuse_indirect', 'use_pass_glossy_color', 'use_pass_glossy_direct', 'use_pass_glossy_indirect', 'use_pass_indirect', 'use_pass_reflection', 'use_pass_refraction',  'use_pass_specular', 'use_pass_subsurface_color', 'use_pass_subsurface_direct','use_pass_subsurface_indirect','use_pass_transmission_color','use_pass_transmission_direct', 'use_pass_transmission_indirect']

objid=['use_pass_combined','use_pass_ao','use_pass_mist','use_pass_normal','use_pass_ambient_occlusion','use_pass_uv','use_pass_vector','use_pass_z','use_solid','use_strand']



for rl in Mrender.layers:
    
    rl.cycles['use_denoising']=0
    
    if rl.name.lower().find('plano')>-1:
        for attr in dir(rl):
            if attr not in plano1:
                if attr not in ro:
                    setattr(rl,attr,False)
            else:
                if attr not in ro:
                    setattr(rl,attr,True)
                    
    if rl.name.lower().find('objid')>-1:
        for attr in dir(rl):
            if attr not in objid:
                if attr not in ro:
                    setattr(rl,attr,False)
            else:
                if attr not in ro:
                    setattr(rl,attr,True)
        
    #if rl.name.find('ObjID'):
        