# Agrega Indices
# Agrega indices a los objetos
# 
# (C) Ramiro Delgado - Modificaciones por Ross Rodriguez
# Pepito la pelicula
# 20141107
# Mod: 20141118

# Uso: 
#      
#      

import bpy
import bgl
import blf

###################################
### ADDS INDEX TO OBJECTS WITHIN CAMERA FRAME OF THE SCENE AND CREATES A LIST WITH THE INDEX NUMBER AND OBJECT NAME
####################################

def log(x):
    print(x)
    texto=bpy.data.texts.new('Indices') if not 'Indices' in bpy.data.texts else bpy.data.texts['Indices']
    texto.write(x+"\n")
    
def setObjectMode():
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            if obj.mode != 'OBJECT':
                print("     Objeto",obj.name)
                if obj.name != "Puerta_Salida":
                    bpy.context.scene.objects.active = obj
                    bpy.ops.object.mode_set()
            

bpy.context.scene['xmin']=0
bpy.context.scene['ymin']=0
bpy.context.scene['xmax']=0
bpy.context.scene['ymax']=0
bpy.context.scene['count']=0

inicio = bpy.context.scene.frame_preview_start if bpy.context.scene.use_preview_range else bpy.context.scene.frame_start
fin = bpy.context.scene.frame_preview_end if bpy.context.scene.use_preview_range else bpy.context.scene.frame_end
marcadores=sorted (marcador.frame for marcador in bpy.context.scene.timeline_markers if (marcador.frame >= inicio and marcador.frame <= fin))

myFrames = []
#print("\n"*10)

if (marcadores[0]!=inicio):
    marcadores= [inicio]+marcadores

for f in range(len(marcadores)):
    if f<len(marcadores)-1:
        if marcadores[f+1]-marcadores[f] > 6:
            myFrames.append(marcadores[f])
            myFrames.append(marcadores[f+1]-3)
        else:
            myFrames.append(marcadores[f])
    else:
        myFrames.append(marcadores[f])

if (marcadores[len(marcadores)-1]<fin):
    myFrames.append(fin)
        
#print (list(myFrames))

def draw_callback_px(self, context):
    #print("mouse points", self.mouse_path[len(self.mouse_path)-1])

    font_id = 0  # XXX, need to find out how best to get this.

    # draw some text
    blf.position(font_id, 15, 30, 0)
    blf.size(font_id, 20, 72)
    blf.draw(font_id, "Mouse " + str(self.mouse_path[len(self.mouse_path)-1]))
    x1=bpy.context.scene['xmin']
    y1=bpy.context.scene['ymin']
    x2=self.mouse_path[len(self.mouse_path)-1][0]
    y2=self.mouse_path[len(self.mouse_path)-1][1]

    # 50% alpha, 2 pixel width line
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glColor4f(0.8, 0.0, 0.8, 0.5)
    bgl.glLineWidth(3)

    if bpy.context.scene['SupIzq']:
        bgl.glBegin(bgl.GL_LINE_STRIP)
        bgl.glVertex2i(x1, y1)
        bgl.glVertex2i(x2, y1)
        bgl.glVertex2i(x2, y2)
        bgl.glVertex2i(x1, y2)
        bgl.glVertex2i(x1, y1)
        bgl.glEnd()

    # restore opengl defaults
    bgl.glLineWidth(1)
    bgl.glDisable(bgl.GL_BLEND)
    bgl.glColor4f(0.0, 0.0, 0.0, 1.0)


class RectangleDrawOperator(bpy.types.Operator):
    """Draw a rectangle with the mouse"""
    bl_idname = "view3d.rectangle_operator"
    bl_label = "Rectangle Operator"

    def modal(self, context, event):
        context.area.tag_redraw()

        if event.type == 'MOUSEMOVE':
            self.mouse_path.append((event.mouse_region_x, event.mouse_region_y))

        elif event.type == 'LEFTMOUSE':
            #bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            #return {'FINISHED'}
            bpy.context.scene['SupIzq']=True
            bpy.context.scene['xmin']=event.mouse_region_x
            bpy.context.scene['ymin']=event.mouse_region_y

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            bpy.context.scene['SupIzq']=False
            bpy.context.scene['xmax']=event.mouse_region_x
            bpy.context.scene['ymax']=event.mouse_region_y
            bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')
            setObjectMode()
            #return {'CANCELLED'}
            return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            # the arguments we pass the the callback
            args = (self, context)
            # Add the region OpenGL drawing callback
            # draw in view space with 'POST_VIEW' and 'PRE_VIEW'
            self._handle = bpy.types.SpaceView3D.draw_handler_add(draw_callback_px, args, 'WINDOW', 'POST_PIXEL')

            self.mouse_path = []
            bpy.context.scene['SupIzq']=False
            bpy.context.scene['xmin']=0
            bpy.context.scene['ymin']=0

            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}

bpy.utils.register_class(RectangleDrawOperator)
    
