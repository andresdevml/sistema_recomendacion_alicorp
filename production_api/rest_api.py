

# implementacion de la API que dara servicio

from flask import Flask
from flask import jsonify
from flask import request
import pickle
import numpy as np 
import torch


app=Flask(__name__)

@app.route('/predict',methods=['POST'])
def predict():
	# input_data sera un json, para comodidad del usuario servido 
	
	try:
	
		input_data=np.array(request.get_json(force=True)['data'])
	
		prediction=model.predict(user_ids=input_data,
                      item_ids=unique_product_id)

		return jsonify(y_pred=prediction)
		
	except:
		print('\n\nHubo un error')
	
if __name__=='__main__':
	
	# extraemos el modelo

	model = torch.load('/model.sav')
	
	# extraemos el id de los productos 
	
	df_user=pd.read_csv(filepath_or_buffer=dir_data+'/df_user.csv')
	
	unique_product_id=np.array(df_user['product_id'].unique())
	
	app.run(port=2205,debug=True)
	
