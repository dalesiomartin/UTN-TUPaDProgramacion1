# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", 'w') as archivo:
    archivo.write("Papa,2000.0,5\n")
    archivo.write("Manzana,1500.5,8\n")
    archivo.write("Banana,750.0,3\n")

#------------------------------------------------------------------#


# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea,
#  la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30


with open("productos.txt", 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")

        producto = partes[0]
        precio = partes[1]
        cantidad = partes[2]
        print(f"Producto: {producto} | Precio: ${precio} | Cantidad: {cantidad}")

#------------------------------------------------------------------#

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
#  los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad)
#  y lo agregue al archivo sin borrar el contenido existente.

print("--Lista de Productos--")
with open("productos.txt", 'r') as archivo:
    contenido = archivo.read().strip()
    print(f'{contenido}')
print("----------------------")
print("Ingrese un nuevo producto")
nombre = input("Nombre del Producto: ")
precio = float(input("Precio del Producto: "))
cantidad = int(input("Cantidad del Producto: "))

with open("productos.txt", 'a') as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")
   
print(f"\n El producto '{nombre}' ha sido agregado al archivo")

with open("productos.txt", 'r') as archivo:
    contenido = archivo.read()
    print(f'{contenido}')

#------------------------------------------------------------------#

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los 
# datos en una lista llamada productos, donde cada elemento sea un diccionario 
# con claves: nombre, precio, cantidad.
productos= []

with open("productos.txt", 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        
        nombre = partes[0]
        precio = float(partes[1])
        cantidad = int(partes[2])
        
        producto_diccionario = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        productos.append(producto_diccionario)

print("Lista de productos cargados:\n")
for i in productos:
    print(f"Nombre: {i['nombre']}, Precio: ${i['precio']}, Cantidad: {i['cantidad']}")

#------------------------------------------------------------------#

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.

print()
encontrado = False
busca_prod = input("Ingrese el nombre del producto que desea consultar: ").title()

for produc in productos:

    if produc["nombre"].title() == busca_prod:
        print("\nProducto encontrado!!")
        print(f"Producto: {produc['nombre']} | Precio: ${produc['precio']} | Cantidad: {produc['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"\nEl producto '{busca_prod}' no existe en la lista.")

#------------------------------------------------------------------#

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista

with open("productos.txt", 'w') as archivo:
    for producto in productos:
        prod_actualizado = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"

        archivo.write(prod_actualizado)

print("Archivo 'productos.txt' actualizado")
