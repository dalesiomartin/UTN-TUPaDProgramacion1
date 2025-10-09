# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#-----------------------------------------------------------------------------------------------#

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    saludo= f"Hola {nombre}!"
    return saludo

nombre_usuario = input("Ingrese su nombre: ")
mensaje=saludar_usuario(nombre_usuario)
print(mensaje)


#-----------------------------------------------------------------------------------------------#
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(n, a,e, r):
    print(f"Soy {n} {a}, tengo {e} años y vivo en {r}") 
    

print("--Ingreses sus datos personales--")
nombre= input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))
residencia= input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido,edad, residencia)


#-----------------------------------------------------------------------------------------------#
#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    area = math.pi * (radio * radio)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * (math.pi) * radio
    return perimetro

radio_circulo = float(input("Ingrese el radio del circulo: "))

print(f"El area del circulo es: {calcular_area_circulo(radio_circulo)} y su perimetro es: {calcular_perimetro_circulo(radio_circulo)}")


#-----------------------------------------------------------------------------------------------#
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    hora = segundos / 60 / 60
    return hora

segundos_convertir = float(input("Ingrese los segundos para ser convetidos a horas: "))
hora_convertida = segundos_a_horas(segundos_convertir)

print(f"El resultado de la conversion son {hora_convertida:.2f} horas ")



#-----------------------------------------------------------------------------------------------#
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    print(f"Tabla de Multiplicar del {numero}")
    for i in range(1,11):
        print(f"{i} x {numero}: {i*numero}")

num = int(input("Ingrese el numero para mostrar su tabla de multiplicacion: "))

tabla_multiplicar(num)


#-----------------------------------------------------------------------------------------------#
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = divide_cero(a,b)
    return suma , resta, mult, div

def divide_cero (a,b):
    if b == 0:
        return "Error DIV/0"
    else:
        return a / b


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: ")) 

resultado = operaciones_basicas(num1, num2)

print("\nResultados de las operaciones:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")




#-----------------------------------------------------------------------------------------------#
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Ingrese su peso en kilos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado = calcular_imc(peso,altura)
print(f"El IMC es {resultado:.2F}")

#-----------------------------------------------------------------------------------------------#
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    conversion = (celsius * 9/5) +32
    return conversion

temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"La temperatura pasado a Fahrenheit es: {temp_fahrenheit:.2F}")

#-----------------------------------------------------------------------------------------------#
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))
num3 = float(input("Ingresá el tercer número: "))

resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de los tres números es: {resultado:.2F}")


#-----------------------------------------------------------------------------------------------#