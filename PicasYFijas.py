from cProfile import label
from distutils.command.config import config
from email.mime import image
from logging import root
from tkinter import Label, PhotoImage, Toplevel
import tkinter as tk
from tkinter import font
from tkinter.font import BOLD, families
import tkinter.ttk as ttk
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

global generar_aleatorio
generar_aleatorio=0


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


def validar_numero_digitos(text, new_text):
    if len(new_text) > 4:
        return False
    if len(new_text) == 2:
        if new_text[0] == new_text[1]:
            return False
    if len(new_text) == 3:
        if new_text[0] == new_text[2] or new_text[1] == new_text[2]:
            return False
    if len(new_text) == 4:
        if (new_text[0] == new_text[3] or
           new_text[1] == new_text[3] or new_text[2] == new_text[3]):
            return False
    return text.isdecimal()


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


def historico():
    webbrowser.open("Resultados_picas_y_fijas.txt")


class App1(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        global result
        global entry
        window_height=500
        window_width=800
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        center_x=int(screen_width/2-window_width/2)
        center_y=int(screen_height/2-window_height/2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.title("Picas y fijas - Computador vs Jugador")

        label = ttk.Label(self,text="\n\nIngrese 4 digitos diferentes y oprima jugar")
        label.pack()

        entry = ttk.Entry(self, justify=tk.CENTER, font=font.Font(family="Courier",size=12,weight=font.BOLD),validate="key",validatecommand=(self.register(validar_numero_digitos),"%S","%P"))
        entry.pack()

        button = ttk.Button(self,text="Jugar", command=modo1)
        button.pack()

        result_label = ttk.Label(self,text="Resultado")
        result_label.pack()

        result = tk.Text(self,height=15, width=70,font=('Courier',12,BOLD))
        result["state"]="disable"
        result.pack()
        ttk.Button(self,
                text='Cerrar',
                command=self.destroy).pack()

"""
class App2(tk.Toplevel):

    def __init__(self, parent):
        global archivo
        archivo = open("Resultados_picas_y_fijas.txt ", 'w')
        archivo.write("Historico\n")
        archivo.close()
        global Valor_computador
        global contadormodo2
        contadormodo2 = 1
        global numero_entry
        global picas_entry
        global fijas_entry
        global numeros
        numeros = posibles_combinaciones()


        super().__init__(parent)
        global result
        global entry


        window_height = 400
        window_width = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


        self.title("Picas y fijas - Jugador vs Computador")


        label = ttk.Label(self,
                          text="\n\n\nIngrese el numero de picas y de fijas\n que tiene el numero de la computadora\n")
        label.grid(row=0, column=0, columnspan=2, sticky='ew')


        Valor_computador = numeros[random.randint(0, len(numeros) - 1)]

        numero_label = ttk.Label(self, text="Numero computador\n")
        numero_entry = ttk.Entry(self, justify=tk.CENTER, font=font.Font(family="Courier", size=12, weight=font.BOLD))
        picas_label = ttk.Label(self, text="Picas\n")


        picas_entry = ttk.Entry(self, justify=tk.CENTER, font=font.Font(family="Courier", size=12, weight=font.BOLD),
                                validate="key", validatecommand=(self.register(Validar_es_numero), "%S", "%P"))
        fijas_label = ttk.Label(self, text="Fijas\n")
        fijas_entry = ttk.Entry(self, justify=tk.CENTER, font=font.Font(family="Courier", size=12, weight=font.BOLD),
                                validate="key", validatecommand=(self.register(Validar_es_numero), "%S", "%P"))


        numero_entry.delete(0, tk.END)
        numero_entry.insert(0, Valor_computador)
        numero_entry.configure(state="disabled")

        numero_label.grid(row=1, column=0)
        numero_entry.grid(row=1, column=1)
        picas_label.grid(row=2, column=0)
        picas_entry.grid(row=2, column=1)
        fijas_label.grid(row=3, column=0)
        fijas_entry.grid(row=3, column=1)
        mostrar_lista()
        button = ttk.Button(self, text="Validar", command=modo2)
        button.grid(row=4, column=0, sticky='we')

        ttk.Button(self,
                   text='Ver Intentos',
                   command=historico).grid(row=4, column=1, sticky='we')

        ttk.Button(self,
                   text='Cerrar',
                   command=self.destroy).grid(row=5, column=0, columnspan=2)
"""

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        window_height=400
        window_width=300
        screen_width=self.winfo_screenwidth()
        screen_height=self.winfo_screenheight()
        center_x=int(screen_width/2-window_width/2)
        center_y=int(screen_height/2-window_height/2)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        """
        load=Image.open("logo.gif")
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.pack()
        """
        self.st = ttk.Style(self)
        self.st.configure("TButton", font=('Courier Neew',16, "bold"),foreground="#900C3F")
        self.s = ttk.Style(self)
        self.s.configure("TLabel", font=('Courier New',12, "bold"),foreground="#0008FF")

        ttk.Button(self, text='Computador vs Jugador', command=self.open_app1).pack()

        ttk.Button(self,
            text='Jugador vs Computador',
            command=self.open_app2).pack()
        ttk.Button(self,
            text='Cerrar',
            command=self.destroy).pack()

    def open_app1(self):
        app = App1(self)
        app.grab_set()

    def open_app2(self):
        app = App2(self)
        app.grab_set()


if __name__ == "__main__":
    main = Main()
    main.mainloop()

