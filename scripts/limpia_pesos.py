import bpy

## DELETES WEIGHT PAINT GROUP FOR SELECTEd POSE BONE

sbones=bpy.context.selected_pose_bones

aobj=bpy.context.selected_objects[1]

x=[]
rvg=[]
for b in sbones:
    x.append(b.name) 
print(x)

for ovg in aobj.vertex_groups:
    if ovg.name in x:
        print(ovg.name+" ei es")
        
    else:
        rvg.append(ovg)

print('test')

for rv in range(len(rvg)-1,0,-1):
    print(rvg[rv].name)
    aobj.vertex_groups.remove(rvg[rv]) 