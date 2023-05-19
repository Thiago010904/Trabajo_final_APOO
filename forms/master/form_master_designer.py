from tkinter.font import BOLD
from tkinter import ttk
from forms.login.form_login_designer import FormLoginDesigner
import util.generic as utl
import tkinter as tk


class MasterPanelDesinger:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Página libroteca") 
        self.ventana.geometry("800x500")
        self.ventana.config(bg= "#fcfcfc")
        self.ventana.resizable(width = 0, height = 0)
        self.cupones = 100
        # self.lista = [1,2,3,4,5]
        utl.centrar_ventana(self.ventana, 800, 500)
        


        logo = utl.leer_imagen("./Plantillas/logo.png", (170,170))

        frame_logo = tk.Frame(self.ventana, bd=0, width=200, height=10, relief=tk.SOLID, padx=10, pady=10, bg="#fcfcfc")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#fcfcfc")
        label.place(x=0, y=0, width=150, height=150) 


        frame_form = tk.Frame(self.ventana, bd=0, width=200, height=10, relief=tk.SOLID, padx=10, pady=10, bg="blue")
        frame_form.pack(side= "bottom", expand= tk.YES, fill=tk.BOTH)

        boton1 = tk.Button(frame_form, text= "boton1", font= ("Times", 15, BOLD), bg= "#3a7ff6", bd= 0, fg= "#fff")
        boton1.pack(fill= tk.X, padx= 20, pady= 20)
        # boton1.bind("<Return>", (lambda event: self.verificar()))
         
        ## FRAME PARA LA INFORMACIÓN Y TITULO ##
        frame_form_top = tk.Frame(frame_form,height= 50, bd= 0, relief= tk.SOLID, bg= "black")
        frame_form_top.pack(side= "top", fill= tk.X)

        title = tk.Label(frame_form_top, text= "Bienvenido a la libroteca", font=("Times", 30), fg= "#666a88", bg= "#fcfcfc", pady= 50)
        title.pack(expand= tk.YES, fill= tk.BOTH) 

        titlemenu = tk.Label(frame_form_top, text= "¿Qué deseas hacer?", font=("Times", 20), fg= "#666a88", bg= "#fcfcfc", pady= 10) 
        titlemenu.pack(expand= tk.YES, fill= tk.BOTH)

        titlecupon = tk.Label(frame_form_top, text= f"Tus cupones actuales son de: {self.cupones} ", font=("Times", 15), fg= "#666a88", bg= "#fcfcfc", pady= 5) 
        titlecupon.pack(expand= tk.YES, fill= tk.BOTH)

        self.ventana.mainloop()
    
    
    """
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
    """
