# aqui haremos las peticiones y verificaremos todo anda bien 

import requests
import pandas as pd 
import numpy as np

if __name__=='__main__':
	url = 'http://127.0.0.1:2205/predict'

	# extraemos data para hacer una verificacion de servidor 

	X=user_id=df_user['customer_id'].iloc[18]

	input_data=X.tolist()

	response= requests.post(url,json={'data':input_data})

	print(np.array(response.json()['y_pred']))
	print(Y)
