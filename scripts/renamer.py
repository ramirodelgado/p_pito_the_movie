import bpy
### MULTIPLE OBJECT RENAMER
# SELECT NEW NAME PREFIX FOR SELECTED OBJECTS

rename='chocolate'

so=bpy.context.selected_objects

for i in range(len(so)):
    print(i)
    nn=rename+'.'+str(i)
    print(nn)
    so[i].name=nn