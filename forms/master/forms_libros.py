from tkinter.font import BOLD
from tkinter import ttk
import util.generic as utl
import tkinter as tk
from tkinter import messagebox, simpledialog



class FormLibros:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Libros disponibles")
        self.ventana.geometry("800x600")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 700, 400)
        
        self.libros_disponibles = [
            {"titulo": "Necronomicon", "autor": "HP Lovecraft", "precio": 100},
            {"titulo": "Cien años de soledad", "autor": "Gabriel Garcia Marquez", "precio": 15},
            {"titulo": "Don Quijote de la mancha", "autor": "Miguel de Cervantes", "precio": 20},
            {"titulo": "Diario", "autor": "Ana Frank", "precio": 20},
            {"titulo": "El Señor de los Anillos", "autor": "J.R.R Tolkien", "precio": 23},
            {"titulo": "El código Da Vinci", "autor": "Dan Brown", "precio": 30},
            # Agrega más libros aquí
        ]
        
        self.libros_comprados = []
        print(self.libros_comprados)
        self.cupones = 100
       
        # Mostrar la lista de libros disponibles en la ventana
        self.canvas = tk.Canvas(self.ventana, bg="#fcfcfc", width=800, height=400)
        self.canvas.pack()

        self.cupones_label = tk.Label(self.ventana, text=f"Cupones restantes: {self.cupones}")
        self.cupones_label.pack()



        self.actualizar_visualizacion()

        
        self.ventana.mainloop()


    def comprar_libro_seleccionado(self, libro):
            if libro not in self.libros_comprados:
            # Verificar si hay suficientes cupones para comprar el libro
                if self.cupones >= libro['precio']:
                    # Mostrar un cuadro de diálogo para confirmar la compra
                    confirmacion = messagebox.askyesno("Confirmación de compra", f"¿Estás seguro de comprar el libro '{libro['titulo']}'?")
                    if confirmacion:
                        self.ventana.grab_set()  # Capturar la ventana actual en primer plano
                        self.libros_comprados.append(libro) 
                        self.libros_disponibles.remove(libro)
                        self.cupones -= libro['precio']  # Restar el precio del libro a los cupones
                        messagebox.showinfo("Compra exitosa", f"Has comprado el libro '{libro['titulo']} y te quedan {self.cupones} cupones'")
                        self.actualizar_visualizacion()
                        self.ventana.grab_release()  # Liberar el primer plano de la ventana
                elif self.cupones == 0:
                    # Mostrar mensaje de recarga de cupones
                    respuesta = messagebox.askyesno("Recargar cupones", "Ya no tienes cupones ¿Deseas recargar?")
                    if respuesta:
                        cantidad_recarga = simpledialog.askinteger("Recargar cupones", "Ingrese la cantidad de cupones a recargar:")
                        if cantidad_recarga:
                            self.cupones += cantidad_recarga
                            self.actualizar_visualizacion()
                            messagebox.showinfo("Recarga exitosa", f"Se han recargado {cantidad_recarga} cupones. Cupones restantes: {self.cupones}")

                else:
                    messagebox.showinfo("Cupones insuficientes", "No tienes suficientes cupones para comprar este libro.")                 
            else:
                messagebox.showinfo("Libro repetido", f"El libro '{libro['titulo']}' ya ha sido comprado")          
                
    def actualizar_visualizacion(self):
        self.canvas.delete("all")
        x = 10
        y = 10
        num_columnas = 3
        libros_por_fila = num_columnas
        contador = 0

        for libro in self.libros_disponibles:
            libro_frame = tk.Frame(self.canvas, padx=10, pady=10)
            libro_frame.pack(side=tk.LEFT, padx=10)
            
            titulo_label = tk.Label(libro_frame, text=f"Título: {libro['titulo']}")
            titulo_label.pack()
            
            autor_label = tk.Label(libro_frame, text=f"Autor: {libro['autor']}")
            autor_label.pack()
            
            precio_label = tk.Label(libro_frame, text=f"Precio: {libro['precio']}")
            precio_label.pack()
            
            comprar_boton = tk.Button(libro_frame, text="Comprar", command=lambda l=libro: self.comprar_libro_seleccionado(l))
            comprar_boton.pack()

            fila = contador // libros_por_fila
            columna = contador % libros_por_fila
            self.canvas.create_window(x + columna * 220, y + fila * 180, anchor="nw", window=libro_frame)
            contador += 1

    

    