class Clase_Alumno:
    def __init__(self, nombre, carnet):
        self.__nombre = nombre
        self.__carnet = carnet
        self.__cursos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def carnet(self):
        return self.__carnet

    def tiene_curso(self, codigo_curso):
        for curso_buscar in self.__cursos:
            if curso_buscar.codigo == codigo_curso:
                return True
        return False 

    def agregar_curso(self, curso):
        if self.tiene_curso(curso.codigo):
            print(f"El alumno {self.__nombre} ya está inscrito en el curso {curso.nombre}.")
            return

        self.__cursos.append(curso)
        print(f"El alumno {self.__nombre} ha sido inscrito en el curso {curso.nombre}.")

    def buscar_curso(self, codigo_curso):
        for curso in self.__cursos:
            if curso.codigo == codigo_curso:
                return curso
        return None

    def eliminar_curso(self, codigo_curso):
        curso = self.buscar_curso(codigo_curso)
        if curso:
            self.__cursos.remove(curso)
            print(f"El curso {curso.nombre} ha sido eliminado del alumno {self.__nombre}.")
        else:
            print(f"El alumno {self.__nombre} no está inscrito en el curso con código {codigo_curso}.")
    
    def mostrar_cursos(self):
        if len(self.__cursos) == 0:
            print(f"El alumno {self.__nombre} no está inscrito en ningún curso.")
            return

        print(f"Cursos del alumno {self.__nombre}:")
        for curso in self.__cursos:
            curso.mostrar_informacion()