#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 101
#

from io import open

# escritura

# texto = "Hola soy cris"

# archivo = open("archivo_test.txt","w")

# archivo.write(texto)
# archivo.close()


# # lectura
# archivo = open("archivo_test.txt","r")
# texto = archivo.read()
# print(texto)
# archivo.close()


# lectura como lista
# archivo = open("archivo_test.txt","r")
# texto = archivo.readlines()
# print(texto)
# archivo.close()

# __enter__ __exit__
# with open("archivo_test.txt","r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print (linea)


# #agregar
# archivo = open("archivo_test.txt","a+")
# archivo.write("chao feos ")
# archivo.close()

#  lectura escritura

with open("archivo_test.txt","r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] ="soy feliz\n"
    archivo.writelines(texto)