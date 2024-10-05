#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 133
#
#
#
# pip install --upgrade pipenv
# req: pipenv install requests

import requests

url = "https://jsonplaceholder.typicode.com/users"
r = requests.get(url,timeout=20)
print (r.text)

r= r.json()

for user in r:
    print(user["name"])