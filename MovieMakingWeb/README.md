# CS235FlixSkeleton
Python project for the 2020 S2 CompSci 235 practical assignment CS235Flix.

## Description  
This is a web application for CompSci 235 Movie Making Website practical assignment. Different python libraries are used such as Flask framework, Jinja templating and WTForms. Additionally, Flask Blueprints are used to create different sections of movies, actors, genres, users, and many more. Testing includes unit and end-to-end testing using pytest. Project runs in PyCharm IDE.

## Installation
You have to install venv environment into your computer. In your terminal, type the following:
`
$ python3 -m pip install --user virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
`  
Open Pycharm and set the virtual environment. Go 'File' -> 'Settings' and select the project. Select 'Project Interpreter', then click on the gearwheel icon and choose 'Add'. Click 'Existing environment' to select the virtual environment

## Execution  
Within the project's directory's terminal, type the following:  
`
$ python -m flask run
`
