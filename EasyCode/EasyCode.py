# Crear una lista vacía:

import random


def crear_lista_enteros(nombre=input(),cantidad=input()):
    nombre = [int() for i in range(cantidad)]
    print(f"{nombre}, se ah creado con exito")

def crear_lista_floats(nombre=input(),cantidad=input()):
    nombre = [int() for i in range(cantidad)]
    print(f"{nombre}, se ah creado con exito")

def crear_lista_str(nombre=input(),cantidad=input()):
    nombre = [int() for i in range(cantidad)]
    print(f"{nombre}, se ah creado con exito")

# Añadir un elemento a una lista:

def añadir_a_lista(array, elemento):

    if not isinstance(array, list):
        raise TypeError("La lista debe ser de tipo list/tupple.")

    array = array[:] + elemento

    return array

array = ["valor0","valor1","valor2"]

print(añadir_a_lista(array,["valor3"]))
    

# Eliminar un elemento de una lista:

def eliminar_de_lista(array, elemento):

    return [item for item in array if item != elemento]
array = ["valor0", "valor1", "valor2"]

print(eliminar_de_lista(array, "valor1"))

# Ubicar un elemento de la lista:

def encontrar_indice(lista,valor):
    cantidad = 0
    for elemento in lista:
        cantidad += 1

    for valores in range(cantidad):
        
        if lista[valores] == valor:
            return valores


# Obtener el tamaño de una lista:

def obtener_tamaño_lista(lista):
    cantidad = 0
    for elemento in lista:
        cantidad += 1
    return cantidad

# Crear un diccionario vacío:

def crear_diccionario():
    return {}

# Añadir una clave-valor a un diccionario:

def añadir_clave_valor_a_diccionario(diccionario, clave, valor):
    diccionario[clave] = valor

# Obtener el valor de una clave de un diccionario:

def obtener_valor_de_clave_de_diccionario(diccionario, clave):
    return diccionario[clave]

# Eliminar una clave de un diccionario:

def eliminar_clave_de_diccionario(diccionario, clave):
    del diccionario[clave]

def sumar(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def promediar(numeros):
    suma = 0
    cantElement = 0
    for numero in numeros:
        suma += numero
        cantElement += 1
    return suma/cantElement

def obtener_cantidad_objetos_array(array):
    cantidad_objetos = 0
    for elemento in array:
        cantidad_objetos += 1
    return cantidad_objetos

# Leer un archivo de texto
def leer_archivo(archivo):
    with open(archivo) as f:
        data = f.readlines()
    return data

# Escribir un archivo de texto
def escribir_archivo(archivo, data):
    with open(archivo, "w") as f:
        for linea in data:
            f.write(linea)

# Generar un número aleatorio entre 0 y 1
def generar_numero_aleatorio():
    return random.random()

# Generar un número aleatorio entre un rango dado
def generar_numero_aleatorio_entre(min, max):
    return random.randint(min, max)

# Comprobar si una variable es igual a un valor
def es_igual(variable, valor):
    return variable == valor

# Comprobar si una variable es mayor o igual que un valor
def es_mayor_igual(variable, valor):
    return variable >= valor

# Comprobar si una variable es menor o igual que un valor
def es_menor_igual(variable, valor):
    return variable <= valor

def es_menor(variable,valor):
    return variable < valor

def es_mayor(variable,valor):
    return variable > valor

# Iterar sobre una lista
def iterar_lista(lista):
    for elemento in lista:
        pass

def leer_archivo(archivo):
    with open(archivo) as f:
        data = f.readlines()
    return data

def escribir_archivo(archivo, data):
    with open(archivo, 'w') as f:
        for linea in data:
            f.write(linea)

# encontrar_indice(array,"coco")