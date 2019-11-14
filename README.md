# Emerging technologies project
## Machine learning neural newtwork

## Introduction
This project involves using the MNIST dataset to train a neural network to recognise digits sent to the network via a web app that allows the user to draw digits. The neural network or model, will be created in python using the **Keras** library. The web app is a standard HTML, Javascript and CSS configuration. And the two are connected via a python **Flask** server file which will connect to two by sending data from the web app to the neural network in the notebook.

## Tools used 
- Anaconda: A distributed system for working with machine learning in python, it has a lot of inbuilt packages needed like keras, tenorflow, numpy and matplotlib(More on these later).

- Jupyter Notebook: A python development enviroment, it works with python 3.7 and can be used with any python library, It is good for visualising the neural network and learning how it works

- Visual Studio Code: A easy to use IDE for making the Flask server and HTML web app.

## Enviroment Set Up
### Download Python
Download **Python** version 3.7 through ***Anaconda*** (Works with any OS)
[https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)

Check the version of python, open a cmd/terminal and enter
- python --version
make sure its al least version 3.7.

If you have an older version of anaconda  you can update it with
- conda update --all

### Anaconda
Comes with the following packages which will be used in the project
- Keras
- Tensorflow
- numpy
- matplotlib

All you need to install manually is jupyter notebook or jupyter lab.
cmd line for installing jupyter lab
- conda install -c conda-forge jupyterlab
or 
- pip install jupyterlab

## How to Run
### Run the notebook 
1. Clone the repository to you machine:
git clone https://github.com/aaronBurns59/4th-year-emerging-technologies-project

2. Navigate to this directory in your CMD/Terminal and enter one of the following to run it:
jupyter lab

3. It will open in an Edge browser by default just copy http://localhost:8888/ into the browser of your choice to rectify this

- If you are interested in changing the default browser to say firefox or chrome, I followed this video to do so
[https://youtu.be/8avwgjr3oTw](https://youtu.be/8avwgjr3oTw)  

## Run the Flask Server
1. Navigate to the project directories subdirectory "webapp"  
....\4th-year-emerging-technologies-project\webapp  
- python app.py
or
- env FLASK_APP=app.py flask run

## Research
### - Keras
keras is a ***high level neural networks API***. It is written in Python and can run on top of Tensorflow (Tensorflow is used in the backend). It is good for those who want to experiment quickly with neural networks in a very streamlined implementation, without knowing exactly how machine learning works.

#### Guiding Principles
1. User Friendlyness: Designed for humans, follows best practises for reducing cognitve load and offers simple and consistent APIs

2. Modularity: Fully configured **models** can be plugged together with few restrictions. ***neural layers, activation functions, optimizers etc.*** are all stand alone models that can be combine in creating **the** model for the neural network

3. Easily Extendibility: New models are simple to add ***model.add(....)***

4. Works with Python: Models are described in python code, this make it easier to debug and easier to extend.

### - Tensorflow

### - NumPy

### - MNSIT

### - Flask

## References
[https://keras.io/](https://keras.io/)

