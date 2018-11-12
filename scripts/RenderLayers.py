# Render Layers
# Establece lo que se debe renderear para cada layer
# (C) Ramiro Delgado
# Pepito la pelicula
# 20141107

#CREA RENDER LAYERS CON SETTINGS PARA CADA TIPO DE LAYER PERSONAJES; BACKGROUND ; ETC
#
#
import bpy
#from bpy.props import (StringProperty,         BoolProperty,   IntProperty,        FloatProperty,
#                       FloatVectorProperty,    EnumProperty,   PointerProperty)
#from bpy.types import (Panel,                  Operator,       AddonPreferences,   PropertyGroup)
from bpy.props import (IntProperty, EnumProperty, PointerProperty)
from bpy.types import PropertyGroup

def log(x):
    
    print(x)
    texto=bpy.data.texts.new('Log') if not 'Log' in bpy.data.texts else bpy.data.texts['Log']
    texto.write(x+"\n")
    
l=[]

atributos=[ #Para desactivar todos
#Include
  "use_all_z",
  "use_edge_enhance",
  "use_freestyle",
  "use_halo",
  "use_sky",
  "use_solid",
  "use_strand",
  "use_zmask",
  "use_ztransp",
#Passes
  "use_pass_ambient_occlusion",
  "use_pass_color",
  "use_pass_combined",
  "use_pass_diffuse",
  "use_pass_diffuse_color",
  "use_pass_diffuse_direct",
  "use_pass_diffuse_indirect",
  "use_pass_emit",
  "use_pass_environment",
  "use_pass_glossy_color",
  "use_pass_glossy_direct",
  "use_pass_glossy_indirect",
  "use_pass_indirect",
  "use_pass_material_index",
  "use_pass_mist",
  "use_pass_normal",
  "use_pass_object_index",
  "use_pass_reflection",
  "use_pass_refraction",
  "use_pass_shadow",
  "use_pass_specular",
  "use_pass_subsurface_color",
  "use_pass_subsurface_direct",
  "use_pass_subsurface_indirect",
  "use_pass_transmission_color",
  "use_pass_transmission_direct",
  "use_pass_transmission_indirect",
  "use_pass_uv",
  "use_pass_vector",
  "use_pass_z"]

#Atributos para cada grupo
char_attr=[
#Include
  #"use_zmask",
  #"use_all_z",
  "use_solid",
  #"use_ztransp",
  "use_edge_enhance",
  "use_strand",
#Passes
  "use_pass_combined",
  "use_pass_z",
  "use_pass_ambient_occlusion",
  ##############################"use_pass_color",
  "use_pass_diffuse",
  "use_pass_diffuse_color",
  "use_pass_diffuse_direct",
  "use_pass_diffuse_indirect",
  "use_pass_environment",
  #"use_pass_indirect",
  ###"use_pass_normal",
  ###"use_pass_material_index",
  ###"use_pass_object_index",
  ###"use_pass_shadow",
  "use_pass_specular",
  ###"use_pass_uv"
  ###"use_pass_vector",
    ]

bg_attr=[
#Include
  #"use_zmask",
  "use_solid",
  #"use_ztransp",
  "use_edge_enhance",
  ###"use_strand",
#Passes
  "use_pass_combined",
  "use_pass_z",
  ###"use_pass_uv",
  ###"use_pass_object_index",
  ###"use_pass_material_index",
  "use_pass_diffuse",
  "use_pass_specular",
  ###"use_pass_shadow",
  "use_pass_ambient_occlusion",
  "use_pass_environment"
  #"use_pass_indirect"
  ###"use_pass_vector",
  ###"use_pass_normal",
  ###"use_pass_color"
  ]

shadows_attr=[
#Include
  #"use_zmask",
  "use_solid",
  "use_strand",
  "use_ztransp",
#Passes
  "use_pass_combined",
  "use_pass_z",
  "use_pass_object_index",
  "use_pass_material_index",
  "use_pass_shadow",
  "use_pass_environment"]#,"use_pass_indirect"]

globales=[
  "use_solid",
  "use_pass_vector",
  "use_pass_object_index",
  "use_pass_material_index"]

mirror=[
  "use_solid",
  "use_ztransp",
  "use_pass_combined",
  "use_pass_diffuse",
  "use_pass_specular",
  "use_pass_reflection",
  "use_pass_refraction"]

polvo=[
  "use_solid",
  "use_ztransp",
  "use_pass_combined",
  "use_pass_z"]

cielo=[
  "use_solid",
  "use_pass_combined",
  "use_pass_z",  
  "use_pass_color",
  "use_pass_ambient_occlusion"]

auto=[
  "use_solid",
  "use_ztransp",
  "use_pass_combined",
  "use_pass_z",
  "use_pass_vector",
  "use_pass_combined",
  "use_pass_diffuse",
  "use_pass_specular",
  "use_pass_ambient_occlusion",
  "use_pass_environment"]

