import bpy

def SK(V, I, F):    
    if V < 0:
        p = -1
    else:
        p = 1        
    val = 0
    V = abs(V)   
    I = abs(I)
    F = abs(F)
    if V >= I and V <= F:
        val = (V - I) * (1.0/(F - I))
    else:
        val = 1.0    
    val= val * p  
    return val                

def SK_(V, I, M, R, F):
    if V < 0:
        p = -1
    else:
        p = 1        
    val = 0
    V = abs(V)   
    I = abs(I)
    M = abs(M)
    R = abs(R)
    F = abs(F)
    if V >= I and V <= F:
        if V <= M:
            val = (V - I) * (1.0/(M - I))
        else:
            if V >= R:
                val = (1.0 - ((V - R) * (1.0/(F - R))))
            else:
                val = 1.0    
    val= val * p  
    return val                


bpy.app.driver_namespace['SK'] = SK
bpy.app.driver_namespace['SK_'] = SK_

