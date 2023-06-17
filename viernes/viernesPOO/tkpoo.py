import tkinter as tk


# Herencia
class MiAplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Aplicación Python POO, PAPIME PE100423')
        self.geometry('300x200')
        self.configure(bg='lightgreen')
        # Composición
        self.widget = Boton(self)
        self.widget.pack()


# otra herencia
class Boton(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='blue')
        # evento
        self.button = tk.Button(self, text="Presioname!!", command=self.saludar_ya, bg='lightblue')
        self.button.pack(pady=20)

    def saludar_ya(self):
        print("¡Hola, mundo!")


app = MiAplicacion()
app.mainloop()