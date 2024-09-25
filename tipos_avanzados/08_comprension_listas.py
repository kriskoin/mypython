"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""



usuarios = [
            ["chanchito",4],
            ["Felipe",1],
            ["Pulga",5]
            ]


nombres = []
for  usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)


nombres2= [usuario[0] for usuario in usuarios ]
print(nombres2)

# filtra
nombres3 = [usuario for usuario in usuarios if usuario[1]>2]
print(nombres3)

#filtra y transforma
nombres3 = [usuario[0] for usuario in usuarios if usuario[1]>2]
print(nombres3)

nombres4 = list(map(lambda usuario: usuario[0], usuarios))
print (nombres4)

nombres5 = list( filter (lambda usuario: usuario[1] > 2,usuarios))
print (nombres5)