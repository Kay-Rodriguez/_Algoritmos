#1.	Realizar la corrección de la prueba (Use IF-ELSE anidado)
print("BIENVENIDO AL CARBONERO")
print("Por favor ingrese los datos para la factura")
nombre = str(input("Ingrese su nombre: "))
print(nombre)

cedula = int(input("Ingrese su número de cédula: "))
print(cedula)

correo_electronico = input("Ingrese su correo electrónico: ")
print(correo_electronico)

print("Le ofrecemos los siguientes tipos de hamburguesa:")
# Costos de hamburguesa
precio_hamburguesa_sencilla = 1.50
precio_hamburguesa_doble = 2.50
precio_hamburguesa_triple = 3.25
precios = [precio_hamburguesa_triple, precio_hamburguesa_sencilla, precio_hamburguesa_doble]

# Tipo de hamburguesa
print("Sencilla")
print("Doble")
print("Triple")
tipo_de_hamburguesa = input("Ingrese la hamburguesa que desea: ")

precio_unitario = 0

# Cantidad de hamburguesa
numero_de_hamburguesas = int(input("Ingrese la cantidad de hamburguesas: "))

# Precio total de hamburguesa
if tipo_de_hamburguesa == "sencilla":
    costo_total = numero_de_hamburguesas * precio_hamburguesa_sencilla
elif tipo_de_hamburguesa == "doble":
    costo_total = numero_de_hamburguesas * precio_hamburguesa_doble
elif tipo_de_hamburguesa == "triple":
    costo_total = numero_de_hamburguesas * precio_hamburguesa_triple
else:
    print("Tipo de hamburguesa no existe. Por favor ingrese sencilla, doble, triple")
    costo_total = 0

# Tipo de pago
print("Por favor ingrese un número para indicar el tipo de pago")
tipo_de_pago = input("Seleccione efectivo o tarjeta de crédito: ")

if tipo_de_pago.lower() == "tarjeta":
    cargo_de_tarjeta = costo_total * 0.05
else:
    print("El método de pago no es válido. Por favor, seleccione efectivo o tarjeta.")
    cargo_de_tarjeta = 0

# Costo final
costo_final_de_tarjeta = costo_total + cargo_de_tarjeta

# Resultado de la compra
print("Su pago es con tarjeta de crédito. Deberá cancelar el 5% adicional del pago: $", costo_final_de_tarjeta)
print("Nombre: ", nombre)
print("Cédula: ", cedula)
print("Correo Electrónico: ", correo_electronico)
print("Tipo de Hamburguesa: ", tipo_de_hamburguesa)
print("Cantidad de Hamburguesas: ", numero_de_hamburguesas)
print("Costo Total: $", costo_total)
print("Muchas gracias por su compra, vuelva pronto. La factura será enviada a su correo.")
print("Karla Rodriguez")

###############################################################################################################
#2.	Realizar el ejercicio anterior usando la sentencia SWITCH Case.
def sencilla():
    return 1.50

def doble():
    return 2.50

def triple():
    return 3.25

print("BIENVENIDO AL CARBONERO")
print("Por favor ingrese los datos para la factura")

nombre = str(input("Ingrese su nombre: "))
print(nombre)

cedula = int(input("Ingrese su número de cédula: "))
print(cedula)

correo_electronico = input("Ingrese su correo electrónico: ")
print(correo_electronico)

print("Le ofrecemos los siguientes tipos de hamburguesa:")
print("1. Sencilla")
print("2. Doble")
print("3. Triple")
opcion_tipo_hamburguesa = int(input("Ingrese el número correspondiente a la hamburguesa que desea: "))

switch = {
    1: sencilla,
    2: doble,
    3: triple
}

funcion_hamburguesa = switch.get(opcion_tipo_hamburguesa, lambda: 0)

# Cantidad de hamburguesa
numero_de_hamburguesas = int(input("Ingrese la cantidad de hamburguesas: "))

# Precio total de hamburguesa
costo_total = numero_de_hamburguesas * funcion_hamburguesa()

# Tipo de pago
print("Por favor ingrese un número para indicar el tipo de pago")
tipo_de_pago = input("Seleccione efectivo o tarjeta de crédito: ")

cargo_de_tarjeta = 0

if tipo_de_pago.lower() == "tarjeta":
    cargo_de_tarjeta = costo_total * 0.05
else:
    print("El método de pago no es válido. Por favor, seleccione efectivo o tarjeta.")

# Costo final
costo_final_de_tarjeta = costo_total + cargo_de_tarjeta

# Resultado de la compra
print("Su pago es con tarjeta de crédito. Deberá cancelar el 5% adicional del pago: $", costo_final_de_tarjeta)
print("Nombre: ", nombre)
print("Cédula: ", cedula)
print("Correo Electrónico: ", correo_electronico)
print("Tipo de Hamburguesa: ", opcion_tipo_hamburguesa)
print("Cantidad de Hamburguesas: ", numero_de_hamburguesas)
print("Costo Total: $", costo_total)
print("Muchas gracias por su compra, vuelva pronto. La factura será enviada a su correo.")
print("Karla Rodriguez")

#########################################################################
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def potencia(a, b):
    return a ** b

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: No se puede realizar el módulo por cero."

def main():
    while True:  
        print("Calculadora de Operaciones Básicas:")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División")
        print("5) Potencia")
        print("6) Módulo")
        print("7) Salir")

        opcion = int(input("Ingrese el número de la operación que desea realizar: "))
        
        if opcion == 7:
            break

        if 1 <= opcion <= 6:    
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            resultado = None

            if opcion == 1:
                resultado = suma(num1, num2)
            elif opcion == 2:
                resultado = resta(num1, num2)
            elif opcion == 3:
                resultado = multiplicacion(num1, num2)
            elif opcion == 4:
                resultado = division(num1, num2)
            elif opcion == 5:
                resultado = potencia(num1, num2)
            elif opcion == 6:
                resultado = modulo(num1, num2)
            else:
                print("Error: Opción no válida.")

            if resultado is not None:
                print("El resultado es:", resultado)

if __name__ == "__main__":
    main()

print("Karla Rodriguez")
