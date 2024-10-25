import random
import string
import os
from passlib.hash import md5_crypt
from passlib.hash import sha512_crypt

# Borramos los datasets antiguos
archivos = os.listdir("datasets_1")
for archivo in archivos:
    if os.path.isfile("datasets_1/"+archivo):
        os.remove("datasets_1/"+archivo)

archivos = os.listdir("datasets_2")
for archivo in archivos:
    if os.path.isfile("datasets_2/"+archivo):
        os.remove("datasets_2/"+archivo)

archivos = os.listdir("contraseñas_1")
for archivo in archivos:
    if os.path.isfile("contraseñas_1/"+archivo):
        os.remove("contraseñas_1/"+archivo)

archivos = os.listdir("contraseñas_2")
for archivo in archivos:
    if os.path.isfile("contraseñas_2/"+archivo):
        os.remove("contraseñas_2/"+archivo)

print("Datasets antiguos borrados")

# Función para generar las contraseñas y cifrarlas con md5
def generar_contraseña_md5(longitud, caracteres):
    contraseña = ""
    for _ in range(longitud):
        caracter = random.choice(caracteres)
        contraseña += caracter
    return [contraseña,md5_crypt.hash(contraseña)]

# Función para generar las contraseñas y cifrarlas con sha512
def generar_contraseña_sha512(longitud, caracteres):
    contraseña = ""
    for _ in range(longitud):
        caracter = random.choice(caracteres)
        contraseña += caracter
    return [contraseña,sha512_crypt.hash(contraseña)]

