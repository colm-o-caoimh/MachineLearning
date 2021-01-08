# mls_project2020
Machine Learning and Statistics project
***
In this project I create a web service that uses machine learning to make predictions based on the data set 'powerproduction', found in this repository. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. 

The python script contained in the repository uses the Flask microweb framework to create a web service. It is accompanied by the frontend html and separate javascript file to handle the HTTP requests. The web service uses forms submitted using AJAX with jQuery and is based on a structure I found on github.com [1]. The web service enables a user to input values for wind speed and get a response containing the corresponding predicted wind turbine power output based on the model produced above.

## In this repository

### Jupter notebook
The repository contains a jupyter notebook which details the process I took in producing the model that predicts wind turbine power output. I provide a description of the processes taken to arrive at the model chosen, accompanied by the code used to develop it. I compare regression built models using `scikit-learn` as well as neural network models built using `tensorflow`

### powerproduction.py
Python file which implements the server. The server interacts with Python `Flask`, mapping http requests from the browser to the functions. It also interacts with the html and javascript files in this repository to handle the requests

### Templates folder
This folder contains the html file used to display front end user interface

### static/js folder
The js folder contains the file form.js which makes ajax requests

### Dockerfile
Contains the commands a user can call to assemble an image

### requirements.txt
Text file specifying what python packages are necessary to run the web app

### final_model.h5
Neural network model used in the web app

### powerproduction.csv
csv file containing *powerproduction* data set used to build model

### .gitignore file
tells git which files to ignore 

### .dockerignore
tells Docker which files to ignore


## References
[1] Herbert, A.; An example of a form submitted using AJAX with jQuery and Flask; https://github.com/PrettyPrinted/AJAX_Forms_jQuery_Flask
