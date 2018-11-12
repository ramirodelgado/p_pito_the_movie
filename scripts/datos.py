###############################################
#READ BLENDER DATA FOR RENDER WITHOUT GUI
###############################################
import bpy
print(bpy.context.scene.name)
print(bpy.context.scene.frame_start)
print(bpy.context.scene.frame_end)
bpy.ops.wm.quit_blender()