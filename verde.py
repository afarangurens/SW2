def mostrar_lista():
    archivo = open("Conbinaciones_computador.txt ", 'w')
    archivo.write("Lista de numeros\n")
    contador=0
    for linea in numeros:
        contador=contador+1
        for a in linea:
            archivo.write(str(a))
        archivo.write("\n")
    archivo.write("Total filas: " + str(contador))
    archivo.close()

def modo1():
    result["state"]="normal"
    value = entry.get()
    if len(value)==4:
        result.insert("1.0",resultado_modo1(value))
    result["state"]="disable"


