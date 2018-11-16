import bpy
import bgl
import blf
from mathutils import Vector
from math import sqrt
from bpy_extras.view3d_utils import location_3d_to_region_2d


def draw_callback_px(self, context):
    bgl.glColor4f(0,1,0.0,0.9)
    bgl.glEnable(bgl.GL_BLEND)
    font_id = 0
    
    so=bpy.context.selected_objects
    v=[]
    vv=[]
    caml=0.125 * sum((Vector(b) for b in bpy.context.scene.camera.bound_box), Vector())
    camw=bpy.context.scene.camera.matrix_world *caml
    objl=bpy.context.active_object
    v.append(camw)
    local_bbox_center = 0.125 * sum((Vector(b) for b in objl.bound_box), Vector())
    #vv.append(local_bbox_center)
    global_bbox_center = objl.matrix_world * local_bbox_center  
    #print(global_bbox_center) 
    v.append(global_bbox_center)
    #for n in range(len(x)-1,-1,1):    
#    for objl in so:
#        vx=[]
#        vy=[]
#        vz=[]
#        local_bbox_center = 0.125 * sum((Vector(b) for b in objl.bound_box), Vector())
#        #vv.append(local_bbox_center)
#        global_bbox_center = objl.matrix_world * local_bbox_center  
#        #print(global_bbox_center) 
#        v.append(global_bbox_center)
#    #for n in range(len(x)-1,-1,1):
    v0=v[0]
    v1=v[1]
    x=(v1[0]-v0[0])**2
    y=(v1[1]-v0[1])**2
    z=(v1[2]-v0[2])**2
    dist=sqrt(x+y+z)    
    dir=v1-v0
    print(dist)
    print(dir)
    
    verts2d = []
    
    
    new2dCo = location_3d_to_region_2d(bpy.context.region, \
                                           bpy.context.space_data.region_3d, \
                                           v[0])
    new2dCo1 = location_3d_to_region_2d(bpy.context.region, \
                                           bpy.context.space_data.region_3d, \
                                           v[1])
    verts2d.append([new2dCo.x,new2dCo.y])
    verts2d.append([new2dCo1.x,new2dCo1.y])
    
    #print(ve)

        
    bgl.glLineWidth(2)
    bgl.glBegin(bgl.GL_LINE_LOOP)

    for x, y in verts2d:
        bgl.glVertex2f(x, y)

    bgl.glEnd()
    bgl.glDisable(bgl.GL_BLEND)
    #restore defaults
    bgl.glLineWidth(1)
    bgl.glColor4f(1, 1, 1, 1.0)
    blf.position(font_id, 15, 30, 0)
    blf.size(font_id, 20, 72)
    
    blf.draw(font_id,"DISTANCIA:"+str(round(dist)) )
    

    return

class ModalDrawOperator(bpy.types.Operator):
    """Draw a line with the mouse"""
    bl_idname = "view3d.modal_operator"
    bl_label = "Mide Dist"

    def modal(self, context, event):
        context.area.tag_redraw()

        #if event.type == 'MOUSEMOVE':
            #self.mouse_path.append((event.mouse_region_x, event.mouse_region_y))

        if event.type == 'LEFTMOUSE':
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            self.mouse_path = []

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}


def register():
    bpy.utils.register_class(ModalDrawOperator)


def unregister():
    bpy.utils.unregister_class(ModalDrawOperator)

if __name__ == "__main__":
    register()
