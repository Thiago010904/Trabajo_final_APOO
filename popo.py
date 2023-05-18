# Aquí se crea la clase libro
class Libro:
    def __init__(self, titulo, autor, precio, isbn):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.isbn = isbn
    # Se crea un método para ver que libros estan disponibles y su precio
    def libro_dis(self):
        return f"{self.titulo} - {self.autor}  ${self.precio}"


# Se crea la clase Usuario
class Usuario:
    # Se crea el usuario y la contraseña y se agregan los bonos
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        self.saldo_cupones = 1000
        self.libros_comprados = []
        self.nombre_completo = None
        self.edad = None

    # Se crea una función para crear un perfil 
    def crear_perfil(self):
        self.nombre_completo = input("Ingresa Tú nombre completo: ")
        self.edad = int(input("Ingresa tú edad: "))

    # Se crea una función para comprar el libro y se implenta la lógica para descontar los cupones
    def comprar_libro(self, libro):
        if libro in libros_disponibles:
            if self.saldo_cupones >= libro.precio:
                self.libros_comprados.append(libro)
                self.saldo_cupones -= libro.precio
                libros_disponibles.remove(libro)
                print("")
                print(f"{libro.titulo} Comprado con extio")
                print(f"Cupones restantes: {self.saldo_cupones}")
            else:
                print("")
                print("No tienes suficientes cupones para comprar este libro")
                print(f"Cupones restantes: {self.saldo_cupones}")
        else:
            print("")
            print("El libro no esta disponible")
            print(f"Cupones restantes: {self.saldo_cupones}")         

    
    # Aquí se le pide al cliente que ingrese una opción
    def iniciar_sesion():
        while True:
            print("-"*50)
            print("¿Qué desea hacer?")
            print("Opción 1 Iniciar sesión")
            print("Opción 2 Crear nuevo perfil")
            option = input("Ingresa una opción: ")
            print("-"*50)

            if option == "1":
                nombre_usuario = input("Ingrese el nombre de Usuario: ")
                contraseña = input("Ingrese la contraseña: ")

                # Se compara si el usuario que el cliente ingreso coinciden con alguno de la base de datos
                    # sino el sistema le volverá a preguntar al cliente por su usuario y contraseña 
                for usuario in base_datos_usuarios:
                    if usuario.nombre_usuario == nombre_usuario and usuario.contraseña == contraseña:
                        print("-"*50)
                        print("Inicio de sesión exitoso")
                        print("-"*50)
                        return usuario
                print("-"*50)
                print("Nombre de usuario o contraseña incorrectos, por favor ingresar nuevamente")
                print("-"*50)
            elif option == "2":
                nombre_usuario = input("Ingrese un nombre de usuario: ")
                contraseña = input("Ingrese una contraseña: ")
                nuevo_usuario = Usuario(nombre_usuario, contraseña)
                nuevo_usuario.crear_perfil()
                base_datos_usuarios.append(nuevo_usuario)
                print("-"*50)
                print("Perfil creado con exito")

            else:
                print("Opción invalida")
            break




# BASE DE DATOS

base_datos_usuarios = [
    Usuario("usuario1", "contraseña1"), 
    Usuario("usuario2", "contraseña2"), 
    Usuario("usuario3", "contraseña3")

]

libros_disponibles = [
    Libro("Necronomicon","HP Lovecraft", 100, 3343),
    Libro("Cien años de soledad", "Gabriel Garcia Marquez", 50, 4554),
    Libro("Don Quijote de la mancha", "Miguel de Cervantes", 100, 45454),
    Libro("Diario", "Ana Frank", 100, 4488),
    Libro("El Señor de los Anillos", "J.R.R Tolkien", 150, 1234),
    Libro("El código Da Vinci", "Dan Brown", 200, 4532)
]



usuario_actual = Usuario.iniciar_sesion()
# Menú

while True:
    print("-"*50)
    print("¿Qué desea hacer?")
    print("Opción 1 comprar libros")
    print("Opción 2 mostrar libros disponibles")
    print("Opción 3 ver libros comprados")
    print("Opción 4 Cerrar sesión")
    option = input("Ingresa una opcion: ")
    print("-"*50)


    if option == "1":
        titulo_libro = input("Ingrese el titulo del libro que desea comprar: ")
        libro_a_comprar = next((libro for libro in libros_disponibles if libro.titulo.lower() == titulo_libro.lower()), None)
        if libro_a_comprar:
            usuario_actual.comprar_libro(libro_a_comprar)
        else:
            print("El libro no esta disponible en la tienda")

    elif option == "2":
        print("-"*50)
        print("Libros disponibles:")
        for libro in libros_disponibles:
            print(libro.libro_dis())


    elif option == "3":
        if usuario_actual.libros_comprados:
            print("Libros comprados:")
            for libro in usuario_actual.libros_comprados:
                print(f"{libro.titulo} - {libro.autor}")

        else:
            print("No ha comprado nigún libro aún")


    elif option == "4":
        print("Cerrando sesión...")
        print("-"*50)
        break

    else:
        print("Opcion invalida")

# :D
