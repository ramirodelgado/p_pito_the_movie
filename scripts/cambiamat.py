import bpy
#######################
prueba=True
#prueba=False
#######################

buscamat='cabello'
enmeshes='cabeza'
mat='CAMBIO'

#######################

selo=bpy.context.selected_objects
if prueba==True:
    
    print('\n\n'+'      EJECUTANDO CAMBIAMAT.PY EN MODO DE PRUEBA'+'\n')
    print('         BUSCANDO material : \''+buscamat+'\'  en objetos llamados : \''+enmeshes+' \', Cambiando por Material: \''+mat+' \'\n')

for o in selo:
    o.select=False
    if o.type=='MESH':
        if o.name.lower().find(enmeshes.lower())>-1:
            print('     '+o.name)
            o.select=True
            for m in o.material_slots:
                if m!=None:
                    if m.material.name.lower().find(buscamat.lower())>-1:
                        print('         '+str(m.material))
                        if prueba==False:
                            m.material=bpy.data.materials[mat]
                        
                    