import libreria
import Main
Main.salir = False
biblioteca = Main.biblioteca
def registro_libro():
    print("Escriba el título del libro")
    titulo = input()
    print("Escriba el autor del libro")
    autor = input()
    print("Escriba la descripción del libro")
    descripcion = input()
    print("Escriba el isbn del libro")
    isbn = int(input())
    if isbn < 0:
        print("El isbn debe ser un número positivo")
    else:
        libro = libreria.libro(titulo, autor, descripcion, isbn)
        biblioteca.agregar_libro(libro)
def eliminar_libro():
    print("Escriba el isbn del libro")
    isbn = int(input())
    libro = biblioteca.buscar_libro_isbn(isbn)
    biblioteca.eliminar_libro(libro)
def prestar_libro():
    print("Escriba el isbn del libro")
    isbn = int(input())
    libro = biblioteca.buscar_libro_isbn(isbn)
    while libro == None:
        print("""
              Libro no encontrado, se debe escribir un isbn válido
              Escriba un isbn válido...
              """)
        isbn = int(input())
        libro = biblioteca.buscar_libro_isbn(isbn)
    print("Escriba el id del usuario")
    id = int(input())
    usuario = biblioteca.buscar_usuario(id)
    while usuario == None:
        print("Usuario no encontrado, se debe escribir un id válido")
        id = int(input())
        usuario = biblioteca.buscar_usuario(id)
    biblioteca.prestar_libro(libro, usuario)
def recibir_devolucion():
    print("Escriba el isbn del libro")
    isbn = int(input())
    libro = biblioteca.buscar_libro_isbn(isbn)
    while libro == None:
        print("Libro no encontrado, se debe escribir un isbn válido")
        isbn = int(input())
        libro = biblioteca.buscar_libro_isbn(isbn)
    print("Escriba el id del usuario")
    id = int(input())
    usuario = biblioteca.buscar_usuario(id)
    while usuario == None:
        print("Usuario no encontrado, se debe escribir un id válido")
        id = int(input())
        usuario = biblioteca.buscar_usuario(id)
    biblioteca.recibir_devolucion(libro, usuario)
def buscar_libro():
    print("Escriba el título del libro")
    titulo = input()
    libro = biblioteca.buscar_libro(titulo)
    if libro == None:
        print("Libro no encontrado")
    else:
        print(libro)
def menu_bibliotecario():
    print("""Seleccione una opción
                1. Registrar libro
                2. Eliminar libro
                3. Prestar libro
                4. Recibir devolución
                5. Mostrar libros disponibles
                6. Buscar libro
                7. Salir
                """)
    select = int(input())
    match select:
        case 1:
            registro_libro()
        case 2:
            eliminar_libro()
        case 3:
            prestar_libro()
        case 4:
            recibir_devolucion()
        case 5:
            biblioteca.mostrar_libros_disponibles()
        case 6:
            buscar_libro()
        case 7:
            Main.salir = True            
def menu():
    while Main.salir == False:
        print("""Seleccione una opción
              1. Configurar libros
              2. Configurar usuarios
              3. Configurar bibliotecarios
              4. Salir
              """)
        select = int(input())
        match select:
            case 1:
                print("""Seleccione una opción
                1. Registrar libro
                2. Eliminar libro
                3. Prestar libro
                4. Recibir devolución
                5. Mostrar libros disponibles
                6. Buscar libro
                7. Salir
                """)
                select = int(input())
                match select:
                    case 1:
                        registro_libro()
                    case 2:
                        eliminar_libro()
                    case 3:
                        prestar_libro()
                    case 4:
                        recibir_devolucion()
                    case 5:
                        biblioteca.mostrar_libros_disponibles()
                    case 6:
                        buscar_libro()
                    case 7:
                        break
            case 2:
                print("""Seleccione una opción
                1. Agregar usuario
                2. Eliminar usuario
                3. Mostrar usuarios
                4. Salir
                """)
                select = int(input())
                match select:
                    case 1:
                        print("Escriba el id del usuario")
                        id = int(input())
                        if id < 0:
                            print("El id debe ser un número positivo")
                        elif biblioteca.buscar_usuario(id) != None:
                            print("El usuario con ese id ya existe")
                        else:
                            print("Escriba el nombre del usuario")
                            nombre = input()
                            usuario = libreria.usuario(nombre, id)
                            biblioteca.agregar_usuario(usuario)
                    case 2:
                        print("Escriba el id del usuario")
                        id = int(input())
                        usuario = biblioteca.buscar_usuario(id)
                        biblioteca.eliminar_usuario(usuario)
                    case 3:
                        biblioteca.mostrar_usuarios()
                    case 4:
                        break
            case 3:
                print("""Seleccione una opción
                1. Agregar bibliotecario
                2. Eliminar bibliotecario
                3. Mostrar bibliotecarios
                4. Salir
                """)
                select = int(input())
                match select:
                    case 1:
                        print("Escriba el id del bibliotecario")
                        id = int(input())
                        if id < 0:
                            print("El id debe ser un número positivo")
                        elif biblioteca.buscar_bibliotecario(id) != None:
                            print("El bibliotecario con ese id ya existe")
                        else:
                            print("Escriba el nombre del bibliotecario")
                            nombre = input()
                            print("Escriba la contraseña del bibliotecario")
                            contrasena = int(input())
                            bibliotecario = libreria.bibliotecario(nombre, id, contrasena)
                            biblioteca.agregar_bibliotecario(bibliotecario)
                            print("Se ha agregado el bibliotecario")
                    case 2:
                        print("Escriba el id del bibliotecario")
                        id = int(input())
                        bibliotecario = biblioteca.buscar_bibliotecario(id)
                        if bibliotecario == None:
                            print("Bibliotecario no encontrado")
                        else:
                            biblioteca.eliminar_bibliotecario(bibliotecario)
                    case 3:
                        biblioteca.mostrar_bibliotecarios()
                    case 4:
                        break
            case 4:
                Main.salir = True
                break