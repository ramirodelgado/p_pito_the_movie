import bpy
print('\n\n###########  START SCRIPT    ###########\n\n')
context=bpy.context.scene

lmag=context.ms_lightmap_groups[context.ms_lightmap_groups_index].name
print(lmag)

#GET OBJECTS IN TEXTURE ATLAS BAKE GROUPS
bkd_ogroups=[]
bkd_ogroups.append(bpy.data.groups[lmag])

##GET OBJECTS IN TA-BAKE GROUPS

for bkg in bkd_ogroups:
    matspg=[]
    print(bkg)
    for obj in bkg.objects:
        #print (obj)
        for mat in obj.material_slots.keys():
            if mat!='':
                if mat not in matspg:
                    if bpy.data.materials[mat].use_nodes==False:
                        bpy.data.materials[mat].use_nodes=True
                    matspg.append(bpy.data.materials[mat])
    for m in matspg:
        print(m)


        #Clean Old Bake script nodes.
        delete=[]
        
        for n in m.node_tree.nodes:
            if n.name.startswith(lmag):
                delete.append(n)
        for deln in delete:
            m.node_tree.nodes.remove(deln)
        ########################################
        nds=m.node_tree.nodes    
        y=nds.new(type="ShaderNodeUVMap")
        y.name=lmag+"_UV"
        y.uv_map=lmag
        uvoutput=y.outputs[0]

        x=nds.new(type="ShaderNodeTexImage")
        x.name=lmag+"_IMG"
        x.image=bpy.data.images[lmag]
        uvinput=x.inputs[0]
        bakelink=m.node_tree.links.new(uvoutput,uvinput)
        for nodex in m.node_tree.nodes:
            nodex.select=False
        nds.active=x
        #DESELECT
        x.select=True
            
            
        print(m.node_tree.nodes.active.name)
        