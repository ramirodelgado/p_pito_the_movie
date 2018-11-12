import bpy

#SELECCIONA OTROS OBJECTOS QUE INICIEN CON MISMO EL NOMBRE 

def reader(word):
    x=(len(word)/3)*2
    return int(x)
    
o=bpy.context.object
o=o.name.split('.')[0]
o=o[:reader(o)]
for MyObj in bpy.data.objects:
    if MyObj.name.startswith(o):
        print(MyObj.name)
        MyObj.select=True
    