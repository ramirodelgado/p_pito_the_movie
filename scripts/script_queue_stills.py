import bpy
texto=bpy.data.texts.new('queue') if not 'queue' in bpy.data.texts else bpy.data.texts['queue']
filepath=bpy.data.filepath.split('Z:\\_FOTO\\')[1].replace('\\','/')
output=bpy.data.filepath.split('Z:\\_FOTO\\')[1].split('_')[0].split('\\')[1]

texto.write("python '/y/scripts/renderscripts/renderscripts/Queue.py\' '/mnt/z/_FOTO/"+filepath+"'"+" "+str(bpy.context.scene.frame_current)+" "+str(bpy.context.scene.frame_current)+" "+"'STILLS_FOTO'")