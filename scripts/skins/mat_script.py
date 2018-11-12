import bpy

path = "Z:\scripts\skins\mat_skins.blend"
mats=[]
y=[]
with bpy.data.libraries.load(path,link=False) as (data_from, data_to):
    #data_to.materials = data_from.materials
    x = data_from.materials
    for yn in bpy.data.materials:
        y.append(yn.name)
    
#    print(x)
#    print(y)
mats=    [i for i in x if i not in y]
print(mats)
for anm in mats:
    bpy.ops.wm.append(directory=path+"\\Material\\", filename=anm)


names=[]
for mn in x:
    names.append(mn)   
    
class DropDownExample(bpy.types.Operator) :  
    bl_idname = "mat.dropdown"  
    bl_label = "pepishader"  
    bl_options = {"REGISTER", "UNDO"}  

    def item_cb(self, context):
        return [(m.name, m.name, m.name) for m in bpy.data.materials if m.name in names]  
       
                                       
    matname=bpy.props.EnumProperty(items=item_cb,  
                                         name = "Materials",  
                                         description = "Choose material here")

    def execute(self, context) :  
        print("material name", self.matname)
        assm=bpy.data.materials[self.matname]
        ao=bpy.context.active_object
        if not ao.material_slots.keys():
            bpy.ops.object.material_slot_add()
            
        ao.data.materials[ao.active_material_index]=assm
            

        return {"FINISHED"}  

#def add_to_menu(self, context) :  
#    self.layout.operator("mat.dropdown", icon = "PLUGIN")  

def register() :  
    bpy.utils.register_module(__name__)       
    #bpy.types.VIEW3D_PT_tools_object.append(add_to_menu)   

def unregister() :  
    bpy.utils.unregister_module(__name__)   
    #bpy.types.VIEW3D_PT_tools_object.remove(add_to_menu)   


if __name__ == "__main__" :  
    register() 