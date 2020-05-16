

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':48, 'sex':1, 'chest pain type ':2, 'resting bp s	':164 , 'cholesterol':220 , 'fasting blood sugar	':1 , 'resting ecg	':0 , 'max heart rate	':160 , 'exercise angina	':1 , 'oldpeak':1.2 , 'ST slope	':1})
print(r.json())# -*- coding: utf-8 -*-

