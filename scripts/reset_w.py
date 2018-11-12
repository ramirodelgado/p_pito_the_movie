import bpy

bpy.ops.file.make_paths_relative()

#############################################################################
#   Busca shaders del file color_ids y compara con los materiales en la escena
#   activa, los que no estén los importa y los que ya estan no.
#
#############################################################################

path = 'z:/scripts/shader_ids/color_ids.blend'
mats=[]
y=[]
with bpy.data.libraries.load(path,link=False) as (data_from, data_to):
    #data_to.materials = data_from.materials
    x = data_from.materials
    for yn in bpy.data.materials:
        y.append(yn.name)
    
#    print(x)
#    print(y)
mats=    [i for i in x if i not in y]
for anm in mats:
    bpy.ops.wm.append(directory=path+"\\Material\\", filename=anm)


names=[]
for mn in mats:
    names.append(mn)   
x=[]
y=[]
#############################################################################


s=bpy.context.scene
sr=s.render
sr.resolution_x=2048
sr.resolution_y=1024
sr.resolution_percentage=100
sr.use_stamp=False
s.cycles.samples=1100
s.cycles_curves.primitive=='CURVE_SEGMENTS'
s.cycles_curves.shape=='THICK'
#s.cycles_curves.shape=='RIBBONS'
s.cycles.transparent_min_bounces=16
s.cycles.transparent_max_bounces=32
sr.tile_x=16
sr.tile_y=16
sr.use_border=False
sr.use_compositing=False
sr.use_sequencer=False
############################################################
sr.use_simplify=False
############################################################
#
#    Busca layers co nombres de l alista x en las render layers
#    si no las encuentra las crea.
#
###########################################################
x=['PointPosition','ObjID','plano01']
y=s.render.layers.keys()
missing_renderlayers=    [i for i in x if i not in y]
print(missing_renderlayers)
for n in missing_renderlayers:
    s.render.layers.new(n)
######################################################    
#
#    Asigna pases de cada layer y sus material override
#
#######################################################
for rl in bpy.context.scene.render.layers.keys():
    arl=bpy.context.scene.render.layers[rl]
    if rl=='PointPosition':
       arl.samples=160
       arl.use_ao=False
       arl.use_sky=False
       arl.material_override=bpy.data.materials['point position pass']
       arl.layers=s.render.layers['plano01'].layers
       arl.use_pass_z=False
    if rl=='plano01':
        arl.use_ao=False
        arl.use_pass_uv=True
        arl.use_pass_vector=True
        arl.use_pass_normal=True
        arl.use_pass_z=True
    
        arl.cycles.use_denoising=False
        arl.cycles.denoising_radius=12
        arl.cycles.denoising_relative_pca=False
        
##################################################

#        arl.use_pass_diffuse_direct=False
#        arl.use_pass_diffuse_indirect=False
#        arl.use_pass_diffuse_color=False
#        
#        arl.use_pass_glossy_direct=False
#        arl.use_pass_glossy_indirect=False
#        arl.use_pass_glossy_color=False
#        
#        arl.use_pass_transmission_direct=False
#        arl.use_pass_transmission_indirect=False
#        arl.use_pass_transmission_color=False
#    
#        arl.use_pass_subsurface_direct=False
#        arl.use_pass_subsurface_indirect=False
#        arl.use_pass_subsurface_color=False

##################################################
            
    if rl=='ObjID':
        arl.samples=160
        arl.use_ao=False
        arl.use_sky=False
        arl.use_pass_z=True
        arl.layers=s.render.layers['plano01'].layers
        arl.material_override=bpy.data.materials['Material_ids']
        

#texto=bpy.data.texts.new('queue') if not 'queue' in bpy.data.texts else bpy.data.texts['queue']
#bpy.data.texts['queue'].lines[0].body=' '
#filepath=bpy.data.filepath.split('Z:\\_FOTO\\')[1].replace('\\','/')
#output=bpy.data.filepath.split('Z:\\_FOTO\\')[1].split('_')[0].split('\\')[0]


#texto.write("python '/y/scripts/renderscripts/renderscripts/Queue.py\' '/mnt/z/_FOTO/"+filepath+"'"+" "+str(bpy.context.scene.frame_current)+" "+str(bpy.context.scene.frame_current+1)+" "+output)

#####   STILLS    ####
#texto=bpy.data.texts.new('queue') if not 'queue' in bpy.data.texts else bpy.data.texts['queue']
#filepath=bpy.data.filepath.split('/y2/_FOTO/')[1]
#output=bpy.data.filepath.split('Z:\\_FOTO\\')[1].split('_')[0].split('\\')[1]

#texto.write("python '/mnt/z/scripts/renderscripts/renderscripts/Queuer.py\' '/mnt/z/_FOTO/"+filepath+"'"+" "+str(bpy.context.scene.frame_current)+" "+str(bpy.context.scene.frame_current)+" "+"'STILLS_FOTO'")