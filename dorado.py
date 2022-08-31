
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

