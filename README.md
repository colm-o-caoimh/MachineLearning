# mls_project2020
Machine Learning and Statistics project
***
In this project I create a web service that uses machine learning to make predictions based on the data set 'powerproduction', found in this repository. The goal is to produce a model that accurately predicts wind turbine power output from wind speed values, as in the data set. 

The repository contains a jupyter notebook which details the process I took in producing the model that predicts wind turbine power output. I provide a description of the processes taken to arrive at the model chosen, accompanied by the code used to develop it. It also contains visualisations of the data at relevant intervals.

The python script contained in the repository uses the Flask microweb framework to create a web service. It is accompanied by the frontend html and separate javascript file to handle the HTTP requests. The web service uses forms submitted using AJAX with jQuery and is based on a structure I found on github.com [1]. The web service enables a user to input values for wind speed and get a response containing the corresponding predicted wind turbine power output based on the model produced above.

[1] Herbert, A.; An example of a form submitted using AJAX with jQuery and Flask; https://github.com/PrettyPrinted/AJAX_Forms_jQuery_Flask
