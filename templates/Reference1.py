#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/raj")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program and I'm  enjoying it"

@app.route("/raj_1")
def second_flask():
    return "Python is awsome!"

app.run(debug=True)

#run the application on local server
app.run()
