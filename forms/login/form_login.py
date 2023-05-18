from tkinter import ttk, messagebox
from tkinter.font import BOLD
from persistence.repository.auth_user_repository import AuthUserRepository
from forms.master.form_master import MasterPanel
from forms.login.form_login_designer import FormLoginDesigner 
from persistence.model import Auth_user
from forms.registration.form import FormRegister
import util.encoding_decoding as end_dec
import util.generic as utl
import tkinter as tk

class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.auth_reposiroty = AuthUserRepository()
        super().__init__()



    def verificar(self):
        user_db: Auth_user = self.auth_reposiroty.get_user_by_username(self.usuario.get())
        if (self.is_user(user_db)):
            self.is_password(self.password.get(), user_db)


    def user_register(self):
        FormRegister().mainloop()


    ## VERIFICADORES DE CREDENCIALES ##
    def is_user(self, user: Auth_user):
        status: bool = True
        if (user == None):
            status = False
            messagebox.showerror( message= "El usuario no existe, por favor registrese", title= "Mensaje")
        return status
    
    def is_password(self, password: str, user: Auth_user):
        b_password = end_dec.decrypt(user.password)
        if (password == b_password):
            self.ventana.destroy()
            MasterPanel()
        elif(password != b_password or user != self.usuario.get()):
            messagebox.showerror( message= "El usuario o contraseña no son validos", title= "Mensaje")

