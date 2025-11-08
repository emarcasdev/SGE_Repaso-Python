# Repaso de Python para Sistemas de Gestión Empresarial

## Objetivo:
Repasar los conceptos fundamentales de Python para preparar a los alumnos en el desarrollo de módulos Odoo.

---

## Parte 1: Repaso de Conceptos Básicos de Python

### 1. Variables y Tipos de Datos:
- Crea una variable llamada `nombre_empresa` y asígnale el valor `"TechSolutions"`.
- Crea una variable llamada `año_fundacion` y asígnale el valor `2010`.
- Imprime el tipo de dato de ambas variables.

### 2. Estructuras de Control:
- Escribe un programa que pida al usuario ingresar un número y determine si es positivo, negativo o cero.
- Crea un bucle `for` que imprima los números del `1` al `10`.

### 3. Funciones:
- Define una función llamada `calcular_iva` que tome como parámetro el precio de un producto y devuelva el precio con el IVA (21%) incluido.
- Llama a la función con un precio de `100` y muestra el resultado.

### 4. Listas y Diccionarios:
- Crea una lista llamada `empleados` con los nombres `"Ana"`, `"Carlos"`, `"María"` y `"Luis"`.
- Añade un nuevo empleado llamado `"Pedro"` a la lista.
- Crea un diccionario llamado `info_empleado` con las claves `nombre`, `edad` y `departamento`, y asígnales valores correspondientes.
- Imprime el valor asociado a la clave `departamento`.

---

## Parte 2: Repaso de ejercicios complejos

### 5. Programación Orientada a Objetos:
- Define una clase llamada `Producto` con los atributos `nombre`, `precio` y `cantidad`.
- Crea un método llamado `calcular_total` que devuelva el precio total del producto (`precio * cantidad`).
- Crea métodos para aumentar/disminuir la cantidad.
- Crea una instancia de la clase `Producto` y llama al método `calcular_total`.
- Crea una instancia de la clase `Producto` y llama al método `aumentar_cantidad`.
- Crea una instancia de la clase `Producto` y llama al método `disminuir_cantidad`.

### 6. Manejo de Archivos:
- Crea un archivo de texto llamado `empleados.txt` y escribe en él los nombres de los empleados de la lista `empleados`.
- Lee el archivo `empleados.txt` e imprime su contenido.
- Lee un archivo CSV que contenga datos de productos (`nombre`, `precio`, `cantidad`) y crea una lista de objetos `Producto` a partir de esos datos.
