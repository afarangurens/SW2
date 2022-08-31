def eliminar_combinaciones(p,f,x,v):
    eliminar=[]
    eliminar.append(v)
    if (f==0 and p==4):
        eliminar2=[]
        for i in x:
            if not(i.count(v[0])==1 and i.count(v[1])==1 and i.count(v[2])==1 and i.count(v[3])==1):
                eliminar.append(i)      
    elif p+f==4:
        for i in x:
            if not(i.count(v[0])==1 and i.count(v[1])==1 and i.count(v[2])==1 and i.count(v[3])==1):
                eliminar.append(i)
    elif p+f==0:
        for i in x:
            if i.count(v[0])==1 or i.count(v[1])==1 or i.count(v[2])==1 or i.count(v[3])==1:
                eliminar.append(i)
    elif f==0:
        for i in x:
            if i[0]==v[0] or i[1]==v[1] or i[2]==v[2] or i[3]==v[3]:
                eliminar.append(i)
    else:
        for i in x:
            if not(i.count(v[0])==1 or i.count(v[1])==1 or i.count(v[2])==1 or i.count(v[3])==1):
                eliminar.append(i)   
    while eliminar.count(v)>1:
        eliminar.remove(v)
    for a in eliminar:
        x.remove(a) 
    eliminar=[]
    if  (f==0 and p==4):
        for i in x:
            if i[0]==v[0] or i[1]==v[1] or i[2]==v[2] or i[3]==v[3]:
                eliminar.append(i)
        while eliminar.count(v)>1:
            eliminar.remove(v)
        for a in eliminar:
            x.remove(a)             
    return x

