import bpy
print('\n\n###########  START FARM BAKE SCRIPT    ###########\n\n')
context=bpy.context.scene

def join(iterator, seperator):
    it = map(str, iterator)
    seperator = str(seperator)
    string = next(it, '')
    for s in it:
        string += seperator + s
    return string

lmag=context.ms_lightmap_groups[context.ms_lightmap_groups_index].name
print(lmag)

#GET OBJECTS IN TEXTURE ATLAS BAKE GROUPS
bkd_ogroups=[]
bkd_ogroups.append(bpy.data.groups[lmag])

for o in context.objects:
    o.select=False

##GET OBJECTS IN TA-BAKE GROUPS

for bkg in bkd_ogroups:
    for o in bkg.objects:
        print(o)
        o.select=True

bpy.ops.object.bake()
image=bpy.data.images[lmag]
fps=len(bpy.data.filepath.split('/'))-1
fp=bpy.data.filepath.split('/')[:fps]
nfp=join(fp,'/')
coolfilepath=nfp+str(lmag) +"_bake.png"
image.filepath_raw =coolfilepath
image.file_format = 'PNG'
image.save()    