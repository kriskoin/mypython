"""ultimate python"""
"""https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/"""

class Coordenadas:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self,otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __ne__(self,otro): # se aunto infiere
        return self.lat != otro.lat or self.lon != otro.lon
    

    def __lt__ (self,otro):
        return self.lat + self.lon < otro.lat+otro.lon
    

    def __le__(self,otro):
        return self.lat + self.lon <= otro.lat+otro.lon
        
    


coords = Coordenadas (45,27)

coords2 = Coordenadas (45,27)
print (coords , coords2)
print (coords == coords2)
print (coords != coords2)
coords3 = Coordenadas (44,27)
print (coords3 < coords2)
print (coords3 <= coords2)