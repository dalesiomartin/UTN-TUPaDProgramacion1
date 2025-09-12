# Actividades:
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

lista_notas = [7,8,9,10,5,6,8,9,6,9]
len_notas = len(lista_notas)
suma=0
for n in range(len_notas):
    print(f"Alumno {n+1} su nota es: {lista_notas[n]}")
    # comparo las notas que ingresan de la lista
    if n == 0:
        menor = lista_notas[n]
        mayor = lista_notas[n]
    elif lista_notas [n] < menor:
        menor = lista_notas[n]
    elif lista_notas [n] > mayor:
        mayor = lista_notas[n]
    suma += lista_notas[n]

promedio = suma / len_notas

print(f"El promedio de las nota es: {promedio:.2f}")

##Otra altenativa usar la funcion min y max para las notas
# menor = min(lista_notas)
# mayor = max(lista_notas)

print(f"La menor nota es: {menor} y la mayor nota es: {mayor}")

#------------------------------------------------------------------------------------

# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

mi_lista = []

for i in range(5):
    producto = input(f"Ingrese el {i+1}° producto de la lista: ")
    mi_lista.append(producto)

print("\nSu lista original de productos")
print(mi_lista)

lista_ordenada = sorted(mi_lista)
print("\nLista ordenada alfabeticamente de productos")
print(lista_ordenada)

print("\n¿Le gustaria Eliminar algún producto de la lista?")
opcion = (input("E- Eliminar o S-Salir: ")).lower()

while opcion not in ('e', 's'):
    print("Letra incorrecta")
    opcion = input("E- Eliminar o S-Salir: ").lower()

while opcion != 's':
    elemento = input("Ingrese el nombre del producto que desea eliminar: ")
    if elemento in lista_ordenada:
        lista_ordenada.remove(elemento)
        print(f"El prodcuto {elemento} fue eliminado!!")
    else:
        print(f"El producto {elemento} NO esta en la lista")

    opcion = (input("\nE- Eliminar otro producto o S-Salir: ")).lower()

print("\nSu lista actualizada")
print(lista_ordenada)


#------------------------------------------------------------------------------------

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

lista_aleatoria = []
lista_pares = []
lista_impares = []
cont_pares =0
cont_impares =0
cantidad_elementos=15

for i in range(cantidad_elementos):
    valor = random.randint(1,100)
    lista_aleatoria.append(valor)
    if valor % 2 == 0:
        lista_pares.append(valor)
        cont_pares +=1
    else:
        lista_impares.append(valor)
        cont_impares +=1

print("\nLista Orginal con ")
print(lista_aleatoria)

print(f"\nLista con números Pares, con {cont_pares} elementos")
print(lista_pares)

print(f"\nLista con números Impares, con {cont_impares} elementos")
print(lista_impares)


#------------------------------------------------------------------------------------

# 4) Dada una lista con valores repetidos:
## datos = [1,3,5,3,7,1,9,5,3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]
cant = len(datos)
datos_unicos=[]
#opcion robusta. Tambien lo podria hacer con set ==> datos_unicos = set(datos)
for i in range(cant):
    if datos[i] not in datos_unicos:
        datos_unicos.append(datos[i])

print("\nLista Orginal ")
print(datos)
print("\nLista Datos Unicos ")
for i in datos_unicos:
    print(i, end=" ")

#------------------------------------------------------------------------------------

# 5)
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

lista_alumnos = []

for i in range(8):
    nombre = input(f"Ingrese el nombre del {i+1}° estudiante: ")
    lista_alumnos.append(nombre)


print("\nSu lista original de Estudiantes")
for i in lista_alumnos:
    print(i)

print("\n¿Le gustaria Agregar un nuevo estudiante o Eliminar uno existente?")
opcion = (input("A- Agregar, E- Eliminar o S-Salir: ")).lower()

while opcion not in ('a','e', 's'):
    print("Letra incorrecta")
    opcion = input("A- Agregar, E- Eliminar o S-Salir: ").lower()

if opcion == 'a':
    nombre = input(f"Ingrese el nombre del nuevo estudiante: ")
    lista_alumnos.append(nombre)
elif opcion == 'e':
    elemento = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if elemento in lista_alumnos:
        lista_alumnos.remove(elemento)
        print(f"El estudiante '{elemento}' ha sido eliminado.")
    else:
        print(f"El estudiante '{elemento}' NO está en la lista.")

print("\nLista Final de Estudiantes ")
for i in lista_alumnos:
    print(i)

#------------------------------------------------------------------------------------

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

datos = [1,2,3,4,6,8,9]
print(f"Lista Original {datos}")

ultimo = datos[-1]
resto = datos[:-1]
datos_rotados_a_la_derecha = [ultimo] + resto
print("Numeros rotados")
for i in datos_rotados_a_la_derecha:
    print(i, end=" ")

