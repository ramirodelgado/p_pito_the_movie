import bpy
import random
objects=bpy.context.scene.objects

#########################################
# ADDS RANDOM COLOR VERTEX COLOR
#########################################

def rnd():
    v=random.random()
    return v

bpy.ops.object.select_all(action='DESELECT')
for obj in objects:
    if obj.type=='MESH':
        obj.select=True
        print(obj.name)
        rcolor=[]
        for c in obj.color:
            rcolor.append(rnd())
        setattr(obj,'color',rcolor)
        if 'random' in obj.data.vertex_colors:
            print('ya')
        else:
            obj.data.vertex_colors.new(name="random")
        for v in obj.data.vertex_colors['random'].data:
            v.color=obj.color[:3]
        
        
        
        obj.select=False
        #obj.color=[r,g,b,a]