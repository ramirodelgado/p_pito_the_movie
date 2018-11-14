import bpy
import time

############################################################################
# COPY CONSTRAINTS FROM ACTIVE BONE TO ANOTHER SELECTED OBJECT ARMATURE BONE
# WITH SAME NAME
#
# Ramiro Delgado 2018 Pepito La Pelicula
############################################################################

losconstraints=[]


print('=======================\n')
print('\n'+time.ctime()+'\n')
print('=======================\n')
fpl=bpy.data.filepath.split('\\')
fpl.pop(len(fpl)-1)

x='\\'
folder=x.join(fpl)+'\\'
print(folder)
path=folder


pb=bpy.context.active_pose_bone
ao=bpy.context.active_object
so=bpy.context.selected_objects

so.remove(ao)
print(pb)

nb=so[0].pose.bones[pb.name]
print (nb.id_data)

nonmod=['__doc__', '__module__', '__slots__','bl_rna','rna_type','error_location','error_rotation','is_valid']
notwritable=['type']
#nonmod=[]

for constraint in pb.constraints:
    #tipo=constraint.type
    c_data={}
    for cs in dir(constraint):
        
        if cs not in nonmod:
            #print(cs)
            #print(getattr(constraint,cs))
            c_data [cs] = getattr(constraint,cs)
        
    losconstraints.append(c_data)
        
    

for myc in losconstraints:
    
    print(myc)
    newconsmytraint=nb.constraints.new(myc.get('type'))
    
    for setting in myc:
        print(setting)
        print(myc[setting])
        
        if setting in notwritable:
            print('notwritable')
            
        else:
           setattr(newconsmytraint,setting,myc[setting])