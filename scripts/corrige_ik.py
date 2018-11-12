import bpy

################################
# FIXES IK TARGET FOR "control" rig object
################################

control=bpy.data.objects['Clarita.rig']
a=bpy.context.active_object

for d in a.animation_data.drivers.data.drivers:
    print(d.driver.type)
    #if d.driver.type
    for v in d.driver.variables:
        print(v.name)
        v.targets[0].id=control
        
        
