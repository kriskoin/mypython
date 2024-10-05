#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 135
#
#
# req: pipenv install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"

respuesta = requests.get(url)

texto = respuesta.text
soup =BeautifulSoup(texto,"html.parser")

preguntas=soup.select(".s-post-summary")

for pregunta in preguntas :
    #print(pregunta)
    titulo = pregunta.select_one(".s-link").get_text().strip()
    usuario = pregunta.select_one(".s-user-card--link").get_text()
    print(f"{usuario} - Titulo : {titulo}")


# move to the next page

   