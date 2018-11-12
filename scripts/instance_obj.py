import bpy
import random

#ADD RANROM ROTATION TO INSTANCES?
rand=True

print('-----')

#GRAB N STORE OBJ DATA FOR INSTANCES

def newempty(on,ol,orm,ore,os,group):
    print(group.name)
    groupname=group.name
    myObjname=on.split('.')[0]
    myEmpty=bpy.ops.object.empty_add(type='PLAIN_AXES',location=(ol))
    bpy.context.active_object.name='INSTANCE_%s'%myObjname
    myEmpty=bpy.context.active_object
    myEmpty.rotation_euler=ore
    myEmpty.rotation_euler[2]=myEmpty.rotation_euler[2]+(random.random()**3)
    myEmpty.scale=os
    myEmpty.dupli_type='GROUP'
    print('doned:type')
    myEmpty.dupli_group=bpy.data.groups[groupname]
    return print('TERMINADO DUPLIGROUP %s del grupo %s' % (myEmpty,groupname))
    
def getdata(o,group):
    
    on=o.name
    ol=o.location
    orm=o.rotation_mode
    ore=o.rotation_euler
    os=o.scale
    ne=newempty(on,ol,orm,ore,os,group)
    
    return print('TERMINADA INSTANCIA DE %s' % on)


def creategroup(o):
    myObjname=o.name.split('.')[0]
    newgroup=bpy.data.groups.new(name=myObjname)
    newgroup.objects.link(bpy.data.objects[myObjname])
    print('creado el grupo %s con el obj %s' %(newgroup,myObjname))
    return newgroup

bpy.context.object.name=bpy.context.object.name.split('.')[0]
group=creategroup(bpy.context.object)
x=bpy.context.object.name.split('.')[0]
print(x)
dontdel=x
delobjs=[]

for obj in bpy.context.selected_objects:
    getdata(obj,group)
    delobjs.append(obj.name)

print('WONTREMOVE:'+x)
delobjs.remove(x)


bpy.data.objects[dontdel].location=[0,0,0]
bpy.data.objects[dontdel].scale=[1,1,1]
print(delobjs)

for deadobj in delobjs:
    print(deadobj)
    bpy.data.objects.remove(bpy.data.objects[deadobj],do_unlink=True)