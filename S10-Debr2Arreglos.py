#tarea semana 10 KARLA RODIGUEZ, ISAAC QUINAPALLO,ANGEL VILLAMIL
#parte 1
#taller
#Programa que imprime las asignaturas definidas en una lista. 
def asignaturas(asignaturasLista):
    print("Asignaturas: ")
    for asignatura in asignaturasLista:
        print(asignatura)

asignaturasLista = ["Algoritmos","Redes", "Sistemas O.", "Programacion", "Arquitectura de C.", "Emprendimiento"]
asignaturas(asignaturasLista)

#Imprimir el tamaño de una lista dada 
def tamanoLista(lista):
    print("El tamaño de la lista es:", len(lista))

asignaturasLista = ["Algoritmos","Redes", "Sistemas O.", "Programacion", "Arquitectura de C.", "Emprendimiento"]
tamanoLista(asignaturasLista)

#Programa que imprime las asignaturas con for (elemento por elemento) 
def asignaturasfor(asignaturasLista):
    print("Asignaturas con for:")
    for asignatura in asignaturasLista:
        print(asignatura)

asignaturasLista = ["Algoritmos","Redes", "Sistemas O.", "Programacion", "Arquitectura de C.", "Emprendimiento"]
asignaturasfor(asignaturasLista)

#Unir dos listas y mostrar en una tercera lista 
def unirlistas(lista1, lista2):
    terceralista = lista1 + lista2
    return terceralista
lista1 = ["Algoritmos","Redes", "Sistemas O."]
lista2 = ["Programacion", "Arquitectura de C.", "Emprendimiento"]

terceralista = unirlistas(lista1, lista2)
print("Listas unidas:", terceralista)

#Agregar un elemento quemado a una lista usando append()  
def elementoquemado(lista):
    lista.append("Elemento quemado")

asignaturasLista = ['Algoritmos', "Redes", "Sistemas O.", "Programacion", "Arquitectura de C.", "Emprendimiento"]
elementoquemado(asignaturasLista)
print("Lista con elemento quemado:", asignaturasLista)

#Agregar un elemento pidiendo al usuario a una lista usando append()  
def usuario(lista):
    elemento_usuario = input("Ingrese un elemento: ")
    lista.append(elemento_usuario)

asignaturasLista = ["Algoritmos", "Redes", "Sistemas O.", "Programacion", "Arquitectura de C.", "Emprendimiento"]
usuario(asignaturasLista)
print("Lista con elemento del usuario:", asignaturasLista)

#Insertar las asignaturas en la lista e imprimirlas. 
def insertarasignaturas(lista, nuevas_asignaturas):
    lista.extend(nuevas_asignaturas)

asignaturasLista = ["Algoritmos", "Redes", "Sistemas O.", "Programacion", "Arquitectura de C.", "Emprendimiento"]
nuevas_asignaturas = ["Ecologia","Etica", "Deportes"]
insertarasignaturas(asignaturasLista, nuevas_asignaturas)

print("Lista con asignaturas insertadas: ", asignaturasLista)

#Crear una lista e inicialízala  con 5 cadenas de caracteres.
# Copia los elementos de la lista en otra lista pero en orden inverso, 
# y muestra sus elementos por la pantalla. 
nombres = ["Dorali", "Carolina", "karlita", "Sebastian", "Martin"]
invertidos = list(reversed(nombres))

print("Lista original de nombres:", nombres)
print("Lista invertida de nombres:", invertidos)

#Ejercicio9
# Pedir al usuario el número de elementos y ordenarlos de menor a mayor
nelementos = int(input("Ingrese el número de elementos: "))
arreglo = []
for i in range(nelementos):
    elemento = int(input(f"Ingrese el elemento {i + 1}: "))
    arreglo.append(elemento)
arreglo.sort()
print("Arreglo ordenado de menor a mayor:", arreglo)

#Ejercicio10
def ordenar(arreglo):
    n = len(arreglo)

    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j]>arreglo[j + 1]:
                arreglo[j], arreglo[j + 1] = arreglo[j+1], arreglo[j]
arreglo = [64, 34, 25, 12, 22, 11, 90]
print("Arreglo original:", arreglo)
ordenar(arreglo)
print("Arreglo ordenado de menor a mayor:", arreglo)

