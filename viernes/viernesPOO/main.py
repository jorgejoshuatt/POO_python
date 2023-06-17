from cosas import *

def main():

    per1=Persona("Brandon",22)
    print(per1)
    print(Persona.descripcion)
    print(vars(per1))

    al2= Alumno.constructor_defecto()
    print(al2)

    print("---------Herencia ayudante de profesor------------")
    ayudante= AyudanteProfesor("El brus", 20, "6515611", "ICO", 23223, "Administracion de dabses de datos", 4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre="El Josh"
    ayudante.dar_clase("Programacion orientada a objetos")

main()