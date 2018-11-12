import bpy
import os
###########################################
##### CREATE AUTOMATIC PLAYBLAST WITHOUT THE GUI
###########################################

myArea=bpy.context.screen.areas[0]
myArea.type='VIEW_3D'
myArea=myArea.spaces[0]
#bpy.context.scene.render.filepath=bpy.data.filepath.split('.')[0].replace('ESQUEMA','AUTOPLAYBLAST')

path=bpy.data.filepath
basename=os.path.basename(path)
fileName, fileExtension = os.path.splitext(basename)
dir = path[:-(len(fileName)+len(fileExtension))]
bpy.context.scene.render.filepath=dir.replace('ESQUEMA','PlayBlast1502')+fileName+"_"



bpy.context.scene.render.resolution_x=2048
bpy.context.scene.render.resolution_y=1024
#bpy.context.scene.render.resolution_percentage=50
bpy.context.scene.render.resolution_percentage=100
bpy.context.scene.render.image_settings.file_format='H264'
bpy.context.scene.render.image_settings.color_mode='RGB'
bpy.context.scene.render.ffmpeg.format='QUICKTIME'
bpy.context.scene.render.use_file_extension=True
bpy.context.scene.render.use_stamp=True
bpy.context.scene.render.use_stamp_time=False
bpy.context.scene.render.use_stamp_date=False
bpy.context.scene.render.use_stamp_render_time=False
bpy.context.scene.render.use_stamp_frame=True
bpy.context.scene.render.use_stamp_scene=False
bpy.context.scene.render.use_stamp_camera=False
bpy.context.scene.render.use_stamp_lens=False
bpy.context.scene.render.use_stamp_filename=True
bpy.context.scene.render.use_stamp_marker=False
bpy.context.scene.render.use_stamp_sequencer_strip=False
bpy.context.scene.render.use_stamp_note=True
bpy.context.scene.render.stamp_note_text="PEPITO La Pelicula"
bpy.context.scene.render.stamp_font_size=22
bpy.context.scene.render.stamp_foreground=[0.0,0.015,0.03,1]
bpy.context.scene.render.stamp_background=[0.9,0.9,0.9,.35]

bpy.context.scene.render.use_overwrite=True


bpy.context.scene.frame_step=1

myArea.show_only_render=True
myArea.use_matcap=True
myArea.matcap_icon='01'
myArea.viewport_shade='SOLID'
myArea.region_3d.view_perspective='CAMERA'
bpy.ops.render.opengl(animation=True ,view_context=True)
exit()
