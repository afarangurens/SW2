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
