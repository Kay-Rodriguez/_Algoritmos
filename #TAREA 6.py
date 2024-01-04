#TAREA 
#EJERCICIO 1 /
#1.	Calcule la media de varias notas ingresadas por teclado. El usuario ingresará tantas notas hasta que ingrese el “0”.
"""notas = []
while True :
    nota = float(input("Ingrese una nota ( ingrese 0 para calcular): "))
    if nota == 0:
        break
    notas.append(nota)
    
    if len (notas )== 0:
        print("No hay notas.")
    else:
        media = sum(notas) / len(notas)
print(f"La media de las notas ingresadas es: {media}")
#EJERCICIO 2
#2.	Dado un número entero positivo, mostrar su factorial.
#El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
num = int(input("Ingrese un número entero: "))
factorial = 1
if num < 0:
    print ("ingrese un numero entero positivo ")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
print(f"El factorial de {num} es {factorial}") 
#EJERCICIO 3
#3.	Crear un bucle que cuente los números pares e impares del 1 al 100,
# los números deberán ser ingresados por teclado, hasta que el usuario digite “0”.
# Al finalizar, informar la cantidad de números pares y de impares leídos en total
pares = 0
impares = 0
while True:
    numero = int(input("Ingrese un número o 0 para salir: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"total de números pares: {pares} y total de números impares {impares}.")
#EJERCICIO 4
#4.	Crear un programa que imprima la Sucesión de Fibonacci, desde el número 0 hasta el 1597, horizontalmente. (7 líneas de código)
print( " sucesion de fibonacci ")
a, b = 0, 1
sucesion =[a]
while b <= 1597 :
    sucesion.append(b)
    a, b = b, a + b   
    print(a, end=" ") 
#TAREA
# WHILE
# ejercicio 1
print("BIENVENIDO AL BANCO")
objetivo = 1000
ahorrado = 0
cantidad = float(input("Ingrese la cantidad de dinero que desea ahorrar: "))
while ahorrado < objetivo:
    if cantidad < 0:
        print("La cantidad ingresada es negativa, no es válida, inténte de nuevo.")
    else:
        ahorrado += cantidad
        if ahorrado >= objetivo:
            print(f"!!!Felicidades¡¡¡ ha alcanzado su objetivo de ahorro de ${objetivo}")
        else:
            print(f"Ha ahorrado ${ahorrado:.2f} de ${objetivo:.2f}.")
    cantidad = float(input("Ingrese la cantidad de dinero que desea ahorrar (0 para salir): "))
print("¡Gracias por ahorrar con nosotros!")
#Use WHILE o FOR, según crea conveniente
# ejercicio 2 
numero = input("Ingrese un número: ")
contador = 0
for digito in numero:
    contador += 1
print(f"El número {numero} tiene {contador} dígitos.")
#ejercicio 3.
# Mostrar un menú con tres opciones: 
# 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. 
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
# Si elige una opción incorrecta, informarle del error.
# El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir.
# Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, 
# se interrumpirá la impresión del menú y el programa finalizará. 
def comenzarprograma():
    print("Programa iniciado")
def imprimirlistado():
    print("Imprimiendo listado")
while True:
    print("Menú de opciones:")
    print("1- Comenzar programa")
    print("2- Imprimir listado")
    print("3- Finalizar programa")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Ha seleccionado la opción 1: Comenzar programa")
        comenzarprograma()
    elif opcion == "2":
        print("Ha seleccionado la opción 2: Imprimir listado")
        imprimirlistado()
    elif opcion == "3":
        print("Ha seleccionado la opción 3: Finalizar programa")
        break
    else:
        print("Opción incorrecta. Por favor, seleccione una opción válida.")
#ejercicio 4
#Si ingresa un número negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.
total=0
monto = float(input("Ingrese el monto de una venta: $"))
while monto != 0:
    if monto < 0:
        print("El monto ingresado es negativo. Por favor, ingrese un nuevo monto.")
    else:
        total += monto
    monto = float(input("Ingrese el monto de una venta: $"))
if total > 1000:
    descuentototal = total * 0.10
    totalpagar =total - descuentototal
    print(f"El total a pagar con descuento es: ${totalpagar}")
else: 
    totalpagar= total
    print(f"El total a pagar es: ${totalpagar}")"""
    
#ejercicio 5

categorias = ["Perfumería", "Joyería", "Maquillaje", "Ropa"]
articulos_perfumeria = ["Tentación", "Primavera", "Otoño", "Seducción"]
articulos_joyeria = ["Aretes", "Collar", "Cadena", "Pulsera"]
articulos_maquillaje = ["Sombras", "Maquillaje", "Labiales", "Rimel"]
articulos_ropa = ["Blusa", "Chaqueta", "Pantalón", "Abrigo"]
precios_perfumeria = [30, 28, 15, 35]
precios_joyeria = [7, 5, 20, 15]
precios_maquillaje = [8, 5, 4, 6]
precios_ropa = [25, 60, 18, 90]
subtotal = 0
total = 0
cantidad_por_categoria = {categoria: 0 for categoria in categorias}

while True:
    print("Seleccione una categoría:")
    for i, categoria in enumerate(categorias):
        print(f"{i + 1}. {categoria}")

    opcion_categoria = int(input())
    opcion_categoria -= 1

    print("Seleccione un artículo:")
    if opcion_categoria == 1:
        for i, articulo in enumerate(articulos_perfumeria):
            print(f"{i + 1}. {articulo}")
        opcion_articulo = int(input())
        articulo = articulos_perfumeria[opcion_articulo - 1]
        subtotal += precios_perfumeria[opcion_articulo - 1]
        cantidad_por_categoria["Perfumería"] += 1
    elif opcion_categoria == 2:
         for i, articulo in enumerate(articulos_joyeria):
            print(f"{i + 1}. {articulo}")
            opcion_articulo = int(input())
            articulo = articulos_joyeria[opcion_articulo - 1]
            subtotal += precios_joyeria[opcion_articulo - 1]
            cantidad_por_categoria["Joyería"] += 1
    elif opcion_categoria == 3:
        for i, articulo in enumerate(articulos_maquillaje):
            print(f"{i + 1}. {articulo}")
        opcion_articulo = int(input())
        articulo = articulos_maquillaje[opcion_articulo - 1]
        subtotal += precios_maquillaje[opcion_articulo - 1]
        cantidad_por_categoria["Maquillaje"] += 1
    elif opcion_categoria == 4:
        for i, articulo in enumerate(articulos_ropa):
            print(f"{i + 1}. {articulo}")
        opcion_articulo = int(input())
        articulo = articulos_ropa[opcion_articulo - 1]
        subtotal += precios_ropa[opcion_articulo - 1]
        cantidad_por_categoria["Ropa"] += 1

    opcion = input("¿Desea comprar otro artículo? (s/n)").lower()
    
    if opcion == 'n':
        break

print(f"El subtotal de la compra es: {subtotal}")


print("La cantidad de artículos comprados por categoría es:")
for categoria, cantidad in cantidad_por_categoria.items():
    print(f"{categoria}: {cantidad}")

total = subtotal
print(f"El total de la compra es: {total}")


#ejercicio 6 
lineas_completas = 0
while True:
    linea = input("Libro: ")
    if linea == "*":
        print(f"Fin. Se leyeron {lineas_completas} líneas completas.")
        break
    elif "/" in linea:
        digitos = sum([1 for c in linea if c.isdigit()])
        print(f"Línea completa. Aparecen {digitos} dígitos numéricos.")
        lineas_completas += 1
    else:
        continue
 