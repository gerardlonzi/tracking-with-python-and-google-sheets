import requests
import datetime as dt
import os

#post data to nutritionix Api
API_KEY = 'b7fd2c8630ec91319955073b919885c5	'
API_ID = '9c42f0be'
url_nutri_api = ' https://trackapi.nutritionix.com/v2/natural/exercise'
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
requette = requests.post(url=url_nutri_api ,json=params_nutri_Api,headers=header)
render = requette.json()
print(render)

# https://api.sheety.co/phill/myWebsite/emails

# add row to google sheet by sheety Api
url_sheety_Api = 'https://api.sheety.co/GerardLonzi/database/workouts'


now = dt.datetime.now()
date_now = now.strftime("%x")
Hour_now = now.strftime('%X')

for exo in render['exercises']:
    
    params = {
            'workouts':{
                'date':date_now,
                'time':Hour_now,
                'exercise': exo['name'].title(),
                'duration':exo['duration_min'],
                'calories':exo['nf_calories']
                }
    }

requette_to_sheety = requests.post(url_sheety_Api,json=params)
print(requette_to_sheety.text)