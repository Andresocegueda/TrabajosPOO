import Estudiante
def main():
    alumno = Estudiante.estudiante("Juan", 6)
    print("Ingrese la universidad del estudiante")
    alumno.universidad = input()
    print("Ingrese la carrera del estudiante")
    alumno.carrera = input()
    print("Ingrese el semestre del estudiante")
    alumno.semestre = int(input())

    if alumno.nota > 6:
        print(f"El estudiante de la universidad {alumno.universidad} de la carrera {alumno.carrera} {alumno.nombre} con semestre {alumno.semestre} en curso, aprobó con {alumno.nota}")
    else:
        print(f"El estudiante de la universidad {alumno.universidad} de la carrera {alumno.carrera} {alumno.nombre} con semestre {alumno.semestre} en curso, reprobó con {alumno.nota}")

if __name__ == "__main__":
    main()