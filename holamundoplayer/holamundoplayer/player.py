#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 128
#

"""
Esta es la documentaacion de player
"""

class Player:
    """
        Esta clase crea un reproductor de musica
    """

    def play (self,song):
        """
        Reproduce la cancion que recibio del constructor

        Parameters:
         song (str) : este es un string con el path de la cancion

        Returns:
        int: devuelve 1 is ok , 0 on error
        """
        print("Reproduciendo cancion")