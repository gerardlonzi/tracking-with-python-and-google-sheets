import requests
API_KEY = 'b7fd2c8630ec91319955073b919885c5	'
API_ID = '9c42f0be'
url = ' https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_text = input("Tell me which exercises you did: ")

header ={
    'x-app-id':API_ID,
    'x-app-key':API_KEY
}

params_nutri_Api = {
    'query':exercise_text,
    'gender':'male',
    'weight_kg':70,
    'height_cm': 170,
    'age': 20
    
}
requette = requests.post(url=url ,json=params_nutri_Api,headers=header)
print(requette.json())

