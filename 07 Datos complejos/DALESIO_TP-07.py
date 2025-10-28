# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300 

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}


precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print(f'Precio de Frutas del ejerc 1: \n{precios_frutas}\n')

# ---------------------------------------------------- # 

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800 

precios_frutas_ejerc2 = precios_frutas

precios_frutas_ejerc2 ['Banana'] = 1330
precios_frutas_ejerc2 ['Manzana'] = 1700
precios_frutas_ejerc2 ['Melón'] = 2800

print(f'Precio de Frutas del ejerc 2: \n{precios_frutas_ejerc2}\n')

precios_frutas_ejerc3 = precios_frutas_ejerc2

# ---------------------------------------------------- #

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios. 

lista_frutas = list(precios_frutas_ejerc3.keys())
print(f'Listado de Frutas: (ejerc 3): \n{lista_frutas}\n')

# ---------------------------------------------------- #

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:
contactos={}

for i in range(5):
    nombre = input("Ingrese su nombre: ")
    numero = int(input("Ingrese su numero de contaco: "))
    contactos[nombre]=numero

opcion= input("Quiere consultar algun contacto: s(Si) o n(No): ").lower()

if opcion == 's':
    consulta = input("Ingrese el nombre del contacto: ")
    if consulta in contactos:
        print(f"Su teléfono es: {contactos[consulta]}")
    else:
        print("Ese contacto no existe.")

print("fin de la consulta")

# ---------------------------------------------------- #

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo: 

frase = input("Ingrese una frase: ").lower()

lista_frase = frase.split()

#Conjunto
print("Palabras Únicas:")
conj_texto = set(lista_frase)
print(f'{conj_texto}  \n')

#Diccionario
conteo_palaras = {}
for palabra in lista_frase:
    if palabra in conteo_palaras:
        conteo_palaras[palabra]+=1
    else:
        conteo_palaras[palabra]=1

print("Cantidad Palabras")
print(conteo_palaras)

# ---------------------------------------------------- #

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. Ejemplo: 

alumnos={}


for i in range(3):
    nombre= input("Ingrese su nombre: ")
    
    notas=[]
    for j in range(3):
        nota = float(input(f"Ingrese la {j+1}º nota: "))
        notas.append(nota)

    alumnos[nombre]=tuple(notas) 


print(alumnos)

print("\n Notas de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas)/len(notas)
    print(f"{nombre}: notas {notas}, con promedio {promedio:.2f}")

# ---------------------------------------------------- #

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y 
# Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial1 = {10, 9, 8, 7, 6, 8}
parcial2 = {9, 8, 8, 7}

ambos = parcial1 & parcial2 #aprobaron ambos parciales

solo_uno = parcial1 ^ parcial2 #aprobaron solo uno de los dos

al_menos_uno = parcial1 | parcial2 #aprobaron al menos un parcial(unión)

# Mostrar resultados
print(f"Estudiantes que aprobaron ambos parciales: {ambos}")
print(f"Estudiantes que aprobaron solo uno de los dos: {solo_uno}")
print(f"Estudiantes que aprobaron al menos un parcial: {al_menos_uno}")

# ---------------------------------------------------- #

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

inventario = {'azucar': 50, 'arroz': 30, 'fideos': 20}

while True:
    print("\nOpciones:")
    print("1: Consultar stock de un producto")
    print("9: Salir")

    opcion = input("Ingrese el número de su opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto que desea consultar: ").lower()
        if producto in inventario:
            print(f'El producto {producto} tiene {inventario[producto]} unidades en stock')

            opcion_agregar = input("¿Desea agregar unidades? (s/n): ").lower()
            
            if opcion_agregar == 's':
                cantidad = int(input("¿Cuántas unidades desea agregar?: "))
                inventario[producto] += cantidad
                print(f"Inventario actualizado: {producto} con {inventario[producto]} unidades.")
            else:
                print("No se realizaron cambios en el inventario.")
        
        else:
            print(f"El producto '{producto}' no existe en el inventario.")
            
            opcion_agregar_producto = input("¿Desea agregarlo al inventario? (s/n): ").lower()

            if opcion_agregar_producto == 's':
                cantidad = int(input("¿Cuántas unidades desea agregar?: "))
                inventario[producto] = cantidad
                print(f"Producto '{producto}' agregado con {cantidad} unidades.")
            else:
                print("No se agregó el producto.")

    elif opcion == '9':
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida. Por favor, elija 1 o 9.")


# ---------------------------------------------------- #

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y 
# los valores sean eventos. Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ('Lunes', '10:00'): 'Entrenamiento',
    ('Martes', '14:30'): 'Clase de inglés',
    ('Jueves', '09:00'): 'Reunión trabajo' }

# print("Agenda semanal:")
# for clave, evento in agenda.items():
#     print(f'{clave}: {evento}')

print("Consulte su agenda semana\n")

dia = input("Ingrese el día que desea consultar: ").title()
hora = input("Ingrese la hora (formato HH:MM): ")

if (dia,hora) in agenda:
      print(f"En {dia} a las {hora} tenés: {agenda[(dia, hora)]}")
else:
    print(f"No hay ninguna actividad registrada para {dia} a las {hora}.")


# ---------------------------------------------------- #

# 10) Dado un diccionario que mapea nombres de países con sus capitales, 
# construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:

original = {"Argentina": "Buenos Aires", "Peru": "Lima", "Chile": "Santiago"}

invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais


print(f"Diccionario Original \n {original} \n")
print(f"Diccionario Invertido \n {invertido}")