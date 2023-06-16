
@property
def horas(self):
    return self.__horas

@horas.setter
def horas(self ,h):
    self.__hora s =h

def __str__(self):
    return Alumno.__str( ) +Profesor.__str( ) +f"Horas de trabajo: {self.horas}"

def dar_clase(self, materia):
    print(f"{self.nombre} está dando {materia} del area {self.area} por {self.horas} horas")