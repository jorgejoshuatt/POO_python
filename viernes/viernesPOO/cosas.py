class Persona:
    descripcion = "un ser humano común y corriente"

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed

    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad}"

    def dormir(self):
        print("ZzZzZzZzZzZz que calors.... zZzz")

    @classmethod
    def constructor_defecto(cls):
        return cls("", 0)


class Alumno(Persona):
    descripcion = "Una persona que dice que estudia pero se la pasa en el cel"

    def __init__(self, nombre, edad, nc, carrera):
        Persona.__init__(self, nombre, edad)
        self.__numero_cuenta = nc
        self.__carrera = carrera

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, nc):
        self.__numero_cuenta = nc

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    def __str__(self):
        return super().__str__() + f", Numero de cuenta: {self.__numero_cuenta}, Carrera: {self.__carrera}"

    def dormir(self):
        print(super().nombre, " está durmiendo como alumno")

    @classmethod
    def constructor_defecto(cls):
        return cls("", 0, "", "")
        # Alumno.constructor_defecto


class Profesor(Persona):
    descripcion = "Una persona que dice que enseña pero se la pasa leyendo artículos de investigación"

    def __init__(self, nombre, edad, num_tra, area):
        Persona.__init__(self, nombre, edad)
        self.__numero_trabajador = num_tra
        self.__area = area

    @property
    def numero_trabajador(self):
        return self.__numero_trabajador

    @numero_trabajador.setter
    def numero_trabajador(self, num_tra):
        self.__numero_trabajador = num_tra

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    def __str__(self):
        return super().__str__() + f", Numero de trabajador: {self.__numero_trabajador}, Area: {self.__area}"

    def dormir(self):
        print(super().nombre, " está durmiendo como profesor")


class AyudanteProfesor(Alumno, Profesor):
    def __init__(self, nombre, edad, nc, carr, num_tra, area, numero_horas):
        Alumno.__init__(self, nombre, edad, nc, carr)
        Profesor.__init__(self, nombre, edad, num_tra, area)
        self.__horas = numero_horas

    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, h):
        self.__horas = h

    def __str__(self):
        return Alumno.__str__(self) + str(self.numero_trabajador) + self.area + f"Horas de trabajo: {self.horas}"

    def dar_clase(self, materia):
        print(f"{self.nombre} esta dando {materia} del area {self.area} por {self.horas} horas")

    def dormir(self):
        Alumno.dormir(self)
        Profesor.dormir(self)