# Repaso Python para prepararnos para crear los modulos en Odoo
# @author Eder <emarcas@aulaestudio.es>
# @version 1.0.0
# @date 2025-11-08

print('\n=========================================')
print('PARTE 1: Repaso de los conceptos básicos')
print('=========================================\n')

# 1. Variables y Tipos de Datos:
#       o Crea una variable llamada nombre_empresa y asígnale el valor "TechSolutions".
#       o Crea una variable llamada año_fundacion y asígnale el valor 2010.
#       o Imprime el tipo de dato de ambas variables.

print('\n-1: Variables y Tipos de Datos:\n')
# Creamos las dos varibles para el nombre y el año
nombre_empresa = "TechSolutions"
año_fundacion = 2010

# Imprimimos el tipo de dato que almacena cada variable
print(f"Nombre de la empresa: {nombre_empresa} y su tipo de dato es: {type(nombre_empresa)}")
print(f"Año de fundación de la empresa: {año_fundacion} y su tipo de dato es: {type(año_fundacion)}")

# 2. Estructuras de Control:
#       o Escribe un programa que pida al usuario ingresar un número y determine si es positivo, negativo o cero.
#       o Crea un bucle for que imprima los números del 1 al 10.

print('\n-2: Estructuras de Control:\n')
# Pedimos que el usuario inserte un numero por terminal
input_numero = input("Ingresa un número: ")
try:
    # Parseamos el numero a float para las comparaciones
    numero = float(input_numero)

    # Comproabamos si el numero es positivo, negativo u es 0
    if numero > 0:
        print(f"{numero} es positivo.")
    elif numero < 0:
        print(f"{numero} es negativo.")
    else:
        print(f"{numero} es cero") 

# Excepción por si el usuario escribe algo que no sea un número
except ValueError:
    print("Entrada no válida, debía ser un número")

# Hacemos un for simple para mostrar los numeros del 1 al 10
print("Números del 1 al 10")
for num in range(1,11):
    print(num)

# 3. Funciones:
#       o Define una función llamada calcular_iva que tome como parámetro el precio de un producto y devuelva el precio con el IVA (21%) incluido.
#       o Llama a la función con un precio de 100 y muestra el resultado.

print('\n-3: Funciones:')

# Creamos la funcion para devolver el precio con el IVA y solo recibe como parametro el precio
def calcular_iva(precio: float):
    return round(precio * (1 + 0.21), 2)

# Creamos una variable para almacenar el precio con el IVA calculado y lo mostramos por terminal con un mensaje
precio_con_iva = calcular_iva(100)
print(f"Si le aplicamos el 21% de IVA a 100.0€ nos quedaría en {precio_con_iva}€")

# 4. Listas y Diccionarios:
#       o Crea una lista llamada empleados con los nombres "Ana", "Carlos", "María" y "Luis".
#       o Añade un nuevo empleado llamado "Pedro" a la lista.
#       o Crea un diccionario llamado info_empleado con las claves nombre, edad y departamento, y asígnales valores correspondientes.
#       o Imprime el valor asociado a la clave departamento.

print('\n-4: Listas y Diccionarios:')
# Creamos un array simple con 4 empleados
empleados = ["Ana", "Carlos", "María", "Luis"]
# Añadimos al final de la lista anterior al empleado "Pedro"
empleados.append("Pedro")

# Creamos un objeto con el nombre, edad, departamento del empleado
info_empleado = {
    "nombre": "Pedro",
    "edad": 23,
    "departamento": "Informatica" 
}

# Imprimos el valor del departamante del objeto anterior
print(f"El departamento del empleado es: {info_empleado['departamento']}")

print('\n=========================================')
print('PARTE 2: Ejercicios para prácticar')
print('=========================================\n')

# 5. Programación Orientada a Objetos:
#       o Define una clase llamada Producto con los atributos nombre, precio y cantidad.
#       o Crea un método llamado calcular_total que devuelva el precio total del producto (precio * cantidad).
#       o Crea métodos para aumentar/disminuir la cantidad.

