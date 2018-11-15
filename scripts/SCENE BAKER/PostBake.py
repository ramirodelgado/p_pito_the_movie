import bpy
print('\n\n###########  START SCRIPT POST-BAKE   ###########\n\n')
context=bpy.context.scene

lmag=context.ms_lightmap_groups[context.ms_lightmap_groups_index].name
print("### BAKE GROUP   "+lmag)

#GET OBJECTS IN TEXTURE ATLAS BAKE GROUPS
bkd_ogroups=[]
bkd_ogroups.append(bpy.data.groups[lmag])

##GET OBJECTS IN TA-BAKE GROUPS

for bkg in bkd_ogroups:
    matspg=[]
    #print(bkg)
    for obj in bkg.objects:
        if 'uvmap' in obj.keys():
            obj.data.uv_textures.active=obj.data.uv_textures[obj['uvmap']]
        
        print ("      ##  OBJECT :"+obj.name)
        k=0
        for mat in obj.material_slots.keys():
            
            if mat!='':
                
                nm=bpy.data.materials[mat].copy()
                #print(nm)
                obj.material_slots[k].material=nm
            k=k+1
        
        for mat in obj.material_slots.keys():
            if mat!='':
                matspg.append(bpy.data.materials[mat])
    print ("    ## MATERIALS ##")
    for m in matspg:
        print(m)
        anylastlink=False
        
        for l in m.node_tree.links:
            print("CHECANDO LINKS")
            g=False
            if l.to_node.name.find('Material Output')>-1:  
                
                print("ENCONTRADO MAT OUTPUT LINK")
                
                cooltypes=['BSDF_DIFFUSE','BSDF_GLOSSY','MIX_SHADER','ADD_SHADER']
                if l.from_node.type in cooltypes:
                    lastlink=l
                    linkto=lastlink.to_node
                    linkfrom=lastlink.from_node
                    print(lastlink.to_node)
                    print(lastlink.from_node)
                    if linkfrom.name.startswith('x'+lmag):
                        for oldnode in m.node_tree.links:
                            print(oldnode)
                            if oldnode.to_node.name==lastlink.from_node.name:
                                linkfrom=oldnode.from_node
                                g=True
                                
                    
                    anylastlink=True
                else:
                    print("")
        #Clean Old Bake script nodes.
        ournodes=[]
        originalnodes=[]
        delete=[]
        #split our nodes and original shader nodes
        for n in m.node_tree.nodes:
            if n.name.startswith('x'+lmag):
                #if n.
                delete.append(n)
                
        for n in m.node_tree.nodes:
            
            if n.name.startswith(lmag):
                ournodes.append(n)
            else:
                originalnodes.append(n)
                
        for nd in ournodes:
            print(nd.name)
            if nd.name.endswith('UV'):
                bakeuv=nd
                print('uv')
            if nd.name.endswith('IMG'):
                bakeimg=nd
                print('img')
        
        for u in delete:
            m.node_tree.nodes.remove(u)
                
        anyemi=False
        anylpn=False
        anymix=False        
        for nd in ournodes:
            print(nd.name)
            if nd.name.endswith('UV'):
                bakeuv=nd
                print('uv')
            if nd.name.endswith('IMG'):
                bakeimg=nd
                print('img')
            if nd.name.endswith('LP'):
                lpn=nd
                print('lp')
                print(lpn)
                anylpn=True
            if nd.name.endswith('EMI'):
                emi=nd
                print('emi')
                print(emi)
                anyemi=True
            if nd.name.endswith('MIX'):
                mix=nd
                print('mix')
                print(mix)
                anymix=True
        
        print('\nOur nodes\n')        
        #Our nodes
        print(bakeuv.name)
        print(bakeimg.name)
        
        print('\nOriginal Nodes')
        #Original Nodes
        originalmsn=[]
        
        for on in originalnodes:
            print(on)
            
        # material outputs if none, its skipped for later.
        if anylastlink:
            
            if not anylpn:
                lpn=m.node_tree.nodes.new(type='ShaderNodeLightPath')
                lpn.name='x'+lmag+'_LP'
            else:
                print ('ya existe el nodo lightpad')
            if not anyemi:
                emi=m.node_tree.nodes.new(type='ShaderNodeEmission')
                emi.name='x'+lmag+'_EMI'
            else:
                print ('ya existe el nodo mixshader')
            if not anymix:
                mix=m.node_tree.nodes.new(type='ShaderNodeMixShader')
                mix.name='x'+lmag+'_MIX'
            else:
                print ('ya existe el nodo mixshader')
                
                
            print(mix)
            print(lpn)
            print(bakeuv)
            print(bakeimg)
            #link to lamp
            m.node_tree.links.new(bakeimg.outputs[0],emi.inputs[0])
            m.node_tree.links.new(lpn.outputs[2],mix.inputs[0])
            m.node_tree.links.new(emi.outputs[0],mix.inputs[2])
            #if linkfrom.name.startswith(lmag):
            #    print('dont')
            #else:
            print('penultimo')
            m.node_tree.links.new(mix.outputs[0],linkto.inputs[0])
            #if g==True:
            print('ultimo')    
            m.node_tree.links.new(linkfrom.outputs[0],mix.inputs[1])
            print ("fin MAT")
            
            #m.node_tree.links.remove(lastlink)
                 
            
 
