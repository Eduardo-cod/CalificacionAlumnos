#Autor: Eduardo Esparza
#Version 1.1

#Clase materia
class Materia:

    #Constructor vacio de la clase Materia
    def __init__(self):
        self

    #Metodo que pide el total de alumnos a calificar
    def totalAlumnos(self):
        alumnos = int(input("Ingresa el total de alumnos: "))
        self.ingresarCalificaciones(alumnos)

    #Metodo que recibe el total de alumnos a calificar
    #para insertat calificaciones y obtener promedio
    #Los gaurda en una lista
    def ingresarCalificaciones(self,alumnos):
        lista = []
        i = 0;
        while i < alumnos:

            p1 = float(input("Ingresa la primera la calificacion: "))
            p2 = float(input("Ingresa la segunda calificacion: "))
            p3 = float(input("Ingresa la tercera calificacion: "))
            promedio = (p1 + p2 + p3) / 3.0
            lista.append(promedio)
            i+=1
        self.verificarPromedios(lista)

    #Metodo que recibe la lista de los promedios
    #para luego recorrer con un for y comprobar
    #si el alumno aprobo o no
    #guarda el mensaje de aprobacion de cada alumno en una lista
    def verificarPromedios(self,lista):
        lista2 = []

        for prom in lista:
            if prom < 6:
                lista2.append("Reprobado")
            elif prom >=6 and prom <= 6.4:
                lista2.append("Aprobado con 6")
            elif prom >= 6.5 and prom <= 7.4:
                lista2.append("Aprobado con 7")
            elif prom >= 7.5 and prom <= 8.4:
                lista2.append("Aprobado con 8")
            elif prom >= 8.5 and prom <= 9.4:
                lista2.append("Aporbado con 9")
            elif prom >= 9.5 and prom <= 10:
                lista2.append("Aprobado con 10")

        print("\n")
        print(f"Los Promedios son: {lista}")
        print("\n")
        print(f"Estado de Aprobacion: {lista2}")

promedios = Materia()
promedios.totalAlumnos();;