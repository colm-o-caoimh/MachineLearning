# MachineLearningProject
Purpose: College Project | Module: Machine Learning and Statistics
***
In this project I build a web application that uses machine learning to make predictions based on the 'powerproduction' data set, found in this repository. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values. 

The python script uses the Flask microweb framework to build the application. It allows users to input wind speed values and get a response containing the corresponding predicted wind turbine power output based on the model produced above.

## In this repository

* **Jupter notebook**: Details the process undertaken to build the predictive model. I describe the journey taken to arrive at the model chosen, with all code and visualizations included. I compare various regression models using Python's machine learning library `scikit-learn` and multi-platform library `tensorflow` (for neural network models)

* **powerproduction.py**: Python file which uses Flask to implement the server and maps http requests from the browser to the functions. It also interacts with the html and javascript files in this repository to handle the requests

* **Templates folder**: Contains html file for front end user interface

* **static/js folder**: JavaScript file which makes ajax requests

* **Dockerfile**: Contains the commands a user can call to assemble an image

* **requirements.txt**: Text file specifying what python packages are necessary to run the web app

* **final_model.h5**: Predictive model used in the web app

* **powerproduction.csv**: csv file containing *powerproduction* data set used to build model

* **.gitignore file** 

* **.dockerignore**

