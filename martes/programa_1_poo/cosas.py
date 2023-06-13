class Alumno:
    facultad="FES Aragón" #Atributo de clase (Todos tienen este elemento en común)
    def __init__(self, nom, ed, carr): #Declarar el constructor
        self.__nombre=nom #Atributo de instancia
        self.__edad=ed
        self.__carrera=carr
