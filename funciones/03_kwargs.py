"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

def get_product(**datos):
    print(datos)
    print(datos["id"],datos["name"])


get_product(id="id",name="my name")