# Funciones para generar las contraseñas y cifrarlas con md5 a partir del diccionario
# Se duplica la palabra
def generar_contraseña_md5_diccionario_1(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    contraseña = palabra + palabra
    return [contraseña,md5_crypt.hash(contraseña)]

# Se añade la palabra sin la primera letra al principio y 54 al final
def generar_contraseña_md5_diccionario_2(caracteres):
    contraseña = "54"
    palabra = random.choice(caracteres)
    contraseña = palabra[1:] + contraseña
    return [contraseña,md5_crypt.hash(contraseña)]

# Se invierte la palabra y se pone en mayúsculas
def generar_contraseña_md5_diccionario_3(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
    contraseña = invertida.upper()
    return [contraseña,md5_crypt.hash(contraseña)]

# Se añade la palabra invertida al final
def generar_contraseña_md5_diccionario_4(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    contraseña += palabra
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
    contraseña += invertida
    return [contraseña,md5_crypt.hash(contraseña)]

# Se cambia el primer carácter por un ? y se añade al principio un %
def generar_contraseña_md5_diccionario_5(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    contraseña = "%" + "?" + palabra[1:]
    return [contraseña,md5_crypt.hash(contraseña)]

# Funciones para generar las contraseñas y cifrarlas con sha512 a partir del diccionario
# Se duplica la palabra
def generar_contraseña_sha512_diccionario_1(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    contraseña = palabra + palabra
    return [contraseña,sha512_crypt.hash(contraseña)]

# Se añade la palabra sin la primera letra al principio y 54 al final
def generar_contraseña_sha512_diccionario_2(caracteres):
    contraseña = "54"
    palabra = random.choice(caracteres)
    contraseña = palabra[1:] + contraseña
    return [contraseña,sha512_crypt.hash(contraseña)]

# Se invierte la palabra y se pone en mayúsculas
def generar_contraseña_sha512_diccionario_3(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
    contraseña = invertida.upper()
    return [contraseña,sha512_crypt.hash(contraseña)]

# Se añade la palabra invertida al final
def generar_contraseña_sha512_diccionario_4(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    contraseña += palabra
    invertida = ""
    for letra in palabra:
        invertida = letra + invertida
    contraseña += invertida
    return [contraseña,sha512_crypt.hash(contraseña)]

# Se cambia el primer carácter por un ? y se añade al principio un %
def generar_contraseña_sha512_diccionario_5(caracteres):
    contraseña = ""
    palabra = random.choice(caracteres)
    contraseña = "%" + "?" + palabra[1:]
    return [contraseña,sha512_crypt.hash(contraseña)]

# Generación de contraseñas con md5

# Primer tipo (entre 3 y 7 de longitud y solo letras minúsculas)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        contraseña = generar_contraseña_md5(i, string.ascii_lowercase)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])
    
    with open('contraseñas_1/dataset_a_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_1/dataset_a_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Segundo tipo (entre 3 y 7 de longitud y solo letras mayúsculas)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        contraseña = generar_contraseña_md5(i, string.ascii_uppercase)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])

    with open('contraseñas_1/dataset_b_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_1/dataset_b_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Tercer tipo (entre 3 y 7 de longitud y solo números)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        contraseña = generar_contraseña_md5(i, string.digits)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])

    with open('contraseñas_1/dataset_c_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_1/dataset_c_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Cuarto tipo (entre 3 y 7 de longitud y con letras minúsculas, mayúsculas, números y símbolos)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        contraseña = generar_contraseña_md5(i, caracteres)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])

    with open('contraseñas_1/dataset_d_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_1/dataset_d_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Quinto tipo (usando palabras de un diccionario)
with open('diccionario.txt', 'r') as file:
    palabras = file.read().splitlines()

dataset = []
contraseñas = []

# Primer tipo
for _ in range(100):
    contraseña = generar_contraseña_md5_diccionario_1(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_1/dataset_e_1.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []

with open('datasets_1/dataset_e_1.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Segundo tipo
for _ in range(100):
    contraseña = generar_contraseña_md5_diccionario_2(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_1/dataset_e_2.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_1/dataset_e_2.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Tercer tipo
for _ in range(100):
    contraseña = generar_contraseña_md5_diccionario_3(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_1/dataset_e_3.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_1/dataset_e_3.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Cuarto tipo
for _ in range(100):
    contraseña = generar_contraseña_md5_diccionario_4(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_1/dataset_e_4.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_1/dataset_e_4.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Quinto tipo
for _ in range(100):
    contraseña = generar_contraseña_md5_diccionario_5(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_1/dataset_e_5.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_1/dataset_e_5.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

print("Datasets nuevos de MD5 generados")

# Generación de contraseñas con sha512

# Primer tipo (entre 3 y 7 de longitud y solo letras minúsculas)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        contraseña = generar_contraseña_sha512(i, string.ascii_lowercase)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])
    
    with open('contraseñas_2/dataset_a_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_2/dataset_a_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Segundo tipo (entre 3 y 7 de longitud y solo letras mayúsculas)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        contraseña = generar_contraseña_sha512(i, string.ascii_uppercase)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])

    with open('contraseñas_2/dataset_b_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_2/dataset_b_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Tercer tipo (entre 3 y 7 de longitud y solo números)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        contraseña = generar_contraseña_sha512(i, string.digits)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])

    with open('contraseñas_2/dataset_c_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_2/dataset_c_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Cuarto tipo (entre 3 y 7 de longitud y con letras minúsculas, mayúsculas, números y símbolos)
for i in range(3,8):
    dataset = []
    contraseñas = []
    for _ in range(100):
        caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        contraseña = generar_contraseña_sha512(i, caracteres)
        contraseñas.append(contraseña[0])
        dataset.append(contraseña[1])

    with open('contraseñas_2/dataset_d_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(contraseñas))

    with open('datasets_2/dataset_d_{}.txt'.format(i-2), 'w') as file:
        file.write('\n'.join(dataset))

# Quinto tipo (usando palabras de un diccionario)
with open('diccionario.txt', 'r') as file:
    palabras = file.read().splitlines()

dataset = []
contraseñas = []

# Primer tipo
for _ in range(100):
    contraseña = generar_contraseña_sha512_diccionario_1(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_2/dataset_e_1.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []

with open('datasets_2/dataset_e_1.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Segundo tipo
for _ in range(100):
    contraseña = generar_contraseña_sha512_diccionario_2(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_2/dataset_e_2.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_2/dataset_e_2.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Tercer tipo
for _ in range(100):
    contraseña = generar_contraseña_sha512_diccionario_3(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_2/dataset_e_3.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_2/dataset_e_3.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Cuarto tipo
for _ in range(100):
    contraseña = generar_contraseña_sha512_diccionario_4(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_2/dataset_e_4.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_2/dataset_e_4.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

# Quinto tipo
for _ in range(100):
    contraseña = generar_contraseña_sha512_diccionario_5(palabras)
    contraseñas.append(contraseña[0])
    dataset.append(contraseña[1])

with open('contraseñas_2/dataset_e_5.txt', 'w') as file:
    file.write('\n'.join(contraseñas))
    contraseñas = []
    
with open('datasets_2/dataset_e_5.txt', 'w') as file:
    file.write('\n'.join(dataset))
    dataset = []

print("Datasets nuevos de SHA-512 generados")