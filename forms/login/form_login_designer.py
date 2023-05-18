from tkinter import ttk
from tkinter.font import BOLD
from abc import abstractmethod
import util.generic as utl
import tkinter as tk

class FormLoginDesigner:
    @abstractmethod
    def verificar(self):
        pass
     
    @abstractmethod
    def user_register(self):
        pass


    ## INICIADOR DE LA PANTALLA ##
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesión")
        self.ventana.geometry("800x500")
        self.ventana.config(bg= "#fcfcfc")
        self.ventana.resizable(width= 0, height= 0)
        utl.centrar_ventana(self.ventana, 800, 500)
        

        logo = utl.leer_imagen("./Plantillas/logo.png", (250, 250))

        ## CONTENEDOR LOGO ##
        frame_logo = tk.Frame(self.ventana, bd= 0, width= 300, relief= tk.SOLID, padx= 10, pady= 10, bg= "#dbc5ae")
        frame_logo.pack(side= "left", expand= tk.NO, fill= tk.BOTH)
        label = tk.Label(frame_logo, image= logo, bg= "#dbc5ae")
        label.place(x= 0, y= 0, relwidth= 1, relheight= 1)


        ## CONTENEDOR FORMULARIO ##
        frame_form = tk.Frame(self.ventana, bd= 0, relief= tk.SOLID, bg= "#fcfcfc")
        frame_form.pack(side= "right", expand= tk.YES, fill=tk.BOTH)

        ## CONTENEDOR TITULO ##
        frame_form_top = tk.Frame(frame_form,height= 50, bd= 0, relief= tk.SOLID, bg= "black")
        frame_form_top.pack(side= "top", fill= tk.X)
        title = tk.Label(frame_form_top, text= "Inicio de sesión", font=("Times", 30), fg= "#666a88", bg= "red", pady= 50)
        title.pack(expand= tk.YES, fill= tk.BOTH) 

        ## CONTENEDOR PARA EL FORMULARIO ##
        frame_form_fill = tk.Frame(frame_form, height= 50, bd= 0, relief= tk.SOLID, bg= "#fcfcfc")
        frame_form_fill.pack(side= "bottom", expand= tk.YES, fill= tk.BOTH)

        ## CAJA DE TEXTO DE USUARIO Y TITULO USUARIO ##
        etiqueta_usuario = tk.Label(frame_form_fill, text= "Usuario", font=("Times", 14), fg= "#666a88", bg= "#fcfcfc", anchor= "w")
        etiqueta_usuario.pack(fill= tk.X, padx= 20, pady= 5)
        self.usuario = ttk.Entry(frame_form_fill, font= ("Times", 14))
        self.usuario.pack(fill= tk.X, padx= 20, pady= 10)

        ## CAJA DE TEXTO DE CONTRASEÑA Y TITULO CONTRASEÑA ##
        etiqueta_password = tk.Label(frame_form_fill, text= "Contraseña", font=("Times", 14), fg= "#666a88", bg= "#fcfcfc", anchor= "w")
        etiqueta_password.pack(fill= tk.X, padx= 20, pady= 5)
        self.password = ttk.Entry(frame_form_fill, font= ("Times", 14))
        self.password.pack(fill= tk.X, padx= 20, pady= 10)
        self.password.config(show= "*")

        ## BOTÓN INICIO ##
        inicio = tk.Button(frame_form_fill, text= "Iniciar sesión", font= ("Times", 15, BOLD), bg= "#3a7ff6", bd= 0, fg= "#fff", command= self.verificar)
        inicio.pack(fill= tk.X, padx= 20, pady= 20)
        inicio.bind("<Return>", (lambda event: self.verificar()))

        registrar = tk.Button(frame_form_fill, text= "Registrar usuario", font= (
            "Times", 15), bg= "#fcfcfc", bd= 0, fg= "#3a7ff6", command= self.user_register)
        registrar.pack(fill= tk.X, padx= 20, pady= 20)
        registrar.bind("<Return>", (lambda event: self.user_register()))
        
        self.ventana.mainloop()