class Paneldim(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Agregar Indices"
    bl_idname = "panel.dimensiones"
    
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        col.prop(bpy.context.scene, '["count"]', text="Index inicial", slider=False)
        col.separator()
        col.label(text="Dimensiones del render border :")
        box=col.box()
        row=box.row()
        row.label(text='X1='+str(bpy.context.scene['xmin'])+', Y1='+str(bpy.context.scene['ymin']))
        row=box.row()
        row.label(text='X2='+str(bpy.context.scene['xmax'])+', Y2='+str(bpy.context.scene['ymax']))
        col.operator("view3d.rectangle_operator", text="Marcar area", icon='BORDER_RECT')
        col.separator()
        col.separator()
        col.operator("object.view_select", text='Seleccionar', icon='PLAY')
        col.operator("next.marker", text='Ir al siguiente KeyPoint', icon='NEXT_KEYFRAME') 
        #col.operator("prev.frame", text='Ir un Frame Anterior', icon='TRIA_LEFT') 
        #col.operator("end.frame", text='Ir al Ultimo Frame', icon='FF')
        col.separator()
        col.operator("obj.index", text='Agregar Indices', icon='FILE_TICK')
        
class next_marker(bpy.types.Operator):
    bl_idname="next.marker"
    bl_label="Ir a Siguiente KeyPoint"
    
    @classmethod
    def poll(cls, context):
        frame = bpy.context.scene.frame_current
        return (frame < myFrames[len(myFrames)-1])
    
    def execute(self,context):
        #bpy.ops.screen.marker_jump(next=True)
        frame = bpy.context.scene.frame_current
        i = 0
        while i < len(myFrames)-1 and frame >= myFrames[i]:
            i+=1
        #print (frame,myFrames[i])
        bpy.context.scene.frame_current = myFrames[i]
        return{'FINISHED'}        

class prev_frame(bpy.types.Operator):
    bl_idname="prev.frame"
    bl_label="Previous Frame"
    def execute(self,context):
        bpy.context.scene.frame_current-=3
        return{'FINISHED'}
               
class f_end(bpy.types.Operator):
    bl_idname="end.frame"
    bl_label="Go to END"
    def execute(self,context):
        ef=bpy.context.scene.frame_end
        bpy.context.scene.frame_current=ef
        return{'FINISHED'}
          
class ViewSelect(bpy.types.Operator):
    bl_idname = "object.view_select"
    bl_label = "Select view"
    
    def execute(self, context):
        x=bpy.context.area.spaces.active.viewport_shade
        bpy.context.area.spaces.active.viewport_shade="WIREFRAME"
        x1=bpy.context.scene['xmin']
        x2=bpy.context.scene['xmax']
        y1=bpy.context.scene['ymin']
        y2=bpy.context.scene['ymax']
        bpy.ops.view3d.select_border(gesture_mode=3, xmin=x1, xmax=x2, ymin=y1, ymax=y2, extend=True)
        bpy.context.area.spaces.active.viewport_shade=x        
        return {'FINISHED'}
    
class ind(bpy.types.Operator):
    bl_idname="obj.index"
    bl_label="Agregar index"
        
    def execute(self, context):
        log("Nombre Mesh:                           Obj Index:\n")
                
        myObj=[]
        mats={}
        pai=0

        for sobj in bpy.context.selected_objects:
            #print (sobj.name)
            if sobj.type=='MESH':
                #if sobj.get('index') is None:
                 #   sobj['index']=True
                    myObj+=[sobj]
                #else:
                    #sobj.select=False                    
        #print(myObj)
        if len(myObj)>0:
            for obj in myObj:
                index=bpy.context.scene['count']
                obj.pass_index=index
                log(obj.name+" "*(45-len(obj.name))+"%3s"%obj.pass_index)
                index+=1
                bpy.context.scene['count']=index
                
                for psys in obj.particle_systems:
                    if len(obj.material_slots)>0:
                        if str(obj.material_slots[psys.settings.material-1].name)!="":
                            print(str(obj.material_slots[psys.settings.material-1]))
                            print()
                            matp=obj.material_slots[psys.settings.material-1]
                            matp2=bpy.data.materials[matp.name].name
                            if matp2 in mats.keys():
                                print()
                                #log("Ya esta "+matp2+" en la lista.")
                            else:
                                mats[matp2]=bpy.data.materials[matp.name]
                                
            log("\nNombre Material:                        Mat Index:\n")  
            for key in mats.keys():
                mats[key].pass_index=pai
                n=str(mats[key].pass_index)
                pai+=1
                log(mats[key].name+" "*(45-len(mats[key].name))+"%3s"%n)
                
        return{'FINISHED'}
    
bpy.utils.register_class(ind)
bpy.utils.register_class(ViewSelect)
bpy.utils.register_class(Paneldim)
bpy.utils.register_class(f_end)
bpy.utils.register_class(prev_frame)
bpy.utils.register_class(next_marker)