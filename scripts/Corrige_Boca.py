import bpy

########################################
## FIXES TRANSFORM SPACE ERROR ON RIGS
#######################################

grupo = ['Agente.rig','Alma.rig','Borracho.rig','Chango.rig','Clarita.rig','Diego.rig','Director.rig','Maestra.rig','Mama.rig','Memo.rig','Pancho.rig','Papa.rig','Tino.rig',]

for n in bpy.data.objects:
    for y in grupo:
        if n.name == y:
            print(n.name)
            for d in n.animation_data.drivers:
                for v in d.driver.variables:                    
                    for t in v.targets:
                       print(t.transform_space) 
                       t.transform_space = 'TRANSFORM_SPACE'
