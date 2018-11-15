import bpy
from datetime import datetime
###############################################3
#############   ELECTOR.py  ################3
# IF MIN = True DESELECT OBJS THAT WONT HAVE  ##
# '$SIZE' AS MINIMUM VOLUME, ELSE DESELECT OBJS#
# LARGER THAN '$SIZE'.

max=True

size=11

###############################################3

def func(val1,val2):
    if max:
        x=val1>=val2
    else:
        x=val1<=val2
    return x

###############################################3

B1='###############################################3\n'
B2='##############    SELECTOR   ##################3\n\n'
print(B1+B2)
selected_objects=bpy.context.scene.objects

for so in selected_objects:
    
    dims=[]
    
    
    x=so.dimensions[0]
    y=so.dimensions[1]
    z=so.dimensions[2]
    
    xy=x*y
    yz=y*z
    xz=x*z
    
    dims.append(xy)
    dims.append(yz)
    dims.append(xz)
    
    check=0
    
    for x in dims:
        if func(x,size):
            check=check+1
            #print('Value :%d ,min %s check +1'%(x,min))
        else:
            print('check+0')
        
        print('Value :%d ,min %s check +1'%(x,min))
    if check<1 and so.type=='MESH':
        print(" Deselected %s"%so.name)
        so.select=True
    
    print ('    ## object %s , check %d \n'%(so.name,check))
    
now=datetime.now()
print('ENDED AT : %s:%s:%s' %(now.hour,now.minute,now.second))