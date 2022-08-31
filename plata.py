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

    load=Image.open("logo.gif")
    render=ImageTk.PhotoImage(load)
    img=Label(self,image=render)
    img.image=render
    img.pack()

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