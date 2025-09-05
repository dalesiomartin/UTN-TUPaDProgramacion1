# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for n in range(0,101):
    print(n)

#---------------------------------------------------------------------------------------------

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero_O = int(input("Ingrese un numero entero: "))
cont = 0

if numero_O == 0:
    numero = numero_O
    cont = 1
else:
    numero = abs(numero_O)

while numero >= 1:
    cont = cont + 1
    numero = numero/10

print(f"La cantidad de digitos del numero {numero_O} es de {cont} digitos")

#---------------------------------------------------------------------------------------------

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un numero entero "))
num2 = int(input("Ingrese otro numero entero "))
suma = 0

if num1 == num2:
    print("Ambos numeros son iguales")

if num2>num1:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1

for n in range(menor+1, mayor):
    suma = suma + n

print(f"La suma entre {num1} y {num2} es: {suma}")

#---------------------------------------------------------------------------------------------
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

num = int(input("Ingrese un numero entero (*con 0 cero corta): "))
suma = 0
while num != 0:
    suma += num
    num = int(input("Ingrese otro numero entero (*con 0 cero corta): "))

print("Programa Finalizado!")
print (f"La suma de los numeros ingresados es: {suma} ")

#---------------------------------------------------------------------------------------------
# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
nro_sorpresa = random.randint(0,9)

print("Adivina el numero escondido, va entre 0 y 9")
numero = int (input("Ingrese un número: "))
cant = 1
while nro_sorpresa != numero:
    print("No acertaste.....prueba otra vez")
    cant +=1
    numero = int (input("Ingrese otro número: "))

print(f"Felicitaciones!! . Lo lograste en {cant} intentos.....")

#---------------------------------------------------------------------------------------------
# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for n in range(100,-1,-2):
   print(n)

for n in range (100,-1,-1):
    if n % 2 == 0:
        print(n)

#---------------------------------------------------------------------------------------------
# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

suma=0
band = True
while band:
    numero = int (input("Ingrese un número positivo: "))
    if numero > 0:
        band= False

for n in range(0, numero+1):
    suma += n

print(f"La suma de todos los numeros comprendidos entre 0 y {numero} es: {suma}")

#---------------------------------------------------------------------------------------------
# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cont_pares=0
cont_impares=0
cont_positivos=0
cont_negativos=0

for n in range(0,10):
    numero = int (input("Ingrese un número: "))

    if numero == 0:
        cont_pares+=1
    elif numero > 0:
        cont_positivos+=1
        if numero % 2 == 0:  
            cont_pares+=1
        else:
            cont_impares+=1
    else:
        cont_negativos+=1
        if numero % 2 == 0:            
            cont_pares+=1
        else:
            cont_impares+=1

print(f"La cantidad de numeros pares es: {cont_pares}")
print(f"La cantidad de numeros impares es: {cont_impares}")
print(f"La cantidad de numeros positivos es: {cont_positivos}")
print(f"La cantidad de numeros negativos es: {cont_negativos}")

#---------------------------------------------------------------------------------------------
# # 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

suma = 0
cantidad_numeros = 3 

for i in range(0,cantidad_numeros):
    numero = int(input(f"Ingrese el número #{i+1}: "))
    suma += numero

media = suma / cantidad_numeros
print(f"La media de los {cantidad_numeros} números es: {media}")

#---------------------------------------------------------------------------------------------
# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número: ") #lo cargo como string
numero_len = len(numero)
numero_invertido = ""

for n in range(numero_len-1,-1,-1):
    numero_invertido +=numero[n]

print(f"El numero invertido es: {numero_invertido}")