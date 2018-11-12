import bpy

# REFRESH DEPENDENCIES

objs=bpy.context.scene.objects

for o in objs:
    if o.type=='MESH':
	if hasattr(o.data,'shape_keys'):
		if hasattr(o.data.shape_keys,'animation_data')==True:
			if hasattr(o.data.shape_keys.animation_data,'drivers'):
                        	print(o.name)
                        	for d in o.data.shape_keys.animation_data.drivers:
					print(d.driver)
					x=d.driver.expression
					d.driver.expression=x
					d.driver.show_debug_info=True
					d.driver.use_self=True                      