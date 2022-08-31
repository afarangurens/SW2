global generar_aleatorio
generar_aleatorio=0

def posibles_combinaciones():
    numero = 111
    numeros=[]
    z=0
    while numero<=9876:
        x = [int(a) for a in str(numero)] 
        numeros.append(x)
        if not(len(numeros[z])==4):
            numeros[z].insert(0,0)
        z=z+1
        numero=numero+1
    z=0
    while z+1<len(numeros):
        if not(numeros[z][0]==numeros[z][1] or numeros[z][0]==numeros[z][2] or numeros[z][0]==numeros[z][3] or numeros[z][1]==numeros[z][2] or numeros[z][1]==numeros[z][3] or numeros[z][2]==numeros[z][3]):
            z=z+1     
        else:    
            del numeros[z]
    return numeros

def Validar_es_numero(text,new_text):

    if not(text.isdecimal()):
        return False
    if len(new_text)>0:    
        if int(new_text)>4 or int(new_text)<0:
            return False
    return True
