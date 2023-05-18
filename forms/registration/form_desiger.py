from abc import abstractmethod
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
import tkinter as tk


from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_user
from tkinter import messagebox
import util.encoding_decoding as end_dec


class FormRegisterDesigner:

    ## INICIADOR DE LA PANTALLA ##
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Inicio de sesión")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        self.auth_repository = AuthUserRepository()
        utl.centrar_ventana(self.ventana, 600, 480)

        logo = utl.leer_imagen("./Plantillas/logo.png", (200, 200))

        ## CONTENEDOR LOGO ##
        frame_logo = tk.Frame(self.ventana, bd=0, width=200,
                              relief=tk.SOLID, padx=10, pady=10, bg="#F87474")
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg="#F87474")
        label.place(x=0, y=0, relwidth=1, relheight=1)

        ## CONTENEDOR FORMULARIO ##
        frame_form = tk.Frame(self.ventana, bd=0,
                              relief=tk.SOLID, bg="#fcfcfc")
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        ## CONTENEDOR TITULO ##
        frame_form_top = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg="black")
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Registro de usuario", font=(
            "Times", 30), fg="#666a88", bg="#fcfcfc", pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        ## CONTENEDOR PARA EL FORMULARIO ##
        frame_form_fill = tk.Frame(
            frame_form, height=50, bd=0, relief=tk.SOLID, bg="#fcfcfc")
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        ## CAJA DE TEXTO DE USUARIO Y TITULO USUARIO ##
        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=(
            "Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=("Times", 14))
        self.usuario.pack(fill=tk.X, padx=20, pady=10)

        ## CAJA DE TEXTO DE CONTRASEÑA Y TITULO CONTRASEÑA ##
        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=(
            "Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.password = ttk.Entry(frame_form_fill, font=("Times", 14))
        self.password.pack(fill=tk.X, padx=20, pady=10)
        self.password.config(show="*")

        etiqueta_confirm = tk.Label(frame_form_fill, text="Confirmar contraseña", font=(
            "Times", 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_confirm.pack(fill=tk.X, padx=20, pady=5)
        self.confirmation = ttk.Entry(frame_form_fill, font=("Times", 14))
        self.confirmation.pack(fill=tk.X, padx=20, pady=10)
        self.confirmation.config(show="*")

        ## REGISTRAR ##
        registrar = tk.Button(frame_form_fill, text="Registrar", font=(
            "Times", 15), bg="#F87474", bd=0, fg="#fcfcfc", command=self.register)
        registrar.pack(fill=tk.X, padx=20, pady=20)
        registrar.bind("<Return>", (lambda event: self.register()))

        self.ventana.mainloop()