#Alternativa
# print("")
# datos_rotados_bis = datos[-1:] + datos[:-1]
# print(datos_rotados_bis)

#------------------------------------------------------------------------------------

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado", "Domingo"]
indice_dia=0
suma_min = 0
suma_max = 0
minima=0
maxima=0
mayor_amplitud_termica = 0

#matriz_clima = [minimas,maximas]
matriz_clima = [[13, 22],
                [14, 27],
                [12, 18],
                [11, 21],
                [15, 24],
                [ 9, 26],
                [16, 24]]

for i in range(7):
   for j in range(2):
        if j == 0:
            suma_min += matriz_clima[i][j]
            minima = matriz_clima[i][j]
        elif j == 1:
            suma_max += matriz_clima[i][j]
            maxima = matriz_clima[i][j]
   diferencia = maxima - minima
   if mayor_amplitud_termica < diferencia:
       mayor_amplitud_termica = diferencia
       indice_dia = i


print(f"Promedio minimas {suma_min/7:.2f} y los maximos {suma_max/7:.2f}")
print(f"La mayor amplitud fue de {mayor_amplitud_termica}° el dia {dias[indice_dia]}")

#------------------------------------------------------------------------------------

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
notas_estudiantes = [[10, 9, 7],
                     [8, 7, 8],
                     [7, 8, 6],
                     [6, 2, 5],
                     [8, 4, 6]]

#Version optimizada y escalable
fila = len(notas_estudiantes)
columna = len(notas_estudiantes[0])

suma_alumnos = [0] * fila  #guardo la suma de las notas de los alumnos en una lista
suma_materias = [0] * columna #guardo la suma de las notas de las matria en una lista

for i in range(fila):
    for j in range(columna):
        nota = notas_estudiantes[i][j]
        suma_alumnos[i] += nota
        suma_materias[j] += nota

#print(suma_alumnos)
#print(suma_materias)

print("--- Promedio de cada estudiante ---")
for i in range(fila):
    promedio_alumnos = suma_alumnos[i]/columna
    print(f"Promedio del {i+1}º Alumno: {promedio_alumnos:.2f}")

print("--- Promedio de cada materia ---")
for j in range(columna):
    promedio_materia = suma_materias[j]/fila
    print(f"Promedio de la {j+1}º Materia: {promedio_materia:.2f}")

#------------------------------------------------------------------------------------

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = []

for i in range(3):
    fila = [] #para generar las listas internas
    for j in range(3):
        fila.append("-")
    tablero.append(fila) # agrego la primer fila con los "-" al tablero

for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print() # hago un salto de linea asi veo la matriz 3*3

#Variables de control
jugador = "X"
conta_jugadas = 0

while conta_jugadas < 9:
    print(f"\nTurno del jugador {jugador} ")

    fila = int(input("Ingrese la fila (0 - 2): "))
    columna = int(input("Ingrese la columna (0 - 2): "))

    if fila<0 or fila>2 or columna<0 or columna>2:
        print("Posicion fuera dle rango. Intente nuevamente")
        continue    # esto hace que ignora todo lo que esta abajo y reinicia el turno, sin perderlo

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        conta_jugadas +=1
    else:
        print("Casilla ocupada. Intente nuevamente")
        continue #vuelve a pedir la jugada. sin perder el turno

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
        print() # hago un salto de linea asi veo la matriz 3*3


print("JUEGO TERMINADO!!!")


#------------------------------------------------------------------------------------

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [  [19525, 75020, 11000,  5500, 30800, 41140, 30497],
            [15000, 5000 , 44000, 30800, 67500, 31000, 32216],
            [23400, 44000, 73694, 66000, 44000,  2000, 42182],
            [15000, 10000,  5000, 23000, 25000, 10000, 14666]]

filas = len(ventas)
columna = len(ventas[0])

suma_producto = [0] * filas
suma_dia = [0] * columna
for i in range(filas):
    for j in range(columna):
        volumen = ventas[i][j]
        suma_producto[i] += volumen
        suma_dia[j] += volumen

print(suma_producto)
print(suma_dia)

print("\nTotal vendido por cada producto")
for i in range(filas):
    print(f"El total del {i+1}° producto fue: {suma_producto[i]}")

print("\n")
maximo_dia_ventas = max(suma_dia)
dia_maximo = suma_dia.index(maximo_dia_ventas)
print(f"El dia {dia_maximo+1} fue el de mayor ventas, con un total de: {maximo_dia_ventas}")

print("\n")
maximo_producto = max(suma_producto)
producto = suma_producto.index(maximo_producto)
print(f"El producto mas vendido fue el {producto+1} con un total de ventas de {maximo_producto}")