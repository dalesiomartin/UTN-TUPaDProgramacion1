# 1) Factorial recursivo

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo (n-1)


num_usuario = int(input("Ingrese un valor entero para factorizar: "))
print(f"Factoriales hasta {num_usuario}:")

for i in range(1, num_usuario+1):
    resultado = factorial_recursivo(i)
    print(f"{i}! = {resultado}")

#-----------------------------------------------------------

# 2) Serie de Fibonacci recursiva

def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1)+fibonacci_recursivo(posicion-2)


posicion_usuario = int(input("Ingrese un valor entero para calcular el valor de la serie de Fibonacci: "))

print(f"Serie hasta la posición {posicion_usuario}:")

for i in range(posicion_usuario+1):
    print(fibonacci_recursivo(i))

#-----------------------------------------------------------

# 3) Potencia recursiva

def potencia_recursiva(b,e):
    if e == 0:
        return 1
    else:
        return b * potencia_recursiva(b, e - 1)

base=2
exponente = 4

print(f"{base} elevado a {exponente}: {potencia_recursiva(base, exponente)}") 

#-----------------------------------------------------------

# 4) Conversión decimal a binario recursiva

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        cociente = n // 2
        resto = n % 2

        return decimal_a_binario(cociente) + str(resto)

num = 15
print(f"Decimal {num} en Binario: {decimal_a_binario(num)}")


#-----------------------------------------------------------

# 5) Verificar si una palabra es palíndromo

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])
    

palabra_modelo = "radar"

print(f"'{palabra_modelo}' es palíndromo: {es_palindromo(palabra_modelo)}")


#-----------------------------------------------------------

# 6) Suma de dígitos recursiva

def suma_digitos(num):
    if num == 0:
        return 0
    else:
        return (num%10) + suma_digitos(num//10)

numero=305
print(f"Suma dígitos de {numero}: {suma_digitos(numero)}")

#-----------------------------------------------------------

# 7) Contar bloques de una pirámide

def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)

num = 4
print(f"Bloques para numero={num} es: {contar_bloques(num)}")

# #-----------------------------------------------------------

# 8) Contar cuántas veces aparece un dígito en un número

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
         return contar_digito(numero // 10, digito)


numero = 12233421
digito = 2

print(f"Conteo de '{digito}' en {numero}: {contar_digito(numero, digito)}")