
def resultado_modo1(y):
    global generar_aleatorio
    global numero
    if generar_aleatorio==0:
        print("entre una vez")
        z=1
        numero = [0,1,2,3]
        while z==1 :
            x=0
            while x<4 :
                numero[x]=random.randint(0, 9)
                x=x+1
            if not(numero[0]==numero[1] or numero[0]==numero[2] or numero[0]==numero[3] or numero[1]==numero[2] or numero[1]==numero[3] or numero[2]==numero[3]):
                z=0
        generar_aleatorio=generar_aleatorio+1
    print(numero)
    picas=0
    fijas=0
    x = [int(a) for a in str(y)] #vuelve el numero una lista                                  
    #print(x) 
    if len(x)==4 and not(x[0]==x[1] or x[0]==x[2] or x[0]==x[3] or x[1]==x[2] or x[1]==x[3] or x[2]==x[3]):#si el numero introducido por la pesona es 4 cifras y no se repite ninguna cifra el programa se ejecuta 
        indice=0
        while indice < 4: # se ejecuta 4 veces de 0 a 3
            item = x[indice]#el item se declara como el numero de la persona en cada posicion
            if item == numero[indice]:# mira si el item es igual al numero y estan en la misma posicion
                fijas=fijas+1#le suma uno a las fijas
            elif item  in numero:# mira si el item es esta en el numero                                   
                picas=picas+1#le suma uno a las picas
            indice += 1#le suma uno al indice
    if fijas==4:
        messagebox.showinfo("Felictaciones", "¡Ganaste en "+str(generar_aleatorio) +" intentos!")
    a="Intento "+str(generar_aleatorio)+" con el Numero "+str(y)+" tiene: "+str(picas)+" picas y "+str(fijas)+" fijas\n"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    generar_aleatorio=generar_aleatorio+1
    return a



