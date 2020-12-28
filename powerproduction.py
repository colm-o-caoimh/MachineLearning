import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tensorflow.keras as kr
from ipynb.fs.defs.mls_project2020 import model_predict

pp = pd.read_csv('powerproduction.csv')
#print(pp.head())

speed_df = pp.drop('power',axis='columns')
#print(speed_df)

power_df = pp.drop('speed',axis='columns')
#print(power_df)

reg = LinearRegression()
reg.fit(speed_df, power_df)
#print(reg.predict([[9.746]]))


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
 
@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():

	wind_speed = request.form['email']
	# name = request.form['name']

	#if name and wind_speed:
	if float(wind_speed) > 0:
		# power = reg.predict([[float(wind_speed)]])
		power = model_predict([[float(wind_speed)]])
		power = power.item(0)

		if power < 0:
			return jsonify({'name' : 0})

		return jsonify({'name' : float(power)})

	return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)