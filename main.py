from alumno import Clase_Alumno
from curso import Clase_Curso

obj_alumno1 = Clase_Alumno("Juan Pérez", "2023001")
obj_alumno2 = Clase_Alumno("María García", "2023002")

obj_curso1 = Clase_Curso("Matemáticas", "MAT101")
obj_curso2 = Clase_Curso("Física", "FIS101")

print ("Inscribiendo cursos para el alumno 1:")
obj_alumno1.agregar_curso(obj_curso1)
obj_alumno1.agregar_curso(obj_curso2)

print("\nInscribiendo cursos para el alumno 2:")
obj_alumno2.agregar_curso(obj_curso1)

print("\nMostrando cursos del alumno 1:")
obj_alumno1.mostrar_cursos()      

print("\nMostrando cursos del alumno 2:")
obj_alumno2.mostrar_cursos()

print("\nBuscando curso del alumno 1:")
curso_encontrado = obj_alumno1.buscar_curso(obj_curso1.codigo)

if curso_encontrado:
    print(f"El alumno {obj_alumno1.nombre} está inscrito en el curso {curso_encontrado.nombre}.")
else:
    print(f"El alumno {obj_alumno1.nombre} no está inscrito en el curso {obj_curso1.nombre}.")

print("\nIntentado agregar curso repetido:")
obj_alumno1.agregar_curso(obj_curso1)

print("\nEliminando curso del alumno 1:")
obj_alumno1.eliminar_curso(obj_curso1.codigo)   