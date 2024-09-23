"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""


mascotas = ["Pelusa","pulga","felipe","chanchito feliz"]

for mascota in mascotas:
    print(mascota)


# we need the ele index


for mascota in enumerate(mascotas):
    print(mascota)


for mascota in enumerate(mascotas):
    print(mascota[0],mascota[1])

print("----------")
for indice, mascota in enumerate(mascotas):
    print(indice,mascota)

print("---------indice-")
print(mascotas.index("Pelusa"))

if "Wolfgang" in mascotas:
    print(mascotas.iindex("Wolfgang"))


mascotas = ["Pelusa","Wolfgang","pulga","felipe","Wolfgang","chanchito feliz"]

print (mascotas.count("Wolfgang"))