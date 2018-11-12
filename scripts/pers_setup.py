import bpy
import re
t=True
f=False

#MUEVE WGTS A LAYER 20 Y LOS BORRA.
prefix=['wgt','ctrl-','ctrl.','R.F.']

bpy.ops.object.select_all(action='DESELECT')
for obj in bpy.data.objects:
    if obj.type=='MESH':
        for x in prefix:
            if obj.name.lower().startswith(x):
                obj.select=True
                print(obj.name)
                for l in range(len(obj.layers)-1,-1,-1):
                    if l==19:
                        obj.layers[l]=True
                    else:
                        obj.layers[l]=False
                    print(l)
                    
bpy.context.scene.layers[19]=True
bpy.ops.object.delete()
bpy.context.scene.layers[19]=True


#DEJA SOLO LAYERS DE HUESOS.
for obj in bpy.data.objects:
    if obj.type=='ARMATURE':
        #checa que sea personaje
        if obj.data.get("rig_id") is not None:
            obj.data['rig_id']='rigui'
            objl=obj.data.layers
            for x in range(0,20):
                if x in[0,2,4,7,9,11,13,23]:
                    objl[x]=True
                else:
                    objl[x]=False
            for bn in obj.pose.bones:
                if bn.get("ikfk_switch") is not None:
                    bn["ikfk_switch"]=1
                    print(bn.name)
                    

objs=bpy.data.objects
for obj in objs:
    if obj.type=='LATTICE':
        obj.hide=t
        for l in range(len(obj.layers)-1,-1,-1):
                    if l==14:
                        obj.layers[l]=True
                    else:
                        obj.layers[l]=False
    if obj.type=='MESH':
        if re.search('def',obj.name.lower()) or re.search('cloth',obj.name.lower()) :
            obj.hide=t
            for l in range(len(obj.layers)-1,-1,-1):
                    if l==14:
                        obj.layers[l]=True
                    else:
                        obj.layers[l]=False
        elif re.search('ojo',obj.name.lower()):
            if hasattr(obj,"modifiers"):
                for mod in obj.modifiers:
                    if mod.type=='MASK':
                        mod.show_render=f
                        mod.show_viewport=f
                    
    