
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
msj = 'Hola Mundo!'
print (msj)


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.#
nombre = input('Ingrese su nombre: ')
print(f'"Hola {nombre}!"')


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla 
# una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”,
#  el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo
#  si utilizas print(f…) para realizar la impresión por pantalla.#
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}')



#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math
from math import pi
radio = int(input("Ingrese el radio de un círculo "))
PI = math.pi
area = PI * radio ** 2
perimetro = 2 * PI * radio
print (f"El Área del circulo es {area} y su Perimetro es {perimetro}")



#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
segundo = int(input("Ingrese una cantidad de segundos "))
hora = segundo/3600  
print (f"Equivale a {hora} horas")



#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 
numero = int(input("Ingrese un numero "))
for num in range (1,11):
    rdo = num*numero
    print (f"{numero} x {num} = {rdo}")



#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el 
# resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
num1 = int(input("Ingrese un número : "))
while True:   
    num2 = int(input("Ingrese otro número (distinto de cero): "))
    if num2 != 0:
        break;
    else:
        print("El número es cero. Inténtalo de nuevo.")

print(f"La Suma de {num1} y {num2} es: {num1+num2}")
print(f"La Division de {num1} y {num2} es: {num1/num2}")
print(f"La Multiplicacion de {num1} y {num2} es: {num1*num2}")
print(f"La Resta de {num1} y {num2} es: {num1-num2}")



#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
    #𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
altura = float(input("Ingrese su altura en metros : "))
peso = float(input("Ingrese su peso en kilos : "))

imc = peso / (altura**2)
print(f"Si IMC es {imc}")



#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
    #𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =95.𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura celsius {celsius} equivalente en Fahrenheit es: {fahrenheit}")



#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.#
num1 = int(input("Ingrese el 1° número : "))
num2 = int(input("Ingrese el 2° número : "))
num3 = int(input("Ingrese el 3° número : "))
prom = (num1+num2+num3)/3
print(f"El promedio de los numeros ingresado es: {prom}")