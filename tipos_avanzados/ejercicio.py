"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""


from pprint import pprint
string = "Hola mundo esteee es mi string"

def quita_espacios(texto):
    return [char for char in texto if char != " "]

def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict:
            chars_dict[char] +=1
        else:
            chars_dict[char] = 1
    return chars_dict

def ordena(dict):
    return sorted(
        dict.items(),
        key = lambda key:key[1],
    )


def ordena2(dict):
    return sorted(
        dict.items(),
        key = lambda key:key[1],
        reverse= True,
    )


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta

def crea_mensaje (diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key,valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje

sin_espacios = quita_espacios(string)
print (sin_espacios)

contador = cuenta_caracteres(string)
pprint (contador,width=1)

ordenados = ordena(contador)
print(ordenados)

ordenados2 = ordena2(contador)
print(ordenados2)

mayores = mayores_tuplas(ordenados2)
print(mayores)

mensaje = crea_mensaje(mayores)
print (mensaje)
