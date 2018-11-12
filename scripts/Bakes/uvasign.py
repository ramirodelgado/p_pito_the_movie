import bpy

print('\n\n###########  START SCRIPT UV-ASSIGN   ###########\n\n')

context=bpy.context.selected_objects
hide=['LATTICE','ARMATURE','EMPTY','CAMERA','CURVE']
print('\n\n# OBJ SCANNING PHASE ###########\n\n')
mats=[]
for obj in context:
	print(obj.name)
	
	if obj.type in hide:
		obj.select=False
		obj.hide=True

	if obj.cycles_visibility.camera==False:
		obj.hide=True
		
	if obj.type=='MESH':
		useduvs=[]
		for uv in obj.data.uv_textures:
			if uv.active_render:
				usethisuv=uv.name
				useduvs.append(usethisuv)
				if not 'uvmap' in obj.keys():
					obj['uvmap']=usethisuv
				
		print(obj.name)
		m=0
		print('\n##START MATERIAL PHASE\n')
		needsuv=['TEX_IMAGE','MAPPING']
		
		for mat in obj.material_slots.keys():
			if mat!='':
				print('MAT: '+mat)
				newmat=bpy.data.materials[mat].copy()
				obj.material_slots[m].material=newmat
				if newmat.use_nodes==False:
					newmat.use_nodes=True
				ndt=newmat.node_tree
				#SCANUVS:
				for nchk in newmat.node_tree.nodes:
					if nchk.type=='UVMAP':
						if nchk.uv_map!='':
							if nchk.uv_map not in useduvs:
								useduvs.append(nchk.uv_map)
						else:
							nchk.uv_map=usethisuv
							
					if nchk.type in needsuv:
						#print(str(n)+" needs uvs")
						for i in nchk.inputs:
							if len(i.links)==0:
								newuvnode=ndt.nodes.new(type="ShaderNodeUVMap")
								newuvnode.name='SCRIPTUV'
								newuvnode.uv_map=usethisuv
								ndt.links.new(i,newuvnode.outputs[0])
							elif nchk.type=='MAPPING':
								for l in i.links:
									if l.from_node.type=='TEX_COORD':
										if l.from_socket.name=='UV':
											newuvnode=ndt.nodes.new(type="ShaderNodeUVMap")
											newuvnode.name='SCRIPTUV'
											newuvnode.uv_map=usethisuv
											ndt.links.new(i,newuvnode.outputs[0])
								
								
				mats.append(newmat)
			m=m+1
			
		#CHECK OBJ PART SYSTEMS FOR USE OF UVS
		
		if obj.particle_systems:
			for ps in obj.particle_systems:
				if len(ps.settings.texture_slots)!=0:
					for texture in ps.settings.texture_slots:
						if hasattr(texture,'uv_layer'):
							if texture.uv_layer!='':
								useduvs.append(texture.uv_layer)
		
		#CHECK UNUSED UVS:
		print('\n# USED UVS')
		print(useduvs)
		notuseduvs=[]
		for uvx in obj.data.uv_textures:
			if uvx.name not in useduvs:
				
				notuseduvs.append(uvx.name)
		print('\n# NOT USED UVS')
		print(notuseduvs)
		for notused_uv in notuseduvs:
			print("REMOVING UV MAP "+ notused_uv)
			obj.data.uv_textures.remove(obj.data.uv_textures[notused_uv])
	