import libreria
import metodos
salir = False
biblioteca = libreria.biblioteca()
administrador = libreria.admin("Andres", 1, 1234) #NOMBRE, ID, CONTRASEÑA DEL ADMINISTRADOR
biblioteca.agregar_admin(administrador) 
def main():
    print("""
          Bienvenido a la biblioteca
          ¿Quiere iniciar sesión como administrador o como bibliotecario?
          1.- Administrador
          2.- Bibliotecario
          3.- Salir de la aplicación
          """)
    select = int(input())
    match select:
        case 1:
            while libreria.sesion == False:
                print("Escriba el ID del admin")
                id = int(input())
                print("Escriba la contraseña")
                contrasena = int(input())
                biblioteca.iniciar_sesion_admin(id, contrasena)
            metodos.menu()
        case 2:
            while libreria.sesion == False:
                print("Escriba el ID del bibliotecario")
                id = int(input())
                print("Escriba la contraseña")
                contrasena = int(input())
                biblioteca.iniciar_sesion(id, contrasena)
            metodos.menu_bibliotecario()
        case 3:
            global salir
            salir = True

if __name__ == "__main__":
    main()
    print("Usted ha salido de la aplicación...")

