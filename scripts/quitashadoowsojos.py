import bpy

#QUITA SHADOWS PARA BUG DE ANIMADORES EN LOS OJOS

objects=bpy.context.scene.objects

for obj in objects:
    if obj.name.lower().find('ojo')>=0:
        print(obj.name)
        obj.cycles_visibility.shadow=False
    