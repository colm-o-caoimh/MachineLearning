import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tensorflow.keras as kr
from flask import Flask, render_template, request, jsonify


# load saved model
new_model = kr.models.load_model('final_model.h5')

app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	wind_speed = request.form['speed']

	# return 0 for wind speeds below 0.3 and above 24.499
	if float(wind_speed) > 24.499 or float(wind_speed) < 0.3:
		power = 0
		
		return jsonify({'name' : float(power)})
		
	# pass to model for wind speeds between 0.3 and 24.499	
	elif 0.3 < float(wind_speed) < 24.99:
		power = new_model.predict([[float(wind_speed)]])
		power = power.item(0)


		return jsonify({'name' : float(power)})

	
	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)