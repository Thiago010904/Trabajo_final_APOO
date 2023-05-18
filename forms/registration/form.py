
from forms.registration.form_desiger import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_user
from tkinter import messagebox
import util.encoding_decoding as end_dec
import tkinter as tk


class FormRegister(FormRegisterDesigner):

    def __init__(self):
        self.auth_repository = AuthUserRepository()
        super().__init__()

    def register(self):
        user = Auth_user()
        user_db: Auth_user = self.auth_repository.get_user_by_username(
                self.usuario.get())
        if (self.is_confirmation_password()): 
            user.username = self.usuario.get()
            if not(self.is_user_register(user_db)):
                user.password = end_dec.encrypted(self.password.get())
                self.auth_repository.insert_user(user)
                messagebox.showinfo(
                    message="Se registro el usuario correctamente", title="Mensaje")
                self.ventana.destroy()
                

    def is_confirmation_password(self):
        status: bool = True
        if (self.password.get() != self.confirmation.get()):
            status = False
            messagebox.showerror(
                message="La contraseña no coinciden", title="Mensaje error")
            self.password.delete(0, tk.END)
            self.confirmation.delete(0, tk.END)
        return status

    def is_user_register(self, user: Auth_user):
        status: bool = False
        if (user != None):
            status = True
            messagebox.showerror(
                message="El usuario ya existe", title="Mensaje error")
        return status

   