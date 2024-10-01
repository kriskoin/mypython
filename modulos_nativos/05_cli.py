#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 118
#

import sys
# print(sys.argv)

def cli(args):
    if len(args) == 1:
        print ("No se pasaron argumentos")
        return

    if len(args) != 3 :
        print ("se necesitan 2 argumentos")
        return

    print("Aca ocurre la magia")

cli (sys.argv)