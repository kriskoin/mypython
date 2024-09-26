"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

punto = {
    "x": 25,
    "y": 50
         }

print (punto)
punto["z"]=45
print (punto)

punto["lala"]= "cris dice hola"

if "lala" in punto :
    print ("encontre lala",punto["lala"])

print(punto.get("x"))
print(punto.get("majorette"))
print(punto.get("majorette",666))

del punto["x"]
del (punto["y"])
print(punto)

punto ["x"]=25

for valor in punto:
    print(valor,punto[valor])

for valor in punto.items():
    print(valor)

for llave,valor in punto.items():
    print(llave,valor)


usuarios = [
    {"id":1,"nombre":"Chanchito"},
    {"id":2,"nombre":"Feliz"},
    {"id":3,"nombre":"Cris"},
    {"id":4,"nombre":"Mau"}
]

for usuario in usuarios:
    print (usuario["nombre"])