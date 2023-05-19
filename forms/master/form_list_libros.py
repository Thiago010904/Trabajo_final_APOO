from tkinter.font import BOLD
from tkinter import ttk
import util.generic as utl
import tkinter as tk
from tkinter import messagebox, simpledialog



class ListLibros:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Lista de libros")
        self.ventana.geometry("800x600")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 400)