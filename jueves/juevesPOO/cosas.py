class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre=nom
        self.__pseudonimo=pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre=nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @nombre.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f"Nombre: {self.__nombre} pseudónimo: {self.__pseudonimo}"

    def escribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente obra")

class Libro:
    def __init__(self,tit,aut,an,ed):
        self.__titulo=tit
        self.__autor=aut
        self.__año=an
        self.__editorial=ed

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, tit):
        self.__titulo = tit

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, aut):
        self.__autor = aut

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, an):
        self.__año = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, ed):
        self.__editorial = ed

    def __str__(self):
        return f"""
            Título = {self.__titulo}
            Autor={self.__autor}
            Año={self.__año}
            Editorial={self.__editorial}
        """

    @classmethod
    def libro_planeta(cls,titulo, autor, año):
        return cls(titulo, autor, año, "Planeta")

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre=nombre
        self.__edad=edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

class Alumno(Persona):
    def __init__(self, nombre, edad, numer_cuenta, carrera, promedio):
        super().__init__(nombre,edad)
        self.__numero_cuenta=numer_cuenta
        self.__carrera=carrera
        self.__promedio=promedio