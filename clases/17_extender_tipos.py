"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""
""" Lecture 81 """


class Lista(list):
    def prepend(self,item):
        self.insert(0,item)

lista = Lista([1,2,3])
lista.append(4)
lista.prepend(0)

print(lista)