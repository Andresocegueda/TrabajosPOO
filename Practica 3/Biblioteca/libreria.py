sesion = False
class libro:
    def __init__(self, titulo, autor, descripcion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.descripcion = descripcion
        self.isbn = isbn
        self.disponible = True
    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nDescripción: {self.descripcion}\nISBN: {self.isbn}\nDisponible: {self.disponible}\n\n"
class usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    def __str__(self):
        return f"Nombre: {self.nombre}\nID: {self.id_usuario}\n\n"
class bibliotecario:
    def __init__(self, nombre, id_bibliotecario, contrasena):
        self.nombre = nombre
        self.id_bibliotecario = id_bibliotecario
        self.contrasena = contrasena
    def __str__(self):
        return f"Nombre: {self.nombre}\nID: {self.id_bibliotecario}\n\n"
class admin:
    def __init__(self, nombre, id_admin, contrasena):
        self.nombre = nombre
        self.id_admin = id_admin
        self.contrasena = contrasena
    def __str__(self):
        return f"Nombre: {self.nombre}\nID: {self.id_admin}\n\n"
class biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.bibliotecarios = []
        self.administradores = []
    # ----------------------------------CONTROL DE LIBROS-------------------------------------
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def eliminar_libro(self, libro):
        self.libros.remove(libro)
    def prestar_libro(self, libro, usuario):
        if libro.disponible == True:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            print(f"El libro {libro.titulo} ha sido prestado a {usuario.nombre}")
        else:
            print("El libro no está disponible")
    def recibir_devolucion(self, libro, usuario):
        if libro.disponible == False:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            print(f"El libro {libro.titulo} ha sido devuelto por {usuario.nombre}")
        else:
            print(f"{usuario.nombre} no tiene prestado el libro {libro.titulo}")
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    def buscar_libro_isbn(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None
    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if libro.disponible == True:
                print(libro)
    
    # ---------------------------------CONTROL DE ADMINISTRADORES-----------------------------
    def agregar_admin(self, admin):
        self.administradores.append(admin)
    # ----------------------------------CONTROL DE USUARIOS-------------------------------------
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} agregado") 
    def eliminar_usuario(self, usuario):
        print(f"Se ha eliminado al usuario {usuario.nombre}")
        self.usuarios.remove(usuario)
    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None
    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados")
        else:
            print("Usuarios:\n")
            for usuario in self.usuarios:
                print(usuario)
    # ----------------------------------CONTROL DE BIBLIOTECARIOS-------------------------------------
    def agregar_bibliotecario(self, bibliotecario):
        self.bibliotecarios.append(bibliotecario)
        print(f"Bibliotecario {bibliotecario.nombre} agregado")
    def buscar_bibliotecario(self, id_bibliotecario):
        for bibliotecario in self.bibliotecarios:
            if bibliotecario.id_bibliotecario == id_bibliotecario:
                return bibliotecario
    def eliminar_bibliotecario(self, bibliotecario):
        print(f"Se ha eliminado al bibliotecario {bibliotecario.nombre}")
        self.bibliotecarios.remove(bibliotecario)
    def mostrar_bibliotecarios(self):
        if not self.bibliotecarios:
            print("No hay bibliotecarios registrados")
        else:
            print("Bibliotecarios:\n")
            for bibliotecario in self.bibliotecarios:
                print(bibliotecario)
# ----------------------------------CONTROL DE SESIÓN-------------------------------------
    def iniciar_sesion(self, id_bibliotecario, contrasena):
        for bibliotecario in self.bibliotecarios:
            global sesion
            if bibliotecario.id_bibliotecario == id_bibliotecario and bibliotecario.contrasena == contrasena:
                print("Sesión iniciada\n")
                sesion = True
            else:
                print("ID o contraseña incorrectos\n")
        return sesion
    def iniciar_sesion_admin(self, id_admin, contrasena):
        for admin in self.administradores:
            global sesion
            if admin.id_admin == id_admin and admin.contrasena == contrasena:
                print("Sesión iniciada\n")
                sesion = True
            else:
                print("ID o contraseña incorrectos\n")
        return sesion