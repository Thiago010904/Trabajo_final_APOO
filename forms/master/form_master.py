from tkinter.font import BOLD
from tkinter import ttk
import util.generic as utl
import tkinter as tk

class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Master panel") 
        self.ventana.geometry("800x500")
        self.ventana.config(bg= "#fcfcfc")
        self.ventana.resizable(width = 0, height = 0)
        self.lista = [1,2,3,4,5]
        utl.centrar_ventana(self.ventana, 800, 500)

        logo = utl.leer_imagen("./Plantillas/logo.png", (250, 250))


        label = tk.Label(self.ventana, image = logo, bg = "#3a7ff6")
        label.place(x = 0, y = 0, relwidth= 1, relheight= 1)
                ## CONTENEDOR FORMULARIO ##
        frame_form = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, bg= "#fcfcfc")
        frame_form.pack(side= "right", expand= tk.YES, fill=tk.BOTH)

        registrar = tk.Button(frame_form, text="Registrar", font=(
            "Times", 15), bg="#F87474", bd=0, fg="#fcfcfc", command=self.pepe)
        registrar.pack(fill=tk.X, padx=20, pady=20)
        registrar.bind("<Return>", (lambda event: self.pepe()))
        self.lblpepe = tk.Label(self.ventana)
        self.lblpepe.pack()
        self.ventana.mainloop()


    def pepe(self):
        
        ola = self.lista.pop()
        print(self.lista)
        self.lblpepe.config(text=ola)