"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 83 """


try:
    n1 = int (input("Ingresa primer numero: "))
    dfgdsg #esto generea un NameError exception
except ValueError as e:
    print ("Ocurrio un error ")
    print(type(e))
except NameError as e:
    print("Ocurrio un error! de tipo NameError ")



#try:
#    n2 = int (input("Ingresa segundo numero: "))
#except ValueError as e:
#    print ("Ingresa un valor numerico")
#    print(type(e))