#Grupos
personajes=[
  "pepito",
  "ladron",
  "maestra",
  "paloma",
  "agente",
  "mama",
  "Borracho",
  "ruben",
  "don",
  "cuquita",
  "func",
  "funcionaria",
  "director",
  "swat",
  "swats",
  "detective",
  "agente",
  "papa",
  "venancio",
  "manolo",
  "clarita",
  "Diego",
  "guardias",
  "Pancho",
  "Memo",
  "Tino",
  "Animales",
  "Secundarios",
  "Extras1er",
  "Extras2do",
  "Extras3er",
  "Extras4o",
  "Extras5o"]

bgs=[
  "fondo",
  "bg",
  "background",
  "b_g",
  "back_ground",
  "back ground",
  "props",
  "esc",
  "escenario",
  "mesa",
  "mesas",
  "silla",
  "cristal",
  "ventana",
  "BicisDentro",
  "BicisFuera",
  "Muro",
  "Troncos Arboles"]
  
backgound_translucent=[
  "follaje arboles",
  "vegetacion"
]

mainCharacters = [
        ('PEP', "Pepito", ""),
        ('DIE', "Diego", ""),
        ('CLA', "Clarita", ""),
        ('MAE', "Maestra", ""),
        ('DIR', "Director", ""),
        ('MEM', "Memo", ""),
        ('PAN', "Pancho", ""),
        ('TIN', "Tino", ""),
        ('AGE', "Agente", ""),
        ('PAP', "Papa", ""),
        ('MAM', "Mama", ""),
        ('BOR', "Borracho", "")
        ]

secCharacters = [
        ('SWA', "Swats", ""),
        ('CUQ', "Cuquita", ""),
        ('FUN', "Funcionaria", ""),
        ('MAN', "Manolo", ""),
        ('VEN', "Venancio", ""),
        ('RUB', "DonRuben", ""),
        ('CHA', "Chango", ""),        
        ('SEC', "Secundarios", ""),
        ('EX1', "Extras1er", ""),
        ('EX2', "Extras2do", ""),
        ('EX3', "Extras3er", ""),
        ('EX4', "Extras4o", ""),
        ('EX5', "Extras5o", ""),
        ('ANI', "Animales", "")
    ]
    
Misc = [
        ('PRP', "Props", ""),
        ('BCK', "Background", ""),
        ('FOA', "Follaje Arboles", ""),
        ('TRA', "Troncos Arboles", ""),
        ('VEG', "Vegetacion", ""),
        ('AUT', "Auto", ""),
        ('MIR', "Mirror", ""),
        ('POL', "Polvo", ""),
        ('CIE', "Domo", "Cielo (Domo)")
    ]

class MyChars(PropertyGroup):
    renderlayer = EnumProperty(
        name="Layer Char:",
        description="Personajes Principales",
        items=mainCharacters,
        default = 'PEP'
        )

class MySec(PropertyGroup):
    renderlayer = EnumProperty(
        name="Layer Char:",
        description="Personajes Secundarios",
        items=secCharacters,
        default = 'SWA'
        )

class MyMisc(PropertyGroup):
    renderlayer = EnumProperty(
        name="Layer Misc:",
        description="Miscelaneos",
        items=Misc,
        default = 'PRP'
        )

def getValue(list,key):
    for l in list:
        if l[0] == key:
            return (l[1])
    return (None)

def getLayer(name):
    for rl in bpy.context.scene.render.layers:
        if rl.name == name:
            return (rl)
    return (None)

