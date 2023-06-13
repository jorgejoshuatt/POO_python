from cosas import Alumno
def main():
    al1 = Alumno("Diego", 18, "ICO")
    print(vars(al1))

    al2 = Alumno("Monse", 20, "Derecho")
    print(vars(al2))
    """
    al1=Alumno()
    print(al1)
    al2=Alumno()
    print(al1.facultad) #Atributo de instancia
    print(al2.facultad) #Atributo de instancia
    print(Alumno.facultad) #Atributo de clase (Todos tienen este elemento en común)
    print("-----------")
    al1.facultad="FES Aragón EDOMEX" #Se le agrega un atributo de instancia al al1
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print("-- Un vistazo a los objetos --")
    print(vars(al1))
    print(vars(al2))
    print("-- Modificar atributos publicos --")
    al1.edad=999
    print(vars(al1))
    print(vars(al2))
    """


main()
