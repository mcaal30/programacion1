class Clase_Curso:
    def __init__(self, nombre, codigo):
        self.__nombre = nombre
        self.__codigo = codigo

    @property
    def nombre(self):
        return self.__nombre   

    @property
    def codigo(self):
        return self.__codigo    

    def mostrar_informacion(self):
        print(f"Nombre del curso: {self.__nombre}")
        print(f"Código del curso: {self.__codigo}")