class ConfiguraLayers(bpy.types.Operator):
    bl_label="Conf Render Layers"
    bl_idname = "render_layers.config"
    
    def execute(self, context):
        log("\n\n--Render Layers")
        filepath="//shadowsonly.blend"
        rlayers=bpy.context.scene.render.layers
        activeLayers = [False] * 20
        myGlobals = getLayer("Globales")
        if not myGlobals:
            print("no globales")
            bpy.ops.scene.render_layer_add()
            myGlobals = bpy.context.scene.render.layers.active
            myGlobals.name = "Globales"
            
        for rl in rlayers:
            if rl.use:
                if rl.name.lower() != "globales":
                    activeLayers = [(activeLayers[i] or rl.layers[i]) for i in range(20)]
                for attr in atributos:
                    #log("apagando"+attr)
                    setattr(rl,attr,False)
                
                if rl.name.lower() in (nombre.lower() for nombre in bgs): #Backgrounds
                    log(rl.name+" es Background")
                    for attr in bg_attr:
                        setattr(rl,attr,True)
                elif rl.name.lower() in (nombre.lower() for nombre in backgound_translucent): #Backgrounds translucidos
                    log(rl.name+" es backgound_translucent")
                    for attr in bg_attr:
                        setattr(rl,attr,True)
                    setattr(rl,"use_ztransp",True)
                elif rl.name.lower() in (nombre.lower() for nombre in personajes): #Personajes
                    log (rl.name+" es personaje")
                    for attr in char_attr:
                        #log("       ---personaje")
                        setattr(rl,attr,True)
                    if rl.name.lower() == "pepito":
                        setattr(rl,"use_pass_refraction",True)
                        setattr(rl,"use_ztransp",True)
                elif rl.name.lower().find("shadow")>-1 or rl.name.lower().find("sombra")>-1: #Sombras
                    log(rl.name+" es pase de sombras")
                    
                    with bpy.data.libraries.load(filepath) as (data_from, data_to):
                        data_to.materials = ["shadowsOnly"]
                    rl.material_override=bpy.data.materials["shadowsOnly"]
                    for attr in shadows_attr:
                        setattr(rl,attr,True)
                elif rl.name.lower() == "globales":
                    for attr in globales:
                        setattr(rl,attr,True)
                elif rl.name.lower() == "mirror":
                    for attr in mirror:
                        setattr(rl,attr,True)
                elif rl.name.lower() == "polvo":
                    for attr in polvo:
                        setattr(rl,attr,True)
                elif rl.name.lower() == "auto":
                    for attr in auto:
                        setattr(rl,attr,True)
                elif rl.name.lower() == "cielo (domo)":
                    for attr in cielo:
                        setattr(rl,attr,True)
                else:
                    log(rl.name+" es de Todo")
                    rl.use_pass_combined=True
                    rl.use_pass_ambient_occlusion=True
                    rl.use_pass_z=True
                    rl.use_solid=True
                    rl.use_pass_object_index=True
                    #rl.use_ztransp=True
        myGlobals.layers = activeLayers
        bpy.context.scene.layers = activeLayers
        return {"FINISHED"}

class AgregaLayers(bpy.types.Operator):
    bl_label="Agrega Render Layers"
    bl_idname = "render_layers.add"
    
    layerType =  IntProperty()
    
    def execute(self, context):
        scene = context.scene
        print('\n\nTipo:',self.layerType)
        layerType = self.layerType
        if layerType == 1:
            myList=bpy.context.scene.my_layers1
            myEnum = mainCharacters
        elif layerType == 2:
            myList=bpy.context.scene.my_layers2
            myEnum = secCharacters
        else:
            myList=bpy.context.scene.my_layers3
            myEnum = Misc
        sel = myList.renderlayer
        print('sel',sel)
        selected = getValue(myEnum,sel)
        print('selected',selected)
        layers = bpy.context.scene.layers
        print ('layers ',layers)
        
        #Busca o Crear Render Layer
        agrega = True
        myLayer = getLayer(selected)
        if not myLayer:
            bpy.ops.scene.render_layer_add()
            myLayer = bpy.context.scene.render.layers.active
            myLayer.name = selected
            agrega = False
        
        #Configura atributos
        atts = bg_attr if layerType == 3 else char_attr
        for attr in atributos:
            setattr(myLayer,attr,False)
        for attr in atts:
            setattr(myLayer,attr,True)
        if selected == "Pepito":
            setattr(myLayer,"use_pass_refraction",True)
            setattr(myLayer,"use_ztransp",True)
        
        #Layers para renderear
        if agrega:
            myLayer.layers = [(myLayer.layers[i] or layers[i]) for i in range(20)]
        else:
            myLayer.layers = layers
        return {"FINISHED"}

class PanelRenderLayers(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Render Layers"
    bl_idname = "panel.render_layers"

    def draw(self, context):
        scene = context.scene
        mylayers1 = scene.my_layers1
        mylayers2 = scene.my_layers2
        mylayers3 = scene.my_layers3
        
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.prop(mylayers1,"renderlayer", text="")
        row.operator("render_layers.add", text="+Layer Personaje").layerType=1
        row = col.row()
        row.prop(mylayers2,"renderlayer", text="")
        row.operator("render_layers.add", text="+Layer Sec").layerType=2
        row = col.row()
        row.prop(mylayers3,"renderlayer", text="")
        row.operator("render_layers.add", text="+Layer BG").layerType=3
        col.separator()
        col.operator("render_layers.config", text="Configura Layers", icon='RENDER_RESULT')
        
def register():
    bpy.utils.register_module(__name__) #Registra todas las clases
    bpy.types.Scene.my_layers1 = PointerProperty(type=MyChars)
    bpy.types.Scene.my_layers2 = PointerProperty(type=MySec)
    bpy.types.Scene.my_layers3 = PointerProperty(type=MyMisc)

def unregister():
    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.my_layers1
    del bpy.types.Scene.my_layers2
    del bpy.types.Scene.my_layers3

register()