#       o Crea una instancia de la clase Producto y llama al método calcular_total.
#       o Crea una instancia de la clase Producto y llama al método aumentar_cantidad.
#       o Crea una instancia de la clase Producto y llama al método disminuir_cantidad.

print('\n-5: Programación Orientada a Objetos (POO):')
# Creamos la clese producto
class Producto:
    # Creamos el constructor para la clase con los atributos nombre, precio, cantidad
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    # Metodo para calcular el precio total del producto
    def calcular_total(self):
        return self.precio * self.cantidad
    
    # Metodo para aumentar la cantidad del producto
    def aumentar_cantidad(self, uds: int):
        self.cantidad += int(uds)

    # Metodo para disminuir la cantidad del producto
    def disminuir_cantidad(self, uds: int):
        self.cantidad -= int(uds)

# Creamos la instancia de la clase producto
gameboy = Producto("Anbernic RG406V", 219.99, 5)
# Creamos una variable que almacene el total del producto
gameboy_total = gameboy.calcular_total()
# Mensaje con todos los datos y el calculo del total
print(f"Datos del producto: nombre: {gameboy.nombre}, precio: {gameboy.precio}€, cantidad: {gameboy.cantidad} Uds y el total: {gameboy_total}€.")
# Aumentamos la cantidad en 2 unidades
gameboy.aumentar_cantidad(2)
# Mensaje para mostrar el aumento en la cantidad
print(f"Aumentamos el stock en 2: La cantidad actual de la {gameboy.nombre} es de {gameboy.cantidad} Uds.")
# Disminuimos la cantidad en 4 unidades
gameboy.disminuir_cantidad(4)
# Mensaje para mostrar la cantidad disminuida
print(f"Disminuimos el stock en 4: La cantidad actual de la {gameboy.nombre} es de {gameboy.cantidad} Uds.")

# 6. Manejo de Archivos:
#       o Crea un archivo de texto llamado empleados.txt y escribe en él los nombres de los empleados de la lista empleados.
#       o Lee el archivo empleados.txt e imprime su contenido.
#       o Lee un archivo CSV que contenga datos de productos (nombre, precio, cantidad) y crea una lista de objetos Producto a partir de esos datos.

print('\n-6: Manejo de Archivos:')

# Creamos el archivo empleados.txt con los empleados anteriormente definidos
archivo_empleados = open("empleados.txt", "w", encoding="utf-8")
# Recorremos la lista de empleados y escribimes el nombre de cada empleado en el archivo
for empleado in empleados:
    archivo_empleados.write(f"{empleado}\n")

# Leemos el archivo empleados.txt y imprimos su contenido
archivo_empleados = open("empleados.txt", "r", encoding="utf-8")
# Leemos el contenido del archivo y lo guardamos en la variable
contenido_empleados = archivo_empleados.read()
print(f"Contenido del archivo empleados.txt:")
print(contenido_empleados)

# Creamos el archivo productos.csv con 5 productos
archivo_productos = open("productos.csv", "w", encoding="utf-8")
# Escribimos los productos en el archivo
archivo_productos.write("Anbernic RG406V,219.99,5\n")
archivo_productos.write("AYN Thor,329.99,10\n")
archivo_productos.write("Unico Pocket NeoGeo,99.99,8\n")
archivo_productos.write("Evercade Super Pocket,59.99,12\n")
archivo_productos.write("Retroid Pocket 6,309.99,15\n")

# Creamos la lista de objetos para los productos
lista_productos = []

# Leemos el archivo productos.csv
archivo_productos = open("productos.csv", "r", encoding="utf-8")
# Recorremos cada linea de nuestro archivo
for producto in archivo_productos:
    # Recuperamos el nombre, precio y cantidad
    nombre, precio, cantidad = producto.strip().split(",")
    # Añadimos a la lista de productos la instancia rellenada con los datos recuperados
    lista_productos.append(Producto(nombre, float(precio), int(cantidad)))

# Mensaje por terminal para mostrar todos los productos del productos.csv
print("Lista productos mostrada:")
for producto in lista_productos:
    print(f"- Nombre: {producto.nombre}, precio: {producto.precio}€ y cantidad: {producto.cantidad} Uds.")
