"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""


print ("Bienvenidos a la calculadora")
print ("Para salir escrive salir")
print ("Las operaciones son suma, resta, multiplicacion , div")

resultado = ""

while True:
    if not resultado:
        resultado = input ("ingrese numero: ")
        if resultado.lower() == "salir":
            break
    
    op = input ("Ingresa operacion: ")
    if op.lower() == "salir" :
        break
    
    n2 = input ("Ingresa siguiente numero: ")

    if n2.lower() == "salir" :
        break

    n2 = int(n2)
    resultado = int (resultado)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print ("Operacion no valida")
        break   

    print (f"El resultado es {resultado}")