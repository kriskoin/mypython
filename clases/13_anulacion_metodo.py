"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""



class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("Vuela ave")

class Pato(Ave):
    def __init__(self):
        super().__init__() # aqui pone el attributo volador como parte de Pato
        self.nada = True

    def vuela(self):
        super().vuela()
        print("Vuela pato")

pato = Pato()
pato.vuela()