#
# Course: ultimate python
# https://www.udemy.com/course/ultimate-python-de-cero-a-programador-experto/
# Lecture 134
#
#
#
# pip install --upgrade pipenv
# req: pipenv install requests

import requests

url = "https://jsonplaceholder.typicode.com/users"
apikey= "23r4123qwer4123erewf"
headers = {
    "Authorization":f"Bearer {apikey}"
}

r = requests.get(url,timeout=20,headers=headers)
print (r.text)

r= r.json()

for user in r:
    print(user["name"])