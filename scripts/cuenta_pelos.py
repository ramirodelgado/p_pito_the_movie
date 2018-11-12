import bpy

#####################################################
#COUNTS ALL HAIRS THAT ARE GOING TO BE RENDERED
#####################################################

tp=0

for obj in bpy.data.objects:
    for ps in obj.particle_systems:
       x=int(len(ps.particles))*int(ps.settings.rendered_child_count)
       print(x)
       tp=tp+x
   
print(tp)
   