#Ejercicio11
def ordenar(array):
    tamano= len(array)
    for i in range(0, tamano - 1):
        for j in range(0, tamano - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array
numeros = [6, 3, 8, 2, 7]
print("La lista original es:", numeros)
print("La lista ordenada es:", ordenar(numeros))

#PARTE 2
#Ejercicio1
def ingresarNotas(asignaturas):
    notas = {}
    for asignatura in asignaturas:
        nota= float(input("Ingrese la nota para " + asignatura + ": "))
        notas[asignatura] = nota
    print("Notas del curso:")
    for asignatura, nota in notas.items(): #.items sirve para iterar tanto en el valor como en la palabra
        print(asignatura + ": " + str(nota))
asignaturasCurso = input("Ingrese las asignaturas del curso (separadas por comas): ").split(',') #.split sirve para separar variables y guardarlas
ingresarNotas(asignaturasCurso)

#Ejercicio2
import random
listaValores= [random.randint(1, 10) for i in range(10)]
for valor in listaValores:
    cuadrado= valor ** 2
    print("Elemento:", valor, "Cuadrado:", cuadrado)

#Ejercicio3
listacadenas= []
for i in range(5):
    cadena =input("Ingrese una cadena: ")
    listacadenas.append(cadena)
print("Cadena invertida:")
for cadena in listacadenas[::-1]:
    cadenainvertida = cadena[::-1]
    print(cadenainvertida)

#Ejercicio4
tamano= int(input("Ingrese el tamaño de los arrays: "))
nombres= []
longitudes= []
for _ in range(tamano):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    longitudes.append(len(nombre))
print("Array de nombres:", nombres)
print("Array de longitudes:", longitudes)

import random

# Equipos cabezas de serie
cabezas_de_serie = []
# Equipos restantes
equipos_restantes = []

# Solicitar los 8 equipos 
for i in range(8):
    equipo = input("Ingrese el nombre del equipo cabeza de serie: ")
    cabezas_de_serie.append(equipo)

# Generar una lista de los equipos restantes (del 9 al 32)
for i in range(9, 33):
    equipos_restantes.append(i)

# Asignar aleatoriamente los equipos restantes a las series
series = []
for i in range(8):
    serie = []
    # Agregar el equipo cabeza de serie a la serie
    serie.append(cabezas_de_serie[i])
    # Asignar aleatoriamente los equipos restantes
    equipos_asignados = random.sample(equipos_restantes, 3)
    serie.extend(equipos_asignados)
    series.append(serie)
    # Eliminar los equipos asignados de la lista de equipos restantes
    equipos_restantes = [equipo for equipo in equipos_restantes if equipo not in equipos_asignados]

# Mostrar el listado de las series resultantes
for i, serie in enumerate(series):
    print(f"Serie {i+1}: {serie}")

#ANGEL VILLAMIL S10

palabra = input("Ingrese una palabra: ")
#para transformar la palabra a minusculas y evitar crasheos
palabra = palabra.lower()

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Contar el número de veces que aparece cada vocal en la palabra
for letra in palabra:
    if letra in vocales:
        vocales[letra] += 1

# Mostrar el resultado
for vocal in vocales:
    cantidad = vocales[vocal]
    print("La vocal ", vocal, "aparece ", cantidad, "veces en la palabra ", palabra)

#8

#ANGEL VILLAMIL
print("Impresora de letras del abecedario en su tercera posicion")
abecedario = list("abcdefghijklmnopqrstuvwxyz")
print(abecedario[0])

for i in range(2, len(abecedario), 3):
    print(abecedario[i])


#7
#ANGEL VILLAMIL
asignaturas = ["Base de Datos", "Programación", "Matemáticas", "Algoritmos", "Análisis", "Lengua"]
asignaturas_repetir = []

for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de {asignatura}: "))
    if nota < 5.0:
        asignaturas_repetir.append(asignatura)

# Mostrar las asignaturas a repetir o un mensaje de felicitaciones
if len(asignaturas_repetir) > 0:
    print("Debes repetir las siguientes asignaturas:")
    for asignatura in asignaturas_repetir:
        print(asignatura)
else:
    print("¡Felicidades! No tienes que repetir ninguna asignatura.")

#6
#ANGEL VILLAMIL

notas = [20, 15, 12, 11, 8, 4, 1]

nota_mas_baja = notas[0]
for nota in notas:
    if nota < nota_mas_baja:
        nota_mas_baja = nota

notas.remove(nota_mas_baja)

# Calcular el promedio
promedio = sum(notas) / len(notas)
promedio = round(promedio, 2)
print("La nota más baja eliminada es:", nota_mas_baja)
print("El promedio de las notas restantes es:", promedio)

#5
#ANGEL VILLAMIL
numeros = [1, 2, 5, 8, 3, 4, 30, 9, 13]

for numero in numeros:
    if numero > 3 and numero % 2 != 0:
        print(numero)

