import bpy
import re 

print('start')
context=bpy.context
obj=context.object
for b in obj.pose.bones:
    bn=b.name
    if b.custom_shape!=None:
        cs=b.custom_shape
        print(b.name+' has '+cs.name)
        #if cs.library!=None:
        #print('has '+cs.library+' as library.')
        if cs.name.split('.')[-1].isdecimal()==True:
            #print('termina en numero')
            sn=cs.name.split('.')
            sn=sn[:len(sn)-1]
            x=str("")
            ncs=[]
            for s in sn:
                x=str(x+'.'+s)
                #print(s)
                #print(x)
            ncs=x[1:]
            bncs=x[1]
            print(bn.lower())
            if bn.lower().startswith('sq'):
                print('si')
                ncs=ncs+'.007'
            elif b.name.lower().startswith('cachete.l'):
                print('cacheteL')
                ncs=ncs+'.000'
            elif b.name.lower().startswith('cachete.r'):
                print('cacheteR')
                ncs=ncs+'.001'
                
                
            #if ncs.endswith('.'):
                #ncs=ncs[:-1]
                #print('removiendo punto')
            elif cs.name.find('inf'):
                ncs=ncs+'.000'
            
            #if b.name.lower().startswith('cachete'):
                
            else:
                ncs=ncs+'.000'
            print('corregido \''+str(ncs)+"\'")
            #print("Cambiando")
            b.custom_shape=bpy.data.objects[ncs]
            
    else:
        print(b.name+' no tiene.')
        
    