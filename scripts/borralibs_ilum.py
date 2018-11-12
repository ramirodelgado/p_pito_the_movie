import bpy
x=[]

###############################
#### CLEANS ILUMINATION DATA LINKED BY GROUP
###############################

for g in bpy.data.groups:
    if g.library:
        if g.library.filepath.find('iluminacion_link')>-1:
            x.append(g)
print(x)
print('BORRANDO')
for y in x:
    bpy.data.groups.remove(y)
    print(y,' borrado')
        
