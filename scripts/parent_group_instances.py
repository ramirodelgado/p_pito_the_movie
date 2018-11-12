import bpy
import math

children = bpy.context.selected_objects

xs=[]
ys=[]
zs=[]

def avg(x):
    
    avg = sum(x)/len(x)
    
    return avg

def getlocs(obj,index):
    
    locval = obj.location[index]
    
    return locval

for myobj in children:
    
    xs.append(getlocs(myobj,0))
    ys.append(getlocs(myobj,1))
    zs.append(getlocs(myobj,2))

#print(xs)
#print(ys)
#print(zs)

mx = sum(xs)/len(xs)
my = sum(ys)/len(ys)
mz = sum(zs)/len(zs)

#print(mx)
#print(my)
#print(mz)

myloc = [mx,my,mz]

myEmpty=bpy.ops.object.empty_add(type = 'CIRCLE',location = (myloc), rotation = (1.57,0,0))
myEmpty=bpy.context.active_object

for child in children:
    child.select=True

myEmpty.select=True
bpy.ops.object.parent_set(type='OBJECT')

for child in children:
    child.select=False
