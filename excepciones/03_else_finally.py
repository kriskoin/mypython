"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 84 """


try:
    n2 = int (input("Ingresa segundo numero: "))
except Exception as e:
    print(type(e))
    print ("Ocurrio un error")
else:
    print("No ocurrio ningun error")
finally: # se ejecuta siempre
    print("Se ejecuta siempre")
    

    
